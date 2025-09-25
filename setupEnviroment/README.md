# Configure Vulnerable Enviroment and Detection

## Install SSH server on our VMs
```
sudo apt update
sudo apt install openssh-server -y
sudo systemctl start ssh
sudo systemctl enable ssh
sudo ufw allow 22
sudo ufw enable
```

Verify SSH is running. Go to ```sshd_config``` to uncomment the line ``` PasswordAuthentication yes ```. At the same time, navigate to the #PermitRootLogin block. Uncomment and delete ``` prohibit-password``` statement, 
change to ```yes```

``` sudo systemctl status ssh ```

## Enable WinRM on project-x-win-client
- Run Window Powershell with Administration
- Type the following command

```
powershell -ep bypass
Enable-PSRemoting -force
winrm quickconfig -transport:https
Set-Item wsman:\localhost\client\trustedhosts *
net localgroup "Remote Management Users" /add administrator
Restart-Service WinRM
```

## Enable RDP on project-x-dc
- Go to “Settings” ➔ “System” ➔ “Remote Desktop”.
- Toggle Remote Desktop to “On”

## Setup Detections and Alerts
- Go to Explore ➝ Alerting.
- On the Monitors tab, click Create monitor.
- Name the monitor: 3 Failed SSH Attempts.
- Add a query based on the information from the logs (e.g., search for the Failed password event in SSH logs).
<img width="973" height="335" alt="image" src="https://github.com/user-attachments/assets/ce43c656-0607-4868-8c7b-8fa8fb8814e6" />

- Create a trigger that alerts when more than 3 failed SSH login attempts are detected within the specified time frame.
<img width="1113" height="359" alt="image" src="https://github.com/user-attachments/assets/434bec79-aa36-48ba-ac92-f94501f81cee" />

- Click "Create" to finish.

