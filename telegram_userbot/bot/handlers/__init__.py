"""Control-bot handler registration for the hosted session and voice systems."""

from telegram.ext import Application, CommandHandler

from bot.handlers.host import build_host_handler, unhost_command
from bot.handlers.voice_chat import build_voice_chat_handler


async def start_command(update, context) -> None:
    await update.effective_message.reply_text(
        "Use /host to host your Telegram account. "
        "After hosting, use the private Voice Chat commands."
    )


def register_all(app: Application, manager) -> None:
    """Register only the handlers included in the Flexer runtime subset."""
    app.bot_data["manager"] = manager
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(build_host_handler())
    app.add_handler(CommandHandler("unhost", unhost_command))
    app.add_handler(build_voice_chat_handler())