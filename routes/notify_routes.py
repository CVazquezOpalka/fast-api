from db import get_notificaions, delete_notifications, create_notificaions
from models.model_notify import Notification
from fastapi import HTTPException, APIRouter


notify = APIRouter()


@notify.get("/", tags=["Notificaciones"])
async def todas_notificaciones():
    response = await get_notificaions()
    return response


@notify.post("/", tags=["Notificaciones"])
async def create_notify(noti: Notification):
    response = await create_notificaions(noti.model_dump())
    if response:
        return "Notificacion agregada correctamente"
    raise HTTPException(400, "Algo Salio mal vuelve a intentar")


@notify.delete("/{id}", tags=["Notificaciones"])
async def borrar_notification(id: str):
    response = await delete_notifications(id)
    if response:
        print(response)
        return "Se actualizo el calendario de eventos"
    raise HTTPException(404, f"no hay una notificacion con el id {id}")
