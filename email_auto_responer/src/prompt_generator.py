import requests
from config import config
from google import genai
from google.genai import types
from pydantic import BaseModel
# Define the EmailResponse model
class EmailResponse(BaseModel):
    customer_name: str
    customer_query: str
    email_body: str
    status_code: int
    response_body: str
    error_message: str
    email_subject: str
# Constants
GEMINI_API_KEY = config.GEMINI_API_KEY
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_email_content(customer_name, customer_query):
    """Generate a polite, professional response to customer query using Gemini API."""
    prompt = f"""
    You are a customer service assistant. Respond politely and professionally to the following customer query:

    Customer Name: {customer_name}
    Query: {customer_query}

    Your response should be in the form of a formal email, no more than 200 words.
    """

   
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[prompt],
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[EmailResponse],
        "max_output_tokens": 500,
        "temperature": 0.7,
        "top_p": 1
    },
    )
    emails: list[EmailResponse] = response.parsed
    # Check the status code and handle the response
    if emails[0].status_code == 200:
        return emails
    else:
        raise Exception(f"Error generating email content: {emails[0].error_message}")

# Example usage
if __name__ == "__main__":
    customer_name = "John Doe"
    customer_query = "Can I get an update on my order status?"
    
    try:
        email = generate_email_content(customer_name, customer_query)
        print(f"Status code: {email[0].status_code}")
        print(f"Response body: {email[0].response_body}")
        print(f"Error message: {email[0].error_message}")
        print(f"Email subject: {email[0].email_subject}")
        print(f"Generated email body: {email[0].email_body}")
    except Exception as e:
        print(f"Error: {str(e)}")
