from pydbus import SessionBus
from gi.repository import GLib
import json
import hashlib
import getpass
import os

# This is the path where the locked config file is
CONFIG_FILE = os.path.expanduser("~/.age_control_config.json") 

# This hashes the password
def hash_password(password, salt=None):
    # Simple SHA-256 hashing with a salt to keep it secure but not annoying
    if salt is None:
        salt = os.urandom(16).hex()
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed, salt

def save_config(bracket, password):
    # Saves the age bracket and configured password to a file
    hashed_pw, salt = hash_password(password)
    config = {
        "bracket": bracket,
        "hash": hashed_pw,
        "salt": salt
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
    # Set file permissions so only the current user can read/write the file
    os.chmod(CONFIG_FILE, 0o600)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None

# We removed the old method of getting age brackets in favor of this:
def get_bracket():
    config = load_config()

    # If config exists, we verify password before allowing changes
    if config:
        print("Age Control Management: \n")
        entered_pw = getpass.getpass("Enter Parent Password to modify settings.")
        test_hash, _ = hash_password(entered_pw, config['salt'])

        if test_hash != config['hash']:
            print("Incorrect password. The system will continue to use the existing bracket.")
            return config['bracket']
    else:
        print("Initial Setup: Create Parent Password: \n")
        print("Enter in a Parent Password to lock this system utility. \n")
        new_pw = getpass.getpass("Set a new Parent Password: ")
        config = {"bracket": "Unknown"} # placeholder
        save_config("Unknown", new_pw) # Initial save to establish password

    print("Selet Age Bracket: \n")
    print("1. Under 13\n2. 13-15\n3. 16-17\n4. 18+")

    choice = input("Choice: ")
    brackets = {"1": "Under 13", "2": "13-15", "3": "16-17", "4": "18+"}
    selected = brackets.get(choice, "Unknown")


    #password verification logic to ensure there are no mistakes and prevent tampering
    confirm_pw = getpass.getpass("Confirm Password to save changes: ")
    test_hash, _ = hash_password(confirm_pw, config['salt'])

    if test_hash == config['hash']:
        save_config(selected, confirm_pw)
        return selected
    else:
        print("Verification failed. Changes not saved.")
        return config['bracket']

# password verification is done in a separate function
def verify_password(config):
    # Forces password check before any settings can be changed
    entered_pw = getpass.getpass("Enter Parent Password to proceed: ")
    test_hash, _ = hash_password(entered_pw, config['salt'])
    if test_hash != config['hash']:
        print("Access Denied: Incorrect password.")
        return False
    return True

# allows you to change the password
def change_password():
    config = load_config()
    if not config:
        print("No configuration found. Please run initial setup.")
        return
    
    print("\n Change Parent Password:")
    # verify old one first
    if not verify_password(config):
        return
    
    new_pw = getpass.getpass("Enter new Parent Password: ")
    confirm_pw = getpass.getpass("Confirm new Parent Password")

    if new_pw != confirm_pw:
        print("Passwords do not match. Change aborted.")
        return
    
    save_config(config['bracket'], new_pw)
    print("Password updated successfully!")

# This part is the D-Bus service wrapper
class AgeVerificationService:

    # This is the Introspection XML. It defines how the D-Bus tells other programs "I have a method called GetAgeBracket that returns a string".
    dbus = """
    <node> 
        <interface name='org.freedesktop.AgeVerify1'>
             <method name='GetAgeBracket'>
                <arg type='s' name='bracket' direction='out'/>
             </method>
        </interface>
    </node> 
    """
    # Take the value of age_val and hold onto it so it doesn't vanish after get_age_bracket() finishes.
    def __init__(self, age_val):
        self.age_val = age_val

    def GetAgeBracket(self):
        # When another app or service calls this, the script returns the string stored in self.age_val
        print(f"Service: Sending age bracket '{self.age_val}' to caller.")
        return self.age_val

if __name__ == "__main__":
    # Check if we should run setup or start the service
    # If the file doesn't exist, run setup
    if not os.path.exists(CONFIG_FILE):
       print("Initial Setup: Create Parent Password\n")
       print("Be sure to write it down and save it in a safe place!\n")
       new_pw = getpass.getpass("Set a new Parent Password: ")
       # save a dummy config first to establish the password
       save_config("Unknown", new_pw)
       print("Password set. Choose your age bracket.")
       get_bracket()
       exit(0)
       # The reason we do it like that is to prevent conflictions with the D-Bus if we ever change the info.
    
    # load config
    config = load_config()
    current_bracket = config['bracket']

    # Global authentication; it keeps people from messing with settings without the password
    if not verify_password(config):
        exit(1)

    # actions menu
    print(f"\n--- Age Control Management ---")
    print(f"Current Status: {current_bracket}")
    print("1. Start D-Bus Service")
    print("2. Change Age Bracket")
    print("3. Change Parent Password")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "2":
        # verify the password again for double security
        get_bracket()
        print("Settings updated. Please restart to run service.")
        exit(0)
        pass

    elif choice == "3":
        change_password()

    elif choice == "1":
        # Start D-Bus service
        try: 
            bus = SessionBus()
            
            bus.publish("org.freedesktop.AgeVerify", ("/org/freedesktop/AgeVerify", AgeVerificationService(current_bracket)))
            print(f"Service active with bracket: {current_bracket}")
            print("Press Ctrl+C to stop.")

            # Looping logic
            loop = GLib.MainLoop()
            loop.run()
        except RuntimeError:
            print("Error: Service is already running elsewhere.")
        except KeyboardInterrupt:
            print("\nStopping service.")
    
    else:
        print("Exiting.")
