import asyncio
from datetime import datetime, timedelta
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# ============ CONFIG ============
API_ID = 26060584
API_HASH = "aff2f3bb35ebdea3761316d013d960a9"

SESSION_STRING = (
    "BAGNpygAN7kMlF4tSI0F3RpM_S7UNPQg0T4Z1eH10A9bLVq_hJIG0qho5oJsZcF-G6zDQJisYFD0PTYspjt6xu1IZ3ubtsiTBurBpjmm27BoZFJtfOQi3GY8qpNgxj9mspIiqv1T6mR0Anx5_fmv03zRBTbAwTxU9wSJg5IHpXVCtXGBeDTclMSvn8FYJdyHS55ni8F6II17gL_Em94Wq_E5MV78ubJXCt7nSEz3mcmFQ0Kmnij5vFWlTLn3womZsNc_JQU96Qd7EuPqNdczCdlIROmBAuoqGCoYs0AxW0Pl3HtqrEJNfj0EA_EhyzOmyfWBuMeGuuCIYm8jXoCG2jVcMUH0ygAAAAHcJW4LAA"
)

NAME = "ᴛɪᴄᴋ-ᴛᴏᴄᴋ"
# ================================

app = Client(
    name="ticktock",
    session_string=SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)

web = Flask(__name__)

FONTS = [
    "0123456789",
    "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗",
    "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡",
    "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿",
    "⓪①②③④⑤⑥⑦⑧⑨"
]

current_font = 0

def stylize(text: str) -> str:
    return text.translate(str.maketrans("0123456789", FONTS[current_font]))

@web.route("/")
def home():
    return "Alive"

@app.on_message(filters.me & filters.command("font"))
async def set_font(_, msg):
    global current_font
    try:
        i = int(msg.command[1])
        if 0 <= i < len(FONTS):
            current_font = i
            await msg.edit(f"✅ فونت شد {i}")
        else:
            await msg.edit("❌ عدد نامعتبر")
    except:
        await msg.edit("مثال: /font 2")

async def clock_loop():
    async with app:
        while True:
            tehran = datetime.utcnow() + timedelta(hours=3, minutes=30)
            t = stylize(tehran.strftime("%H:%M"))
            try:
                await app.update_profile(
                    first_name=NAME,
                    last_name=f"| {t}"
                )
            except Exception as e:
                print("Update error:", e)
            await asyncio.sleep(60)

def run_web():
    web.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    Thread(target=run_web, daemon=True).start()
    app.run(clock_loop())
