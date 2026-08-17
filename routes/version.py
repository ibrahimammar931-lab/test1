from fastapi import APIRouter

router = APIRouter()


@router.get("/version")
async def get_version():
    """Returns the current API version."""
    return {"version": "1.0.0"}
