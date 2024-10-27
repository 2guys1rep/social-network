from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

from apis.base import api_router

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)