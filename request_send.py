import httpx
import asyncio
import time

URL="http://localhost:8080/"

async def make_request(client):
    r = await client.get(URL)
    return r.text

async def main():
    start = time.time()
    timeout = httpx.Timeout(30.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks = [make_request(client) for _ in range(2)]
        results = await asyncio.gather(*tasks)
    
    print(f"total time {round(time.time()-start,2)} seconds")


asyncio.run(main())