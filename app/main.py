# main.py
import uvicorn
from fastapi import FastAPI
from app.adapters.api.user_controller import router as user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Register API routers
app.include_router(user_router)

# Define a list of allowed origins
origins = [
    "http://localhost",
    "http://localhost:8001",  # If you're using React or another frontend on a different port
]

# Add CORS middleware to FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only the specified origins
    allow_credentials=True,  # Allow cookies to be sent cross-origin
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers (e.g., Authorization, Content-Type)
)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, workers=1)