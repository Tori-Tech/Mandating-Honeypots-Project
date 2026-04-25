# Mandating-Honeypots-Project

This is the Mandating Honeypots Project, a repository which contains audits of digital identity verification systems, whitepapers, position papers, and POCs that simultaneously identify vulnerabilities and offer decentralized, privacy-preserving solutions.

Currently, there are three phases to this project:

### Phase 1 (Current)
* **Objective:** Analyze the systemic risks of centralized Digital ID systems.
* **Deliverables:**
    * **Position Paper:** ["Mandating Honeypots: How Digital ID Verification Poses More Threats Than It Prevents, And How ZKPs Can Offer A Solution."](papers/Phase1/README.md)
    * **Scope:** An analysis of recent age-verification mandating laws such as the Parents Decide Act and the California Digital Assurance Act, explaining the inherent risks and offering a solution found in Schnorr-based ZKPs.
    * **Alternative:** Proposing Zero-Knowledge Proofs (ZKPs) as a privacy-preserving "last resort" for verification, should it become required by law.

---

### Phase 2 (TBD)
* **Objective:** Demonstrate the inherent insecurity of client-side age verification through system-level spoofing.
* **Deliverables:**
    * **Python PoC:** A script that intercepts `dbus` messages to return a persistent `18+` response.
    * **Purpose:** To demonstrate that localized verification can be easily bypassed or manipulated by the end-user.
---

### Phase 3 (TBD)
* **Objective:** Transform the identified vulnerability into a privacy-focused parental control tool.
* **Deliverables:**
    * **"Parents Decide" Utility:** A tool that password-protects the `dbus` script and/or response, allowing for local, parent-authorized verification.
    * **Goal:** To satisfy legal mandates without requiring the submission of government-issued IDs or biometric data to third-party databases.

---
### Notice:
The objectives and deliverables of to-be-decided (TBD) phases are subject to change.

### Disclaimer: 
All code included in the project is tested exclusively within a virtualized environment that exists on hardware owned by the researcher, and exists purely for educational purposes. All information used in the creation of the project was gathered from publically available sources. The researcher and all associated projects operate expressly under good faith and a genuine desire to educate. The researcher does not condone unauthorized access, modification, or general tampering with any systems without express permission.  

### Licensing
- **Code:** Licensed under the [MIT License](LICENSE).
- **Documentation & Position Papers:** Licensed under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/). 
  *© 2026 Mandating Honeypots Project Developers.*
