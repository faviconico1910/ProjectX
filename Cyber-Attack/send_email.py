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
<a href='http://10.0.0.50'>Verify My Account</a> # this is attacker host
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