from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
from config import config
import logging

# Set up logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

# SendGrid client
sg = SendGridAPIClient(config.SENDGRID_API_KEY)

def send_email(customer_email, subject, email_body):
    """Send email to customer using SendGrid."""
    from_email = Email("support@yourcompany.com")
    to_email = To(customer_email)
    content = Content("text/plain", email_body)
    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.send(mail)
        logging.info(f"Email sent to {customer_email} with status code: {response.status_code}")
        return response.status_code, response.body
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")
        return str(e), None
