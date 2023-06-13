from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/all")
async def read_users():
    return [{
        "username": "Rick"
    }]
