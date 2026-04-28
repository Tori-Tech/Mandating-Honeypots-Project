## Overview:

Legislation such as the California Digital Assurance Act mandates age verification at the operating system level, even for Linux, an open-source operating system. The current developer consensus is to use the Linux D-Bus interface to communicate data between the OS and applications. This part of the Mandating Honeypots project demonstrates that OS-level age verification is fundamentally flawed because the D-Bus can be manipulated by local scripts, even if the user does not possess root privileges. A minor with basic Python knowledge can easily broadcast fraudulent information to any application querying the system. This is a simple Proof of Concept that demonstrates that idea in real time. It includes:

- ```dbus.py```: A server script that registers an age bracket on the D-Bus.
- ``` query_dbus.py```: A script that acts as a mock external service/application that queries the D-Bus to “verify” the user’s age.

This PoC also serves as a foundation for Phase 3 of the Mandating Honeypots project, which aims to develop decentralized, parent-controlled verification methods.

## Installation & Setup:

Ensure that you are on a Linux distribution (this guide assumes Ubuntu/Debian) and have the necessary system dependencies for D-Bus integration. If you do not have the necessary dependencies, run:

```
sudo apt update
sudo apt install python3-venv python3-pip python3-gi libgirepository1.0-dev libcairo2-dev pkg-config
```

### Environment setup:

Clone the repository, navigate to the folder, and initialize a virtual environment:

```
git clone https://github.com/Tori-Tech/Mandating-Honeypots-Project.git
cd Mandating-Honeypots-Project/proof-of-concepts/Phase2
```

### Setup virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Python Dependencies:

```
pip install -r requirements.txt
```

### Running the demonstration:

To see the exploit in action, you will need to open two terminal windows. In the first terminal, run the server script to broadcast a chosen age bracket to the D-Bus.

```
python dbus.py
```

In the second terminal, run the query script to simulate an application verifying your age.

```
python query_dbus.py
```

## Disclaimer:

This software is provided "as is" for demonstration purposes only. It is intended to illustrate a specific security vulnerability for the purpose of informing public policy and technical debate. The author assumes no liability for any unauthorized use or damages resulting from the use of this code.
