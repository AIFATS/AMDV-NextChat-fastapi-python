from fastapi import APIRouter
from packages.USER_LOGIN.user_login_check import router as user_login_check_router

router = APIRouter()

# Include user login check router
router.include_router(user_login_check_router)
