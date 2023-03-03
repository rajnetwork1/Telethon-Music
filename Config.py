import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6229405739:AAHu0siyn5hMzD49SKVE6DwzLTtp3fg9DVQ)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOI0Bu03g20xHNNpSwNOggKm1iI7qUQqRu-c3am5zSc8IGRPxg2-ht9RYgppXNhW8EY2TTsnAyzkK2w6eDAZyZBnLofTo2ysD-aea7_Pr-hUZ4J3AgkqYMYk_tNEamXX5abuNS-foBLL5ojgwV31iyUpS0Vyq1DkdbvZNV_fdP82l1AoUKggRe4xbQ91gR2abd5Eh2SzsP4FPujklggHBB7CIURn8tgfBpAa8eHyIr7thtErvMTipz1zm9LWQNWTv-t7SAtsF9CbBu-Eg-W13rmuTCA8TlTpIuuwWuP7A5bw7X3fYwlpnTXqwaUOFxRUb-vI5BfC0lAQ_JBNOAM5fr2YG570=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RAJ1MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
