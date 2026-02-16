from django.core.mail.backends.base import BaseEmailBackend
from resend import Resend
import os

class ResendBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.client = Resend(api_key=os.environ.get('RESEND_API_KEY'))

    def send_messages(self, email_messages):
        if not email_messages:
            return 0
        
        msg_count = 0
        for message in email_messages:
            try:
                self.client.emails.send({
                    "from": message.from_email,
                    "to": message.to,
                    "subject": message.subject,
                    "html": message.body,
                })
                msg_count += 1
            except Exception as e:
                if not self.fail_silently:
                    raise
        return msg_count