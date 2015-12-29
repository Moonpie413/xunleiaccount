#! /usr/bin/env python
# -*- coding:utf8 _*_
import smtplib
import xunlei
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from_addr = 'your address'  # 发件人
password = '**********'  # 密码
# 邮件接收人列表
to_addr = []
smtp_server = 'smtp.qq.com'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf8').encode(), addr))


# 使用map将list中的地址格式化
def mailto(to_addr):
    format_addrs = map(_format_addr, to_addr)
    return format_addrs


# 传入mailto函数
def send_mail(context, mailto):
    msg = MIMEText(context, 'plain', 'utf8')
    msg['From'] = _format_addr('Maroon: %s' % from_addr)
    msg['To'] = ','.join(mailto(to_addr))
    msg['Subject'] = Header('迅雷账号', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

if __name__ == '__main__':
    account_info = xunlei.getXunLeiAccount()
    send_info = '\n'.join(account_info)
    send_mail(send_info, mailto)
