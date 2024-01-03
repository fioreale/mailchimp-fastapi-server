from fastapi import FastAPI
from .routes.subscription_routes import router as subscription_router
# from .deps.cors import setup_cors #Uncommment this to enable CORS

app = FastAPI()
# setup_cors(app) # Uncommment this to enable CORS
app.include_router(subscription_router)
