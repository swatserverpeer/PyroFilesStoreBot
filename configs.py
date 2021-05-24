# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

🧑🏻‍💻 **Developer:** @Bujukku_Bujukku

📺 **Support :** [Discussion Group](https://throwme.ml/discussion)

📢 **Updates Channel:** [Bujukku_Bujukku](https://throwme.ml/bujukku_bujukku)

📢 **Backup Channel:** [Backup_Backup](https://throwme.ml/bujukku_backup)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Bujukku__Bujukku

📺 **Support :** [Discussion Group](https://throwme.ml/discussion)

📢 **Updates Channel:** [Bujukku_Bujukku](https://throwme.ml/bujukku_bujukku)

📢 **Backup Channel:** [Bujukku_Backup](https://throwme.ml/bujukku_backup)

Donate Now (coming soon)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
