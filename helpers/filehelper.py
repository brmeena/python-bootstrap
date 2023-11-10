import sys
import os
import traceback

sys.path.append("../")
import requests
import asyncio
import aiohttp
import aiofiles
def downloadFile(fileUrl,filePath):
    r=requests.get(fileUrl)
    with open(filePath,"wb") as f:
        f.write(r.content)
    return filePath


async def downloadFileAsync(fileUrl,filePath):
    async with aiohttp.ClientSession() as session:
        async with session.get(fileUrl) as resp:
            if resp.status == 200:
                f = await aiofiles.open(filePath, mode='wb')
                await f.write(await resp.read())
                await f.close()
    return filePath

def getFileExtension(filePath):
    split_tup = os.path.splitext(filePath)
    return split_tup[1]

