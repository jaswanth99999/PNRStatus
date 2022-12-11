import urllib.request as ur
import smtplib, ssl
from datetime import datetime
from email.message import EmailMessage
# 4240873565
def SEND_PNR_STATUS(pnr,sender_email,reciever_email,sender_email_password):
    url="https://www.confirmtkt.com/pnr-status/"+pnr
    with ur.urlopen(url) as f:
        resp=f.read().decode('utf-8')
        ind=resp.find('"CurrentStatus":')
        mail_string=resp[ind:ind+26]


    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    # password = "dmvzgpjrcdlezdeb"
    msg = EmailMessage()
    msg['Subject'] = 'PNR STATUS...'
    msg['From'] = sender_email 
    msg['To'] = reciever_email
    msg.set_content(mail_string)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_email_password)
        server.send_message(msg)
    print("Mail Sent...")


if __name__ == "__main__":
    print(f"Running script at {datetime.now()}")
    SEND_PNR_STATUS("4240873565","tester855269@gmail.com","cherukurijaswanth9@gmail.com","dmvzgpjrcdlezdeb")