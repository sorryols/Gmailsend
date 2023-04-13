import smtplib
from email.mime.text import MIMEText
import value as v
def send_email(message):
    sender = v.sender
    password = v.password
    receiver = v.receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Click me please"
        server.sendmail(sender, receiver, msg.as_string())
        return "[+] message delivered"
    except Exception as _ex:
        return f"{_ex}\n[-]Check your login or password please!"


def main():
    message = input("Enter your message: ")
    print(send_email(message))


if __name__ == "__main__":
    main()