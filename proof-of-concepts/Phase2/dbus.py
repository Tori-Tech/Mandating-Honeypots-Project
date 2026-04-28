from pydbus import SessionBus
from gi.repository import GLib

#This function gets the user's age from command-line input. Sure, you could lie about your age and just choose the 18+ bracket, but this is for the sake of demonstrations; we'll be implementing a fix for this that lets parents verify their children's ages while preventing the children from tampering with the utility. Just trust the process for now.
def get_age_bracket():
    print("Choose your age bracket.\n")
    print("Choose your age bracket.\n")
    print("If you are under 13, press 1. \n")
    print("If you are 13-15, press 2.\n")
    print("If you are 16-17, press 3. \n")
    print("If you are 18+, press 4\n")

    response = input()
    #Converts to int because inputs are accepted as strings.
    int_response = int(response)


    match int_response:
        case 1:
            return "Under 13"
        case 2: 
            return "13-15"
        case 3: 
            return "16-17"
        case 4:
            return "18+"
        case _:
            return "Unknown"


#This part is the D-Bus service wrapper

class AgeVerificationService:

    #This is the Introspection XML. It defines how the D-Bus tells other programs "I have a method called GetAgeBracket that returns a string".
    dbus = """
    <node> 
        <interface name='org.freedesktop.AgeVerify1'>
             <method name='GetAgeBracket'>
                <arg type='s' name='bracket' direction='out'/>
             </method>
        </interface>
    </node> 
    """
    #Basically, take the value of age_val and hold onto it so it doesn't vanish after get_age_bracket() finishes.

    def __init__(self, age_val):
        self.age_val = age_val


    def GetAgeBracket(self):
        #When another app or service calls this, the script returns the string stored in self.age_val
        
        print(f"Service: Sending age bracket '{self.age_val}' to caller.")
        return self.age_val

if __name__ == "__main__":
    age_bracket = get_age_bracket()
    print(f"The user's age bracket is: {age_bracket}")

    #start the D-Bus service with the age_bracket variable.
    bus = SessionBus()
    bus.publish("org.freedesktop.AgeVerify", AgeVerificationService(age_bracket))

    print("D-Bus Service is active. Waiting for requests...")

    #this will keep the script running
    try:
        loop = GLib.MainLoop()
        loop.run()
    except KeyboardInterrupt:
        print("\nStopping service.")
