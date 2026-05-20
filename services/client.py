from fastapi import HTTPException, status
from sqlalchemy import func, select
from database import database 
from models.client import clients
from schemas.client import ClientIn, ClientUpdateIn


class ClientServices:
    async def create(self, client:ClientIn):
        query = clients.insert().values(
            name=client.name,
            last_name=client.last_name,
            cpf=client.cpf,
            email=client.email,
            birth_date=client.birth_date,
            phone_number=client.phone_number
        )
        new_id = await database.execute(query)
        return await self.get_by_id(new_id)
    
    async def read_all(self, limit: int = 20, skip: int = 0):
        query = clients.select().limit(limit).offset(skip)
        return await database.fetch_all(query)
    
    async def read_id(self, client_id: int):
        return await self.get_by_id(client_id)
    
    async def update(self, id: int, client: ClientUpdateIn):
        result = await self.count(id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
        
        data = client.model_dump(exclude_unset=True)
        query = clients.update().where(clients.c.id==id).values(**data)
        await database.execute(query)

        return await self.get_by_id(id)
    
    async def delete(self, id):
        query = clients.delete().where(clients.c.id==id)
        await database.execute(query)
    
    async def count(self, id) -> int:
        query = select(func.count()).select_from(clients).where(clients.c.id == id)
        result = await database.fetch_one(query)
        return result[0]
    
    async def get_by_id(self, id):
        query = clients.select().where(clients.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        return post