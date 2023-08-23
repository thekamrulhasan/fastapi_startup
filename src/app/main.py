from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from database.db import Base, engine
from routers import auth

app = FastAPI()

# Set up CORS middleware
origins = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(auth.router)

# API endpoint
@app.get("/", status_code=status.HTTP_200_OK, tags=["API Check"])
def check():
    return {
        "message": "Hello World!"
    }

# Create database tables
Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    load_dotenv()
    import uvicorn
    uvicorn.run(app)
