import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

import os

from dotenv import load_dotenv

load_dotenv()


SMTP_EMAIL = os.getenv("SMTP_EMAIL")

SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


def send_lead_email(lead):

    try:

        message = MIMEMultipart()

        message["From"] = SMTP_EMAIL

        message["To"] = RECEIVER_EMAIL

        message["Subject"] = "New Lead Received"


        body = f"""

New Client Inquiry Received

Full Name: {lead.full_name}

Email: {lead.email}

Phone: {lead.phone}

Company: {lead.company}

Required Service: {lead.service_required}

Project Description:
{lead.project_description}

Budget: {lead.budget}

"""


        message.attach(
            MIMEText(body, "plain")
        )


        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD
        )

        server.sendmail(
            SMTP_EMAIL,
            RECEIVER_EMAIL,
            message.as_string()
        )

        server.quit()

        print("Lead email sent successfully")


    except Exception as e:

        print("Email Error:", e)