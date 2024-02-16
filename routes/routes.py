from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from packages_routes.USER_LOGIN.user_login_routes import router as users_login_routes

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Register routers
app.include_router(users_login_routes)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)