from pydbus import SessionBus

#connect to the Session Bus

bus = SessionBus()

try:
    #Look for the service created previously. The names MUST match EXACTLY what was published in the server.

    verify_service = bus.get("org.freedesktop.AgeVerify", "/org/freedesktop/AgeVerify")

    #Call the method and print the result
    result = verify_service.GetAgeBracket()
    print(f"The system reports the user is: {result}")

except Exception as e:
    print(f"Could not connect to the Age Verification service: {e}")
    print("Make sure the main script is running in another terminal!")
