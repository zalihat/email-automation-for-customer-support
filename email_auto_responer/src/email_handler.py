from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
from config import config
import logging
import os
import requests

# Set up logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO)
def send_email(customer_name,customer_email, email_subject, email_body, sender_email,company_name):
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox1f83825c58e64b0796450aba9725ac63.mailgun.org/messages",
  		auth=("api", config.MAILGUN_API_KEY),
  		data={"from": f"{company_name} <{sender_email}>",
			"to": f"{customer_name} <{customer_email}>",
  			"subject": email_subject,
  			"text": email_body})
message = send_email(customer_name="Zalihat Mohammed",customer_email='zalihatmohammed@gmail.com',email_subject='hello', email_body='email body', sender_email='zalihatmohammad25@gmail.com', company_name='alphaglobal')
print(message.status_code)
print(message.text)
# SendGrid client
# sg = SendGridAPIClient(config.SENDGRID_API_KEY)

# def send_email(customer_email, subject, email_body):
#     """Send email to customer using SendGrid."""
#     from_email = Email("support@yourcompany.com")
#     to_email = To(customer_email)
#     content = Content("text/plain", email_body)
#     mail = Mail(from_email, to_email, subject, content)

#     try:
#         response = sg.send(mail)
#         logging.info(f"Email sent to {customer_email} with status code: {response.status_code}")
#         return response.status_code, response.body
#     except Exception as e:
#         logging.error(f"Failed to send email: {str(e)}")
#         return str(e), None

