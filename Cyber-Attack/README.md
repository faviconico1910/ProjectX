# Cyber Attack - Initial Access to Breached
---
## Setup Attacker machine
- Name our machine ``` project-x-attacker ```.
- Set IP address to ``` 10.0.0.5 ```.

## The Concept of Reconnaissance
- Also referred to as 'recon'. This is first phase of a cyber-attack where attackers gather information about their target to identify vulnerabilities they can exploit. This phase is all about preparation and involves collecting as much data as possible about the target's systems, network, employees, or infrastructure without triggering alarms.

# Scanning
- Nmap (Network Mapper) is a powerful open-source tool for network discovery and security auditing. It finds hosts, open ports, running services and versions, OS guesses, and can run scripts to automate checks.
- To discover which services are running and identify their versions on the target, we can execute nmap -sV -p1-1000 10.0.0.8, which will probe TCP ports 1 through 1000 on 10.0.0.8 and perform service/version detection

# Brute-force attack
- Hydra: Password-cracking tool used for brute-force attacks on various network services. It automates the process of attempting multiple username and password combinations to gain unauthorized access to systems. We can initiate a brute force and use a wordlists file, such as rockyou.txt to see if there are any matches.
``` hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.0.0.8 ```
