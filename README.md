# Mandating-Honeypots-Project

As laws like the Parents Decide Act (H.R.8250) and California's Digital Age Assurance Act (Assembly Bill 1043) move through legislative bodies, privacy, anonymity, and data security becomes laden with systemic threats and new security architecture with unexamined attack surfaces. If passed, such legislation would quite literally mandate the existence of honeypots for determined attackers by demanding sensitive information (such as a government-issued ID) from anyone who wishes to use a computer. This not only endangers the very minors these laws claim to protect, but also provides a very clear attack surface: compromise the databases that house those digital IDs, and you will have suddenly stolen a thousand new identities.

The Mandating Honeypots Project seeks to prove that invasive ID verification is not the only solution. It will do so by posting audits of digital identity verification systems, related position papers, POCs, and prototype applications that simultaneously identify vulnerabilities and offer decentralized, privacy-preserving solutions. This project, designed to demonstrate vulnerabilities within Linux D-Buses (an integral part of the California Digital Age Assurance Act) was deemed "finished" on 5/6/26. With the recent introduction of the SCREEN Act, more specialized research is likely to follow. 

There are three phases to this project:

### Phase 1
* **Objective:** Analyze the systemic risks of centralized Digital ID systems.
* **Deliverables:**
    * **Position Paper:** ["Mandating Honeypots: How Digital ID Verification Poses More Threats Than It Prevents, And How ZKPs Can Offer A Solution."](papers/Phase1/README.md)
    * **Scope:** An analysis of recent age-verification mandates such as the Parents Decide Act and the California Digital Assurance Act, explaining the inherent risks and offering a solution found in Schnorr-based ZKPs.
    * **Alternative:** Proposing Zero-Knowledge Proofs (ZKPs) as a privacy-preserving "last resort" for verification, should it become required by law.

---

### Phase 2
* **Objective:** Demonstrate the inherent insecurity of client-side age verification through system-level spoofing.
* **Deliverables:**
    * **Python PoC:** [A script](proof-of-concepts/Phase2/README.md) that intercepts `dbus` messages to return a response determined by the user's inputs, as well as a script that acts as an application querying the `dbus` to "verify" the user's age.
    * **Purpose:** To demonstrate that localized verification can be easily bypassed or manipulated by the end-user.
---

### Phase 3
* **Objective:** Transform the identified vulnerability into a privacy-focused parental control tool.
* **Deliverables:**
    * **"Parents Decide" Utility:** [A tool](proof-of-concepts/Phase3/README.md) that password-protects the `dbus` script and/or response, allowing for local, parent-authorized verification.
    * **Goal:** To satisfy legal mandates without requiring the submission of government-issued IDs or biometric data to third-party databases.

---

### Disclaimer: 
All code included in the project is tested exclusively within a virtualized environment that exists on hardware owned by the researcher, and exists purely for educational purposes. All information used in the creation of the project was gathered from publicly available sources. The researcher and all associated projects operate expressly under good faith and a genuine desire to educate. The researcher does not condone unauthorized access, modification, or general tampering with any systems without express permission.  

### Licensing
- **Code:** Licensed under the [MIT License](LICENSE).
- **Documentation & Position Papers:** Licensed under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/). 
  *© 2026 Mandating Honeypots Project Developers.*
