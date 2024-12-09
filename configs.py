from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22768311"))
    API_HASH = getenv("API_HASH", "702d8884f48b42e865425391432b3794")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "Naruto_Shippunden_In_Hindi_Dub")
    CHID = int(getenv("CHID", "-1002059068082"))
    SUDO = list(map(int, getenv("6040503076").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://woyijir141:<uDHAqNrHMDe2ZxHv>@rohit098.9qldt.mongodb.net/?retryWrites=true&w=majority&appName=Rohit098")
    
cfg = Config()
