import os
import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox1f83825c58e64b0796450aba9725ac63.mailgun.org/messages",
  		auth=("api", os.getenv('API_KEY', 'api_key')),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox1f83825c58e64b0796450aba9725ac63.mailgun.org>",
			"to": "zalihat Mohammed <zalihat.mohammed@st.futminna.edu.ng>",
  			"subject": "Hello zalihat Mohammed",
  			"text": "Congratulations zalihat Mohammed, you just sent an email with Mailgun! You are truly awesome!"})
message = send_simple_message()
print(message.status_code)
print(message.text)
