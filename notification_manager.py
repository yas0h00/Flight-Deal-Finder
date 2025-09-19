import smtplib
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
class NotificationManager:
    def __init__(self):
        self.client = Client(os.getenv('ACOUNT_SID'), os.getenv('AUTH_TOKEN'))

    # def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.
        Parameters:
        message_body (str): The text content of the SMS message to be sent.
        Returns:
        None
        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        # message = self.client.messages.create(
        #     from_=os.getenv('TWILLIO_PHONE_NO'),
        #     body=message_body,
        #     to=os.getenv('MY_NO')
        # )
        # # Prints if successfully sent.
        # print(message.sid)
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.getenv("TWILLIO_PHONE_NO")}',
            body=message_body,
            to=f'whatsapp:{os.getenv('MY_NO')}'
        )
        print(message.sid)
    # def send_email(self, message_body):
    #     with smtplib.SMTP("smtp.gmail.com") as connection:
    #         connection.starttls()
    #         connection.login(user=os.getenv('MY_EMAIL'), password=os.getenv('EMAIL_PASS'))
    #         connection.sendmail(
    #             from_addr=os.getenv('MY_EMAIL'),
    #             to_addrs=os.getenv('USER_EMAIL'),
    #             msg=message_body
    #         )
