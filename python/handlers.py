from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from database import get_today_times, get_tomorrow_times
from buttons import choose_region_button, region_buttons, main_menu
import datetime

router = Router()  # Dispatcher o‘rniga Router ishlatamiz
user_regions = {}  # Userning viloyatini saqlash uchun lug‘at

# 📌 **/start komandasi**
@router.message(Command("start"))
async def start_handler(message: types.Message):
    first_name = message.from_user.first_name
    await message.answer(
        f"Assalamu alaykum, {first_name}! 🌙 Ramazon taqvimi botiga xush kelibsiz!\n\n"
        "Bu bot sizga Ramazon oyining namoz va ro‘za jadvalini taqdim etadi.\n\n"
        "📍 Iltimos, viloyatingizni tanlang:",
        reply_markup=choose_region_button()  # ✅ Faqat "Viloyatingizni tanlang" tugmasi
    )

# 📌 **Viloyat tanlash tugmasi bosilganda**
@router.callback_query(F.data == "choose_region")
async def choose_region_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "📍 Iltimos, viloyatingizni tanlang:",
        reply_markup=region_buttons()  # ✅ Faqat viloyatlar tugmasi chiqadi
    )

# 📌 **User viloyat tanlaganda**
@router.callback_query(F.data.startswith("region_"))
async def region_handler(callback: CallbackQuery):
    region = callback.data.split("_")[1]
    user_regions[callback.from_user.id] = region
    await callback.message.delete()  # ✅ Viloyat tanlash tugmalarini o‘chirib tashlaymiz
    await callback.message.answer(
        f"✅ Siz {region} viloyatini tanladingiz!\n\nQuyidagi menyudan foydalanishingiz mumkin:",
        reply_markup=main_menu()  # ✅ Viloyat tanlangandan keyingina menu tugmalar chiqadi
    )

# 📌 **Bugungi namoz vaqtlari**
@router.message(F.text == "📅 Bugungi vaqt")
async def today_handler(message: types.Message):
    user_id = message.from_user.id
    region = user_regions.get(user_id, "Toshkent")
    today = datetime.date.today().strftime("%Y-%m-%d")
    times = get_today_times(region, today)

    if times:
        await message.answer(
            f"📅 Bugungi ({today})\n\n🌅 Saharlik: {times[0]}\n🌙 Iftorlik: {times[1]}"
        )
    else:
        await message.answer("❌ Ma'lumot topilmadi!")

# 📌 **Ertangi namoz vaqtlari**
@router.message(F.text == "📅 Ertangi vaqt")
async def tomorrow_handler(message: types.Message):
    user_id = message.from_user.id
    region = user_regions.get(user_id, "Toshkent")
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    times = get_tomorrow_times(region, tomorrow)

    if times:
        await message.answer(
            f"📅 Ertangi kun ({tomorrow})\n\n🌅 Saharlik: {times[0]}\n🌙 Iftorlik: {times[1]}"
        )
    else:
        await message.answer("❌ Ma'lumot topilmadi!")

# 📌 **Duo (matn shaklida)**
@router.message(F.text == "🤲 Duo")
async def duo_handler(message: types.Message):
    await message.answer(
        "🌙 **Saharlik (ro‘za tutish) duosi:**\n"
        "📖 *Arabcha:*\n"
        "نَوَيْتُ أَنْ أَصُوْمَ صَوْمَ شَهْرِ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ خَالِصًا لِلَّهِ تَعَالَى\n\n"
        "📝 *O‘zbekcha ma’nosi:*\n"
        "\"Bomdoddan shomgacha Ramazon oyining ro‘zasini ixlos bilan Alloh taolo uchun tutishga niyat qildim.\"\n\n"
        
        "🌙 **Iftorlik (ro‘zani ochish) duosi:**\n"
        "📖 *Arabcha:*\n"
        "اللَّهُمَّ لَكَ صُمْتُ وَبِكَ آمَنْتُ وَعَلَيْكَ تَوَكَّلْتُ وَعَلَى رِزْقِكَ أَفْطَرْتُ فَاغْفِرْ لِي يَا غَفَّارُ مَا قَدَّمْتُ وَمَا أَخَّرْتُ\n\n"
        "📝 *O‘zbekcha ma’nosi:*\n"
        "\"Allohim! Faqat sening rizoliging uchun ro‘za tutdim, Senga iymon keltirdim, Senga tavakkul qildim va bergan rizqing bilan iftor qildim. Ey G‘affor Zot, oldingi va keyingi gunohlarimni kechir!\"",
        parse_mode="Markdown"
    )
