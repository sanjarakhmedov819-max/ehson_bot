import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 👉 Token (tez ishga tushish uchun kiritildi; keyin ENV ga o‘tkazamiz)
BOT_TOKEN = "8200240692:AAGZ1ufDqSSPtfpHJdfTIsLuT-hB6rrHekw"

PORT = int(os.environ.get("PORT", "8080"))
BASE_URL = os.environ.get("BASE_URL", "")   # Render’da Public URL ni keyin ENV ga qo‘yasiz
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET", "secret123")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Webhook rejimidagi bot ishga tushdi ✅")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start yuboring 😊")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    if not BASE_URL:
        raise SystemExit("BASE_URL bo'sh. Render’da Public URL ni BASE_URL env sifatida qo'ying, so'ng redeploy qiling.")

    webhook_url = f"{BASE_URL}/{BOT_TOKEN}"
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        secret_token=WEBHOOK_SECRET,
        webhook_url=webhook_url
    )

if __name__ == "__main__":
    main()
