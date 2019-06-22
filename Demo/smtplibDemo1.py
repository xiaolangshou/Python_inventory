import smtplib

client = smtplib.SMTP()
client.connect('smtp.163.com',25)
client.login('xiaolangshou','0306113006btx###')

msg = '''From:xiaolangshou@163.com
To:xiaolangshou@163.com
Subject: this is mail title 

this is mail context
'''

client.sendmail('xiaolangshou@163.com', 'xiaolangshou@163.com', msg)
client.quit()

