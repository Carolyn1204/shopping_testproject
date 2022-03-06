import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config.global_parameters as gp
from util import logger


report_path = gp.report_path


class s_email:
    def __init__(self):
        self.mylog = logger.LogUtil()

    def __get_report(self):
        # get the latest report
        dirs = os.listdir(report_path)
        dirs.sort()
        new_report = dirs[-1]
        # print(new_report)
        return new_report

    def __init_email(self):
        # email content and the attachment
        new_report = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = 'Test Report Subject'
        self.msg['date'] = '56-23-32'
        # time.strftime('%a, %d %b %Y %H:%M:%S')

        with open(os.path.join(report_path, new_report), 'rb') as f:
            mail_body = str(f.read())
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        self.msg.attach(html)


        # html attachment
        att1 = MIMEText(mail_body, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport123.html"'
        self.msg.attach(att1)

    def send_report(self):
        self.__init_email()
        self.msg['from'] = gp.sender_address
        self.msg['To'] = gp.receiver_address
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtp.login(gp.sender_address, gp.sender_password)
            smtp.sendmail(self.msg['from'], self.msg['To'], self.msg.as_string())
            smtp.close()
            self.mylog.info('send successfully')
        except Exception:
            self.mylog.error('fail to send')



if __name__ == '__main__':
    sm = s_email()
    sm.send_report()
