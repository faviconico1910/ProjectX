### What is Active Directory?
- A service developed by Microsoft to provide authentication and authorization to users on the network
- Key components:
  + Authentication: Verify user identity using credentials
  + Authorization: Grants or denies access to network resources based on permissions
  + Centralized Management: Control over users, computers and other resources
### Core Concept
- Domain: Group object (users, devices, ...) share the same database and security policies
- Domain Controllers: Servers host Active Directory database, which is ```corp.project-x-dc.com```
- Organizational Units
- Objects
- Groups
- Trust Relationships: Trusts enable users in one domain to access resources in another domain
### Build Directory Services Server
- All configurations step is according to the video in section 1: Build a Directory Services Server on the website projectsecurity.teachable.com
- The computer name is ```demo2-project-x-dc``` and the password is ```@Deeboodah1!```
- It is all about install active directory, DHCP server, DNS server, ...
- For IP address, we set the static ip for this server to be 10.0.0.5
- For DHCP server, we apply the scope from 10.0.0.100 to 10.0.0.200 and subnet mask is /24, default gateway is 10.0.0.1
- Create some users such as John Doe
<img width="937" height="652" alt="image" src="https://github.com/user-attachments/assets/b55dbea1-e629-4464-a823-871c490da960" />

-  Then we can create a snapshot to restore back when we mess up configuration

### Setup Windows 11 Enterprise
- Installation steps are the same as *** Build Directory Services Server *** when we use Windows 11 Enterprise ISO file instead
- The computer name is ```project-x-win-client``` and the password is ```@password123!```. This password is used for all other computers.
- Change workgroup to ```project-x-win-client``` and the domain is our DC ```corp.project-x-dc.com```. The account now is ```johnd@corp.project-x-dc.com```
### Setup Ubuntu Desktop (demo-project-x-linux-client)
- The owner name is ``` Jane Doe ``` and the computer name is linux-client
### Setup CORP-SVR (dedicated server)
- Make a clone from ```demo-project-x-linux-client```
- Change IP address to ```10.0.0.8```, everything else stay the same
- Change hostname to ```corp-svr```: ```sudo hostnamectl set-hostname corp-svr```
- Add a new user ```project-x-admin``` (admin account)
- Connect with AC DC: ``` sudo net ads join -U Administrator ```
- Install Docker Engine using apt
## Setup MailHog

- What is MailHog?:
- Create docker-compose.yml in ``` /home ``` in the CORP-SVR and write down these codes:

```
version: "3"
services:
  mailhog:
    image: mailhog/mailhog
    container_name: mailhog
    ports:
      - "1025:1025"
      - "8025:8025"
```
- Build docker and we are able to see our server when search the browser
<img width="1324" height="764" alt="image" src="https://github.com/user-attachments/assets/74c3c52c-1769-4509-8c89-b0030a006cce" />

- Create Email Poller Script

## Setup Security Onion (project-x-sec-work)

**Security Onion** is an open-source Linux distribution built for **Network Security Monitoring (NSM)**, **threat hunting**, and **log management**.  
It’s not just a piece of software, but an **all-in-one cybersecurity platform**.  

###  Key Features
- **Network Security Monitoring (NSM)** → monitors all traffic, detects anomalies, attacks, and malware.
- **Threat Hunting** → SOC analysts can query logs, look for IOCs, and analyze attacks.
- **Log Management** → centralizes logs from firewalls, Windows, Linux, and endpoints.
- **Incident Response** → integrates workflows to handle incidents when they are detected.



