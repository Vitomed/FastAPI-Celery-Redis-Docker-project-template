from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from app.routers import router

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(router=router)