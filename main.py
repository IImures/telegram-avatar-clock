from telethon import TelegramClient
from time import sleep
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import datetime
import photos

import configparser

config_file_path = 'config.ini'

config = configparser.ConfigParser()
config.read(config_file_path)

#you need to write your api_id and api_hash to config file or simply write them into variables
api_id = config['BOT']['api_id']
api_hash = config['BOT']['api_hash']

client = TelegramClient('session1', api_id, api_hash)



async def main():
    now = datetime.datetime.now()
    while True:
        if now.second == 0:
            delete = await client(DeletePhotosRequest(await client.get_profile_photos('me')))
            photos.make_avatar()
            sleep(1)
            result = await client(UploadProfilePhotoRequest(file=await client.upload_file('avatar/result.jpg')))
            now = datetime.datetime.now()
        now = datetime.datetime.now()


with client:
    client.loop.run_until_complete(main())
