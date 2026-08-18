This portion of the repository houses the POCs, scripts, and any other technical documentation. Below is a list of what has been published so far:

## Phase 1: Cryptographic Alternatives (As A Last Resort)


- [age_verification_ZKP.py](Phase1/age_verification_ZKP.py) A Python implementation that demonstrates a Zero-Knowledge approach to age verification, ensuring compliance without exposing raw data.
 - [associated paper](../papers/Phase1/README.md) A position paper outlining the security threats imposed by digital ID mandates, which also discusses the usage of Zero-Knowledge Proofs if a non-invasive approach is deemed impossible.

## Phase 2: Vulnerability Demonstration (D-Bus Spoofing)

- [D-Bus PoC](Phase2/README.md) Technical documentation detailing the construction and exploitation of a script that injects false data through Linux D-Buses when queried for age information.
- [dbus.py](Phase2/dbus.py) The simulated D-Bus service that intercepts and returns data when queried.
- [query_dbus.py](Phase2/query_dbus.py) A script that queries the D-Bus and prints the response, demonstrating how client-side checks can be spoofed.


## Phase 3: Constructive Remediation ("Parents Decide" Utility)

- [Parental Control Tool PoC](Phase3/dbus.py) A hardened iteration of the D-Bus service from Phase 2, which features access control mechanisms via robust password protection to prevent unauthorized modification.
- [Query Script](Phase3/query.py) A verification script that queries the D-Bus system once again, validating the functionality of the local, user-centric parental control tool, proving a less invasive, decentralized, and secure method of age verification exists.
