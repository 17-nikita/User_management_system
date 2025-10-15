from fastapi import FastAPI
from core.connections.database import engine, Base
from services.auth.jwt.routes import router as auth_router
from services.users.routes import router as user_router
from services.users.profile.routes import router as profile_router

# # Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management Microservice with JWT")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(profile_router)

@app.get("/")
def root():
    return {"message": "Service is running!"}
