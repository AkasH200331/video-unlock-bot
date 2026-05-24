import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get('TOKEN')

AD_LINK = "https://www.effectivecpmnetwork.com/m9crbafj?key=955ca13aae348d36d62d00bff8367325"
CHANNEL_ID = -1003846056544  # ඔයාගේ Channel ID එක දාන්න
VIDEO_MESSAGE_ID = 2       # ඔයාගේ Video Message ID එක දාන්න

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🎬 Video එක බලන්න Ready ද?

1. පහළ "🔓 Video Unlock" button එක ඔබන්න
2. Ad එකේ තප්පර 5-10ක් ඉන්න 
3. ආයෙත් Bot එකට ඇවිත් "✅ Verified" ඔබන්න

එච්චරයි! Video එක එවනවා.
    """
    keyboard = [[InlineKeyboardButton("🔓 Video Unlock කරන්න", callback_data="get_ad")]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "get_ad":
        keyboard = [
            [InlineKeyboardButton("🔗 Ad එක බලන්න", url=AD_LINK)],
            [InlineKeyboardButton("✅ Verified - Video එක ගන්න", callback_data="verify")]
        ]
        await query.edit_message_text(
            text="👇 Step 1: Ad එක බලන්න\n\nAd එක open කරලා තප්පර 5ක් ඉඳලා ආයෙත් ඇවිත් පහළ 'Verified' ඔබන්න.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    elif query.data == "verify":
        await query.edit_message_text("✅ Verified! Video එක එවනවා...")
        try:
            await context.bot.copy_message(
                chat_id=query.message.chat_id,
                from_chat_id=CHANNEL_ID,
                message_id=VIDEO_MESSAGE_ID
            )
            await start(update, context)
        except Exception as e:
            await query.message.reply_text(f"❌ Error: {e}\n\nBot channel එකේ admin කරලා තියෙනවද check කරන්න.")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot එක Run වෙනවා...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
