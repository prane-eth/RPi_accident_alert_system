from smtplib import SMTP

session = SMTP('smtp.gmail.com', 587)        
session.ehlo()
session.starttls()
session.ehlo()

email='annaloki2000@gmail.com'
session.login(email, '123@loki')

headers = [
            "From: " + email,
            "Subject: Accident",
            "To: " + email,
            "MIME-Version: 1.0",
           "Content-Type: text/html"
          ]
headers = "\r\n".join(headers)

def send(txt):
    session.sendmail(
            email,
            email,
            headers + "\r\n\r\n" + txt
    )

send("Accident")

# curl --url 'smtps://smtp.gmail.com:465' --ssl-reqd \
#  --mail-from 'annaloki2000@gmail.com' \
#  --mail-rcpt 'annaloki2000@gmail.com' \
#  --user 'annaloki2000@gmail.com:123@loki' \
#  -T <(echo -e 'From: annaloki2000@gmail.com\nTo: annaloki2000@gmail.com\nSubject: Curl Test\n\nHello')
