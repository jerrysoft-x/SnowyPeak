from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# email address and password
from_addr = 'jerryleevip@163.com'
password = 'update password here'

# recipient address
to_addr1 = 'jerry.li@dnvgl.com'
to_addr2 = 'Jian.Tao.Bruce.Fan@dnvgl.com'
# SMTP server address
smtp_server = 'smtp.163.com'

# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr('Jerry Li <%s>' % from_addr)
msg['To'] = _format_addr('Jerry <%s>' % to_addr1)
msg['Subject'] = Header('来自Python的问候...', 'utf-8').encode()

# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello, Lily</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

with open(r'C:\Users\JJLI\Documents\GitHub\SnowyPeak\Email\test.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpeg', filename='test.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr1], msg.as_string())
server.quit()
