import asyncio , aiosqlite


async def fetch_user(db="" , query = "" , param =()):
    
    async with aiosqlite.connect(db) as conn:
        async with conn.execute(query , param) as cursor:
           row = await cursor.fetchall()
           
           return row
       
       

async def fetch_older_user(db = "" , query ="" , params = ()):
   
    async with (aiosqlite.connect(db)) as conn:
        async with conn.execute(query , params) as cursor:
            row = await cursor.fetchall()
            
            return row
       
       
       
       

async def fetch_concurrently():
   r = await asyncio.gather(fetch_user(
       "testdb.sqlite3" , 
       "SELECT * FROM Users ;"
   ),
    fetch_older_user("testdb.sqlite3" , "SELECT * FROM Users WHERE age > ?;" , (40,)))
   print(r)
   
   
asyncio.run(fetch_concurrently())