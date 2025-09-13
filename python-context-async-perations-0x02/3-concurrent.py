import asyncio 
import aiosqlite


async def async_fetch_users():
    
    async with aiosqlite.connect("testdb.sqlite3") as conn:
        async with conn.execute( 
       "SELECT * FROM Users ;"
   ) as cursor:
           row = await cursor.fetchall()
           
           return row
       
       

async def async_fetch_older_users():
   
    async with (aiosqlite.connect("testdb.sqlite3")) as conn:
        async with conn.execute( "SELECT * FROM Users WHERE age > ?;" , (40,)) as cursor:
            row = await cursor.fetchall()
            
            return row
       
       
       
       

async def fetch_concurrently():
   r = await asyncio.gather(async_fetch_users(),
    async_fetch_older_users())
   print(r)
   
   
asyncio.run(fetch_concurrently())