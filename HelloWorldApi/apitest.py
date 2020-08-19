# Install the aiohttp and asyncio modules and change the count and URL before running this: python apitest.py
import aiohttp
import asyncio

count = 10000
url = 'http://10.1.1.4:32139/hello'

async_list = []
ok = 0
failed = 0

async def fetch(session):
    async with session.get(url) as response:
        content = await response.text()
        print(f'Status: {response.status} - Content:{content}')

async def fetch_all():
  async with aiohttp.ClientSession() as session:
    tasks = []
    for x in range(0, count):
        tasks.append(
            fetch(session)
        )
    await asyncio.gather(*tasks, return_exceptions=True)

print(f'Running {count} requests')
asyncio.run(fetch_all())
print(f'Done')




