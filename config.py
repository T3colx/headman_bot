from enum import Enum

token = '1192994778:AAG7QhnCmFoWLP-RDbW_y3_JLpnamo_Txn4'

g_drive = "https://drive.google.com/drive/folders/174z7BNpxIqgA8_I3UhevyjnZCIv8ezLZ?usp=sharing"

g_calendar = "https://calendar.google.com/calendar/u/0?cid=MjZvamk1dmthbmdjcmVxYThwc3JnZmpwc2tAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ"

db_file = "database.vdb"


class States(Enum):
    S_START = "Start"  # Начало нового диалога
    S_MAIN_MENU = "Main_Menu"
    S_PROFESSORS = "Main_Menu_Professors"
    S_PROFESSORS_PHYSICS = "Main_Menu-->Professors-->Physics"
    S_PROFESSORS_PROGRAMMING = "Main_Menu-->Professors-->Programming"
    S_USEFUL_LINKS = "Main_Menu-->Useful_links"
    S_USEFUL_LINKS_COURSES = "Main_Menu-->Useful_links-->Courses"
    S_USEFUL_LINKS_FRESH_NEWS = "Main_Menu-->Useful_links-->Fresh_News"
