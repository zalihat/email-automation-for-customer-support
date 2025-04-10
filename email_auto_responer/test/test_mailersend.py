from mailersend import emails

mailer = emails.NewEmail("mlsn.02be60bc5865ab0759cafc10f2bc8a5f3bd095d7f32199e7930c5911eb71afca")

# define an empty dict to populate with mail values
mail_body = {}

mail_from = {
    "name": "zalihat",
    "email": "zalihatmohammad25@gmail.com",
}

recipients = [
    {
        "name": "Zalihat Mohammed",
        "email": "zalihatmohammed@gmail.com",
    }
]

reply_to = {
    "name": "Zalihat",
    "email": "zalihatmohammad25@gmail.com",
}

mailer.set_mail_from(mail_from, mail_body)
mailer.set_mail_to(recipients, mail_body)
mailer.set_subject("Hello!", mail_body)
mailer.set_html_content("This is the HTML content", mail_body)
mailer.set_plaintext_content("This is the text content", mail_body)
mailer.set_reply_to(reply_to, mail_body)

# using print() will also return status code and data
response = mailer.send(mail_body)
print(response)