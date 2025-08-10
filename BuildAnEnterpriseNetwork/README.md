### What is Active Directory?
- A service developed by Microsoft to provide authentication and authorization to users on the network
- Key components:
  + Authentication: Verify user identity using credentials
  + Authorization: Grants or denies access to network resources based on permissions
  + Centralized Management: Control over users, computers and other resources
### Core Concept
- Domain: Group object (users, devices, ...) share the same database and security policies
- Domain Controllers: Servers host Active Directory database
- Organizational Units
- Objects
- Groups
- Trust Relationships: Trusts enable users in one domain to access resources in another domain
### Build Directory Services Server
- All configurations step is according to the video in section 1: Build a Directory Services Server on the website projectsecurity.teachable.com
- It is all about install active directory, DHCP server, DNS server, ...
- For IP address, we set the static ip for this server to be 10.0.0.5
- For DHCP server, we apply the scope from 10.0.0.100 to 10.0.0.200 and subnet mask is /24, default gateway is 10.0.0.1
- Create some users such as John Doe
<img width="937" height="652" alt="image" src="https://github.com/user-attachments/assets/b55dbea1-e629-4464-a823-871c490da960" />
- Then we can create a snapshot to restore back when we mess up configuration

