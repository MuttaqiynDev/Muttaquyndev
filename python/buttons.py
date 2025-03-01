from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# 📌 **"Viloyatingizni tanlang" tugmasi (inline)**
def choose_region_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📍 Viloyatingizni tanlang", callback_data="choose_region")]
        ]
    )

# 📌 **Viloyatlar ro‘yxati (inline)**
def region_buttons():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Toshkent", callback_data="region_Toshkent")],
            [InlineKeyboardButton(text="Andijon", callback_data="region_Andijon")],
            [InlineKeyboardButton(text="Buxoro", callback_data="region_Buxoro")],
            [InlineKeyboardButton(text="Samarqand", callback_data="region_Samarqand")],
            [InlineKeyboardButton(text="Namangan", callback_data="region_Namangan")],
            [InlineKeyboardButton(text="Navoiy", callback_data="region_Navoiy")],
            [InlineKeyboardButton(text="Jizzax", callback_data="region_Jizzax")],
            [InlineKeyboardButton(text="Xorazm", callback_data="region_Xorazm")],
            [InlineKeyboardButton(text="Nukus", callback_data="region_Nukus")],
            [InlineKeyboardButton(text="Qarshi", callback_data="region_Qarshi")],
            [InlineKeyboardButton(text="Qoqon", callback_data="region_Qoqon")],
            [InlineKeyboardButton(text="Xiva", callback_data="region_Xiva")],
            [InlineKeyboardButton(text="Margilon", callback_data="region_Margilon")]
        ]
    )

# 📌 **Asosiy menyu (reply keyboard)**
def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📅 Bugungi vaqt"), KeyboardButton(text="📅 Ertangi vaqt")],
            [KeyboardButton(text="🤲 Duo")]
        ],
        resize_keyboard=True  # ✅ Tugmalar ekranga moslashadi
    )
