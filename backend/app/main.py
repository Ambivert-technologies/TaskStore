from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.api.api_v1.api import router as api_router



app = FastAPI()

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins  = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"]
)

@app.get("/")
def index():
    return {"msg": "Backend Running Successfully... HI"}

app.include_router(api_router, prefix="/app/v1")
handler = Mangum(app)
    

