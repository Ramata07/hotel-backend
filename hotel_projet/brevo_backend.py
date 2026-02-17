from django.core.mail.backends.base import BaseEmailBackend
from sib_api_v3_sdk import Configuration, ApiClient, TransactionalEmailsApi, SendSmtpEmail
import os
import logging

logger = logging.getLogger(__name__)

class BrevoAPIBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        api_key = os.environ.get('BREVO_API_KEY')
        if not api_key:
            logger.error("BREVO_API_KEY not set!")
        
        configuration = Configuration()
        configuration.api_key['api-key'] = api_key
        self.api_client = ApiClient(configuration)
        self.api_instance = TransactionalEmailsApi(self.api_client)

    def send_messages(self, email_messages):
        if not email_messages:
            return 0
        
        msg_count = 0
        for message in email_messages:
            try:
                to_list = [{"email": email} for email in message.to]
                
                send_smtp_email = SendSmtpEmail(
                    to=to_list,
                    sender={"email": message.from_email},
                    subject=message.subject,
                    html_content=message.body,
                )
                
                response = self.api_instance.send_transac_email(send_smtp_email)
                logger.info(f"Email sent: {response}")
                msg_count += 1
                
            except Exception as e:
                logger.error(f"Failed to send email: {str(e)}")
                if not self.fail_silently:
                    raise
        
        return msg_count