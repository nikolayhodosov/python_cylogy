import time
from support.Email_Page import Email
import string, re
import imaplib
import email


mail = Email()
address = "qlik.ib.testuser@gmail.com"
password = "VV3BxS-_9+5kaX"


class Gmail:
    def signin(self, context):
        mail.getgmail(context)
        time.sleep(6)
        mail.enteremailaddress(context, address)
        time.sleep(4)
        mail.enterpassword(context, password)
        try:
            time.sleep(2)
            if mail.protect_email_page(context).is_displayed():
                mail.protect_email_ready(context)
        except:
            success = True
        #time.sleep(3)

    def pass_from_email(self):
        #time.sleep(3)
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('qlik.ib.testuser@gmail.com', 'VV3BxS-_9+5kaX')
        mail.list()

        # Out: list of "folders" aka labels in gmail.
        mail.select("inbox")  # connect to inbox.

        result, data = mail.uid('search', None, "ALL")  # search and return uids instead
        latest_email_uid = data[0].split()[-1]  # get the latest
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')

        email_message = email.message_from_string(raw_email_string)

        # print (email_message['To'])
        # print (email.utils.parseaddr(email_message['From']))
        # print (email_message['Subject'])
        def find_between(s, first, last):
            try:
                start = s.index(first) + len(first)
                end = s.index(last, start)
                return s[start:end]
            except ValueError:
                return ""

        messageMainType = email_message.get_content_maintype()

        if messageMainType == 'text':
            mess = email_message.get_payload()
            mess1 = re.sub('<[^<]+?>', '', mess)
            mess2 = re.sub('=20', '', mess1)
            mess3 = find_between(mess2, "chat window.", "\"Embrace").strip()
            if (mess3 == ""):
                mess3 = find_between(mess2, "address.  &nbsp;", "&nbs=")
            # print(mess3)
            return mess3
