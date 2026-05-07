## Overview:
California’s Age Assurance Act and the Parents Decide Act mandate age verification at the operating system level but lack a technical roadmap. This final phase of the Mandating Honeypots project addresses the inherent insecurities within current Linux proposals and hardens the system by transforming the vulnerability into a parental control tool.

## The Issue:
Linux developers have discussed using the D-Bus interface to broadcast age bracket information, which is insecure because any individual can spoof requests by running a Python script that claims ownership of a specified D-Bus and always outputs an 18+ age bracket, effectively bypassing the age verification system. [Phase 2](./Phase2/README.md) of the Mandating Honeypots project discussed this in more detail.

Instead of abandoning the D-Bus method for more invasive procedures, we transform this vulnerability by wrapping the “spoofing” script within layers of authentication, ensuring minors cannot manipulate the script, thus shifting access management from the government back to the parent.

## Adaptability:
If this script was to be turned into enterprise-level software, further access control could be implemented by changing the utility into a background process protected by root permissions, using the system D-Bus instead of the session D-Bus, and adding MFA options that require a parent to add a phone number or email address upon setup. The application would then send a code before saving any changed settings, ensuring that no one can tamper with the service without both the password AND access to the parent’s phone.

The accompanying code serves as the strongest counterargument against digital age verification from a security standpoint, as it proves that decentralized, privacy-focused methods are possible after all.

## Installation Guide:

Ensure you have dependencies installed on your machine for D-Bus integration. Also ensure you have python3 venv installed as well. If you do not, run these commands (assuming you are using Ubuntu):

```sudo apt update```
```sudo apt install python3-venv python3-pip python3-gi libgirepository1.0-dev libcairo2-dev pkg-config```

Clone the repository and cd into it. Create a Python virtual environment and activate it.

```python3 -m venv .venv```
```source .venv/bin/activate```

Install all required Python dependencies from requirements.txt.

```pip install -r requirements.txt```

Run dbus.py with this command:

```python dbus.py```

Open a separate terminal, cd into the project folder, activate the virtual environment again, and run query.py

```python query.py```

Follow the on-screen prompts and be sure to save the password you choose, as you will need it to perform any future actions.


