from django.core.mail.backends.base import BaseEmailBackend
from resend import Resend
import os
import logging

logger = logging.getLogger(__name__)

class ResendBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        api_key = os.environ.get('RESEND_API_KEY')
        if not api_key:
            logger.error("RESEND_API_KEY not set!")
        self.client = Resend(api_key=api_key)

    def send_messages(self, email_messages):
        if not email_messages:
            return 0
        
        msg_count = 0
        for message in email_messages:
            try:
                # Resend attend 'to' comme liste
                to_list = message.to if isinstance(message.to, list) else [message.to]
                from_email = message.from_email
                
                logger.info(f"Sending email from {from_email} to {to_list}")
                
                response = self.client.emails.send({
                    "from": from_email,
                    "to": to_list,
                    "subject": message.subject,
                    "html": message.body,
                })
                
                logger.info(f"Email sent successfully: {response}")
                msg_count += 1
                
            except Exception as e:
                logger.error(f"Failed to send email: {str(e)}", exc_info=True)
                if not self.fail_silently:
                    raise
        
        return msg_count