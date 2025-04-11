# 📬 Email Automation for Customer Support
A smart email responder system designed to automatically generate and send polite, professional replies to customer queries using **Gemini (LLM)** for natural language generation and **Mailgun** for email delivery.

📁 Project Structure
```
email-automation-for-customer-support/
└── email-auto-responder/
    ├── logs
    |   |--app.log
    ├── src
    |   ├── main.py
    |   ├── prompt_generator.py
    |   ├── email_handler.py
    |   |── util.py
    ├── config/
    │   ├── config_example.py
    │   └── config.py  ← (you will create this)
    └── README.md
```

🚀 What It Does

- 💬 Accepts plain or unformatted customer queries
- 🧠 Uses Google's Gemini API to generate polite, well-structured email replies
- ✉️ Sends generated replies using **Mailgun**
- ✅ Simple and clean modular Python structure


⚙️ Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/zalihat/email-automation-for-customer-support.git
cd email-automation-for-customer-support/email-auto-responder
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
### 3. Install required packages
```bash
pip install -r requirements.txt
```
### 4. Configure API keys and settings

Navigate to the `config` folder:

```bash
cd config
cp config_example.py config.py
```

Then open `config.py` and update with your actual credentials:



# config.py

GEMINI_API_KEY = "your_google_gemini_api_key"
MAILGUN_API_KEY = "your_mailgun_private_api_key"


🧪 How to Run

From the `email-auto-responder/` directory, run:

```bash
python main.py
```

This will:
- Take a plain customer query (you can define it in `main.py`)
- Generate a polite response via Gemini
- Send the email to the customer via Mailgun


✨ Example

```python
# Inside main.py

customer_name = "John Doe"
customer_email = "johndoe@example.com"
customer_query = "Can I get an update on my order status?"
sender_email='zalihatmohammad25@gmail.com'
company_name='alphaglobal'


# Automate the email process
automate_email_response(customer_name, customer_email, customer_query, sender_email,company_name )
```
Expected Output:

```
Status code: 200
Response body: Email sent to customer.
Error message: 
Email subject: Order Status Inquiry
Generated email body: Dear Mr. Doe,

Thank you for reaching out regarding your order status. We understand you're eager to receive an update.

To assist you efficiently, could you please provide your order number? This will allow us to quickly locate your order and provide you with the most accurate information.

Once we have your order number, we will promptly check its status and inform you of its current location and estimated delivery date.

Thank you for your patience and understanding.

Sincerely,
Customer Service


```


✅ Features

- Prompt engineering logic is separated for easy tuning
- Full email sending via Mailgun with fallback logging
- Clean project structure for scalability


📦 To-Do / Future Ideas

- Add a Flask or Streamlit UI for non-developers
- Response templates for specific use-cases (returns, complaints, inquiries)
- Log sent emails and track analytics


🛡️ License
MIT License
🙌 Credits

- Google Gemini API (for LLM responses)
- Mailgun (for email delivery)
- Prompt engineering inspiration from OpenAI/Gemini docs


> 🔧 Need help? Create an issue or contact the maintainer.
