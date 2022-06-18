import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
me = "appsendertestv1@gmail.com"

def send_mail(receiver, company, phone, identity):
  # Create message container - the correct MIME type is multipart/alternative.
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "Welcome "+company+" and thanks for joining us"
  msg['From'] = me
  msg['To'] = receiver

  # Create the body of the message (a plain-text and an HTML version).
  text = "Hi!\nHow are you?\nHere is the all your information"
 
  html = """\
  <html>
    <head></head>
    <body>
      <p>Hi!<br>
        How are you?<br>
        Here is the information.
        <br>
        <br>
        Identity number: """+identity+""" <br>
        With phone: """+phone+""" <br>
      </p>
    </body>
  </html>
  """

  # Record the MIME types of both parts - text/plain and text/html.
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(html, 'html')

  # Attach parts into message container.
  # According to RFC 2046, the last part of a multipart message, in this case
  # the HTML message, is best and preferred.
  msg.attach(part1)
  msg.attach(part2)
  # Send the message via local SMTP server.
  mail = smtplib.SMTP('smtp.gmail.com', 587)

  mail.ehlo()

  mail.starttls()

  mail.login('appsendertestv1@gmail.com', 'Ishimwe12345@123')
  mail.sendmail(me, receiver, msg.as_string())
  mail.quit()