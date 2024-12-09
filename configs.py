from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22768311"))
    API_HASH = getenv("API_HASH", "702d8884f48b42e865425391432b3794")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "SDBotz")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
