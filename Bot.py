import asyncio
from pyrogram import Client, filters
from datetime import datetime, timedelta
from flask import Flask
from threading import Thread

# --- تنظیمات اکانت ---
API_ID = 26060584 
API_HASH = "aff2f3bb35ebdea3761316d013d960a9"
SESSION = "1BJWap1wBu7Pwz2_UpK5hXxHZthGCYnMKG2YaKSvPHmI_Ifmcis3mfdlVb8i3fLCvsPsT5PTxYOxTeHy8CThjWoVmZqPLbmbEErEPC2TTNR9sCKg0kEAcTN8fbIG1raWO9m_yxyMGE5fdV7XU2r6MgGO2uTZoigd3pIHt9P0OFdH7IUloitacXHt194cY2tHU7WBTKDTDoxLZLAlCEm_Vpa5A9mENFPz7OMBa3tPKvKPR1rM70NHDPVFgK6MBYABs14vyal7jV4IQofGl28xdwQ3RIXmQ6CfwoH0mTOyvOWUIkgvbwdKXyPMDLEi7Tfwdmy6wUFwMVrwrwHHmwR7DS3RlgtgH0yU="
NAME = "ᴛɪᴄᴋ-ᴛᴏᴄᴋ"
# --------------------

app = Client("my_self", session_string=SESSION, api_id=API_ID, api_hash=API_HASH)
web = Flask(__name__)

# دیتابیس ساده برای ذخیره فونت انتخابی (در حافظه)
current_font = 0

FONTS = [
    "0123456789", # 0: Default
    "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗", # 1: Bold
    "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡", # 2: Double Struck
    "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿", # 3: Mono
    "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫", # 4: Sans
    "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵", # 5: Sans Bold
    "⓪①②③④⑤⑥⑦⑧⑨", # 6: Circle
    "🄀⒈⒉⒊⒋⒌⒍⒎⒏⒐", # 7: Digit Period
    "⁰¹²³⁴⁵⁶⁷⁸⁹", # (نمونه عددی در استایل های خاص)
    "0⃣1⃣2⃣3⃣4⃣5⃣6⃣7⃣8⃣9⃣", # 9: Emoji
    "⁰¹²³⁴⁵⁶⁷⁸⁹"  # 10: SuperScript
]

def get_styled_time(time_str):
    mapping = str.maketrans("0123456789", FONTS[current_font])
    return time_str.translate(mapping)

@web.route('/')
def home():
    return "Self-Bot is Alive!"

@app.on_message(filters.me & filters.command("font", prefixes="/"))
async def change_font(_, message):
    global current_font
    try:
        index = int(message.command[1])
        if 0 <= index < len(FONTS):
            current_font = index
            await message.edit_text(f"✅ فونت ساعت به شماره {index} تغییر یافت.")
        else:
            await message.edit_text("❌ عدد وارد شده باید بین 0 تا 10 باشد.")
    except:
        await message.edit_text("❌ دستور اشتباه. مثال: `/font 2`")

async def clock_loop():
    async with app:
        while True:
            tehran_time = datetime.utcnow() + timedelta(hours=3, minutes=30)
            raw_time = tehran_time.strftime("%H:%M")
            styled_time = get_styled_time(raw_time)
            
            try:
                await app.update_profile(first_name=NAME, last_name=f"| {styled_time}")
            except Exception as e:
                print(f"Update Error: {e}")
            
            await asyncio.sleep(60)

if __name__ == "__main__":
    Thread(target=lambda: web.run(host="0.0.0.0", port=10000), daemon=True).start()
    app.run(clock_loop())
