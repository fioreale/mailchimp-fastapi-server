from pydantic_settings import BaseSettings

class MailChimpSettings(BaseSettings):
    mailchimp_api_key: str
    mailchimp_data_center: str
    mailchimp_list_id: str

    class Config:
        env_file = ".env"
