import time
import smtplib
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def test():
    print("@this is test file",  time.strftime('%Y-%m-%d %H:%M:%S'))


def send_mail():
    """
        :param receivers: 接受邮箱列表 mail box list receiver
        :param subject:发送邮件主题 mail topic sender
        :param text:发送邮件正文 mail message
        :param filename:发送邮件附件 mail attachment
        :param smtp_server:smtp服务器地址 smtp server address
        :param smtp_port:smtp TLS/STARTTLS port
        :param sender:发送者 sender
        :param account_info:发送者邮箱账号密码 mail sender's account password
        :return:
    """
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SENDER = 'cuitimage47@gmail.com'
    # get password from https://blog.csdn.net/qq_40229790/article/details/128160396
    ACCOUNT_INFO = {'username': 'cuitimage47@gmail.com',
                    'password': 'bekdydmhywevbmyf'}

    # 正文
    msg_root = MIMEMultipart()    # Create an instance with an attachment
    msg_root['SUBJECT'] = "Rent Payment"
    msg_root['To'] = COMMASPACE.join(['xl090@uowmail.edu.au'])
    msg_text = MIMEText(
        "Bangalay contract is over on 2023.01.29. thank you!!!", 'html', 'utf-8')
    msg_root.attach(msg_text)
    # # attachment
    # att = MIMEApplication(open(filename,'rb').read())
    # att.add_header('Content-Disposition', 'attachment', filename=filename)
    # msg_root.attach(att)
    # # 增加socks5代理 add socks5 proxy
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'x.x.x.x', 29900, True)
    # socks.wrapmodule(smtplib)

    smtp = smtplib.SMTP(f'{SMTP_SERVER}:{SMTP_PORT}')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ACCOUNT_INFO['username'], ACCOUNT_INFO['password'])
    smtp.sendmail(SENDER, ['xl090@uowmail.edu.au'], msg_root.as_string())
    smtp.close()
    print("@this is test file",  time.strftime('%Y-%m-%d %H:%M:%S'))

