from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def all_users():
    return {"message": "Get all users"}


@router.get('/{user_id}')
async def user_by_id(user_id: int):
    return {"message": f"Get user with id {user_id}"}


@router.post('/create')
async def create_user():
    return {"message": "Create a new user"}


@router.put('/update')
async def update_user():
    return {"message": "Update a user"}


@router.delete('/delete')
async def delete_user():
    return {"message": "Delete a user"}
