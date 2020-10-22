from typing import Any, Dict, Union

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from app.worker.celery_app import celery
from app.worker import celery_tasks
from app.schema import Item

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/new-task")
async def create_new_task(
        request: Request,
        item: Item = Depends()) -> templates.TemplateResponse:
    task_name = 'app.worker.celery_tasks.main_task'
    task = celery.send_task(
        task_name, kwargs={
            'min_value': item.min_v,
            'max_value': item.max_v})
    return templates.TemplateResponse("main.html", context={"request": request, "task": task})


@router.get("/task-status/{task_id}")
async def task_status(task_id: str) -> Union[Dict[str, Any]]:
    task = celery_tasks.main_task.AsyncResult(task_id)

    if task.state == 'SUCCESS':
        full_time = task.info.pop('full_time')
        print(full_time)

    response = {'state': task.state, **task.info}

    return response
