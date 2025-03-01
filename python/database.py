import sqlite3
from aiogram.filters import Command
import config

# ✅ MA'LUMOTLAR BAZASINI YARATISH
def create_tables():
    conn = sqlite3.connect("ramazon.db")  # Ma'lumotlar bazasiga ulanish
    cursor = conn.cursor()
    
    # prayer_times jadvalini yaratish
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prayer_times (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region TEXT NOT NULL,
            sana TEXT NOT NULL,
            saharlik TEXT NOT NULL,
            iftorlik TEXT NOT NULL
        )
    """)
    
    conn.commit()  # O'zgarishlarni saqlash
    conn.close()   # Bog‘lanishni yopish


# ✅ BUGUNGI NAMOZ VAQTLARINI OLISH
def get_today_times(region, today):
    conn = sqlite3.connect("ramazon.db")  # Ma'lumotlar bazasiga ulanish
    cursor = conn.cursor()
    
    cursor.execute("SELECT saharlik, iftorlik FROM prayer_times WHERE region = ? AND sana = ?", (region, today))
    times = cursor.fetchone()  # Faqat bitta natijani olish
    
    conn.close()  # Bog‘lanishni yopish
    return times  # (saharlik, iftorlik) tuple qaytaradi


# ✅ ERTANGI NAMOZ VAQTLARINI OLISH
def get_tomorrow_times(region, tomorrow):
    conn = sqlite3.connect("ramazon.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT saharlik, iftorlik FROM prayer_times WHERE region = ? AND sana = ?", (region, tomorrow))
    times = cursor.fetchone()
    
    conn.close()
    return times


# ✅ PRAYER_TIMES JADVALIDAGI BARCHA MA'LUMOTLARNI KO‘RISH
def get_all_times():
    conn = sqlite3.connect("ramazon.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM prayer_times")
    data = cursor.fetchall()  # Hamma malumotlarni olish
    
    conn.close()
    return data  # [(id, region, sana, saharlik, iftorlik), (...), (...)]


# ✅ YANGI MA'LUMOT QO‘SHISH
def insert_time(region, sana, saharlik, iftorlik):
    conn = sqlite3.connect("ramazon.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO prayer_times (region, sana, saharlik, iftorlik) VALUES (?, ?, ?, ?)",
                   (region, sana, saharlik, iftorlik))
    
    conn.commit()
    conn.close()


# ✅ DATABASENI YARATISH FUNKSIYASINI CHAQRASH
if __name__ == "__main__":
    create_tables()
    print("✅ Database va jadval yaratildi!")

