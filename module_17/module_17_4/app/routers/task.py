from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def all_tasks():
    return {"message": "Get all tasks"}


@router.get('/{task_id}')
async def task_by_id(task_id: int):
    return {"message": f"Get task with id {task_id}"}


@router.post('/create')
async def create_task():
    return {"message": "Create a new task"}


@router.put('/update')
async def update_task():
    return {"message": "Update a task"}


@router.delete('/delete')
async def delete_task():
    return {"message": "Delete a task"}
