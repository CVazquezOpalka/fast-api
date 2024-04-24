from motor.motor_asyncio import AsyncIOMotorClient
from models import Notification, CreateNotification


client = AsyncIOMotorClient(
    "mongodb+srv://cristianvazquezdev:cristian4515@cluster0.9bwagba.mongodb.net/"
)

database = client.notificationdb

collection = database.notification


async def get_notificaions():
    notify = []
    cursor = collection.find()
    async for document in cursor:
        notify.append(Notification(**document))
    return notify


async def create_notificaions(notificacion: Notification):
    new_notification = await collection.insert_one(notificacion)
    created_notification = await collection.find_one(
        {"_id": new_notification.inserted_id}
    )
    return created_notification



async def delete_notifications(custom_id: str):
    # Utiliza el campo "id" en el filtro de eliminación
    result = await collection.delete_one({"id": custom_id})
    # Verifica si se eliminó algún documento
    if result.deleted_count == 1:
        return True
    else:
        return False
