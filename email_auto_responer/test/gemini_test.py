from google import genai
from google.genai import types
from config import config
from pydantic import BaseModel

class EmailResponse(BaseModel):
    customer_name: str
    customer_query: str
    email_body: str
    status_code: int
    response_body: str
    error_message: str
    email_subject: str

GEMINI_API_KEY = config.GEMINI_API_KEY
client = genai.Client(api_key=GEMINI_API_KEY)
customer_name = "John Doe"
customer_query = "Can I get an update on my order status?"


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
# print(response.text)
# if response.text[0]['status_code'] == 200:
#     print('its all good')
# print(response.text[0]['email_body'])
emails: list[EmailResponse] = response.parsed
# print(emails[0].email_body)
if emails[0].status_code == 200:
    print('its all good')
else:
    print('its not good')
    print(emails[0].error_message)
