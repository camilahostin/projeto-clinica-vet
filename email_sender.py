import smtplib
from email.message import EmailMessage
from secrets_email import EMAIL_SECRET, EMAIL_SYSTEM

msg = EmailMessage()
msg['Subject'] = 'Assunto'
msg['From'] = '@outlook.com'
msg['To'] = '@hotmail.com'
msg.set_content('Teste')


smtp_server = 'smtp.office365.com'
smtp_port = 587

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(EMAIL_SYSTEM, EMAIL_SECRET)

        server.send_message(msg)
        print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")
