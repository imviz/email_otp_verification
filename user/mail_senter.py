import yagmail

# Set up your email credentials
sender_email = 'wedidsolutions@gmail.com'
sender_password = 'qwrwyvgwlfqdkgsd'

# Create a yagmail SMTP client
yag = yagmail.SMTP(sender_email, sender_password)
def send_email(recipient_email, subject, body, attachment_path=None):
    try:
        # Compose the email message
        contents = [body]
        if attachment_path:
            contents.append(attachment_path)

        # Send the email
        yag.send(recipient_email, subject, contents)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")


