import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get('8929420918:AAGBG-uI1TYBQH_4p_7SZ5X9Nh0wbBtkQto')
print(f"DEBUG TOKEN: {repr(TOKEN)}")  # අලුතෙන්
print(f"DEBUG TOKEN LENGTH: {len(TOKEN) if TOKEN else 'None'}")  # අලුතෙන්

AD_LINK = "https://www.effectivecpmnetwork.com/m9crbafj?key=955ca13aae348d36d62d00bff8367325"
CHANNEL_ID = -1003846056544
VIDEO_MESSAGE_ID = 2

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "🎬 Video එක බලන්න Ready ද?\n\n1. පහළ '🔓 Video Unlock' button එක ඔබන්න\n2. Ad එකේ තප්පර 5-10ක් ඉන්න\n3. ආයෙත් Bot එකට ඇවිත් '✅ Verified' ඔබන්න"
    keyboard = [[InlineKeyboardButton("🔓 Video Unlock කරන්න", callback_data="get_ad")]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "get_ad":
        keyboard = [[InlineKeyboardButton("🔗 Ad එක බලන්න", url=AD_LINK)], [InlineKeyboardButton("✅ Verified", callback_data="verify")]]
        await query.edit_message_text("Ad එක බලලා Verified ඔබන්න.", reply_markup=InlineKeyboardMarkup(keyboard))
    elif query.data == "verify":
        await query.edit_message_text("✅ Verified! Video එක එවනවා...")
        try:
            await context.bot.copy_message(query.message.chat_id, CHANNEL_ID, VIDEO_MESSAGE_ID)
        except Exception as e:
            await query.message.reply_text(f"❌ Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot එක Run වෙනවා...")
    app.run_polling()

if __name__ == '__main__':
    main()
