from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime, time
from zoneinfo import ZoneInfo

TOKEN = "7820794013:AAH7sszQ4SUr8sO2XA8CXKLCXc17YMDo_h8"
CHAT_ID = 6990124239

motivasi_harian = {
    "Senin": "LU MISKINNN ANJINGGGGGGGG.",
    "Selasa": "USAHA GOBLOKK.",
    "Rabu": "LAKI LAKI DI LARANG TUMBANG",
    "Kamis": "USAHA ANJINGGGG.",
    "Jumat": "PENGEN MIMPI BERHASIL USAHA ANJINGGG.",
    "Sabtu": "LU MISKIN, KARNA LU BEGO.",
    "Minggu": "BADJINGAN TIDAK BOLEH NYERAH!."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif.")

async def motivasi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hari_ini = datetime.now().weekday()
    await update.message.reply_text(motivasi_harian[list(motivasi_harian.keys())[hari_ini]])

async def kirim_otomatis(context: ContextTypes.DEFAULT_TYPE):
    hari_ini = datetime.now().weekday()
    print("Mengirim motivasi otomatis...")
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=motivasi_harian[list(motivasi_harian.keys())[hari_ini]]
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("motivasi", motivasi))

app.job_queue.run_daily(
    kirim_otomatis,
    time=time(hour=6, minute=0, tzinfo=ZoneInfo("Asia/Jakarta"))
)

print("Bot berjalan...")
app.run_polling()