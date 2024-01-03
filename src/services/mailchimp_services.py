import requests
from ..configs import MailChimpSettings
from ..models import FormData

settings = MailChimpSettings()

def add_to_mailchimp(data: FormData):
    url = f"https://{settings.mailchimp_data_center}.api.mailchimp.com/3.0/lists/{settings.mailchimp_list_id}/members"
    headers = {
        'Authorization': f'Bearer {settings.mailchimp_api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'email_address': data.email,
        'status': 'subscribed',
        'merge_fields': {
            'FNAME': data.name,
            'LNAME': data.surname,
            'PHONE': data.number or ''
        }
    }
    return requests.post(url, json=payload, headers=headers)
