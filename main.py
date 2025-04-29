from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import auth_router
from routers.booking import booking_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], 
)
app.include_router(auth_router, tags=["auth"], prefix="/auth")
app.include_router(booking_router, tags=["booking"], prefix="/booking")

@app.get("/")
def root():
    return {"message":"server running"}
