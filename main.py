from app.prompt_generator import generate_email_content
from app.email_handler import send_email
from app.utils import log_error, log_info

def automate_email_response(customer_name, customer_email, customer_query):
    """Automate the email response workflow."""
    log_info(f"Received inquiry from {customer_name}: {customer_query}")

    # Generate AI response using Gemini API
    try:
        email_body = generate_email_content(customer_name, customer_query)
    except Exception as e:
        log_error(f"Error generating email content: {str(e)}")
        return

    # Send email using SendGrid
    subject = f"Response to Your Inquiry, {customer_name}"
    status_code, response_body = send_email(customer_email, subject, email_body)

    if status_code == 202:
        log_info(f"Successfully sent email to {customer_email}")
    else:
        log_error(f"Failed to send email to {customer_email}. Status: {status_code}")

if __name__ == "__main__":
    # Example customer query
    customer_name = "John Doe"
    customer_email = "johndoe@example.com"
    customer_query = "Can I get an update on my order status?"

    # Automate the email process
    automate_email_response(customer_name, customer_email, customer_query)
