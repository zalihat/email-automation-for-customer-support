from src.prompt_generator import generate_email_content
from src.email_handler import send_email
from src.utils import log_error, log_info
import logging
# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    filename='logs/app.log',  # Optional: log to a file (remove to log to console)
    filemode='a'  # 'a' = append, 'w' = overwrite file each time
)


def automate_email_response(customer_name, customer_email, customer_query, sender_email, company_name):
    """Automate the email response workflow."""
    logging.info(f"Received inquiry from {customer_name}: {customer_query}")

    # Generate AI response using Gemini API
    try:
        email = generate_email_content(customer_name, customer_query)
        logging.info(f"Generated email content: {email}")
    except Exception as e:
        logging.error(f"Error generating email content: {str(e)}")
        return

    # Send email using SendGrid
    subject = email[0].email_subject
    email_body = email[0].email_body
    # message = send_email(customer_name="Zalihat Mohammed",customer_email='zalihatmohammed@gmail.com',email_subject='hello', email_body='email body', sender_email='zalihatmohammad25@gmail.com', company_name='alphaglobal')
     
    message = send_email(customer_name, customer_email, subject, email_body, sender_email, company_name)

    if message.status_code == 202:
        log_info(f"Successfully sent email to {customer_email}")
    else:
        log_error(f"Failed to send email to {customer_email}. Status: {message.status_code}")

if __name__ == "__main__":
    # Example customer query
    customer_name = "John Doe"
    customer_email = "johndoe@example.com"
    customer_query = "Can I get an update on my order status?"
    sender_email='zalihatmohammad25@gmail.com'
    company_name='RayyanAssociates'


    # Automate the email process
    automate_email_response(customer_name, customer_email, customer_query, sender_email,company_name )
