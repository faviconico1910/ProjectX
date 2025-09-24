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
