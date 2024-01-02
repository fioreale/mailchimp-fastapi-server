from fastapi import APIRouter, HTTPException
from ..models import FormData
from ..services.mailchimp_services import add_to_mailchimp

router = APIRouter()

@router.post("/community/subscribe")
async def receive_data(form_data: FormData):
    response = add_to_mailchimp(form_data)
    if response.status_code in [200, 201]:
        return {"message": "Added to Mailchimp successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add to Mailchimp")
