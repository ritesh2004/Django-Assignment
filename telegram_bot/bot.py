import telebot
import os

# setup django environment
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assignment.settings")
django.setup()

# Import the Django model
from api.models import TelegramUsers

# Ensure the TELEGRAM_BOT_TOKEN environment variable is set
token = os.getenv("TELEGRAM_BOT_TOKEN")

bot  = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    print(f"Received start command from {message.from_user.username} ({message.from_user.id})")
    # Save the user to the database
    telegram_user, created = TelegramUsers.objects.get_or_create(
        username=message.from_user.username
    )
    
    if created:
        print(f"New user created: {telegram_user.username} ({telegram_user.id})")
        bot.reply_to(message, f"Welcome {telegram_user.username}! You have been registered.")
        # Optionally, you can send a message to the user
        bot.send_message(message.chat.id, "Thank you for starting the bot!")
    else:
        print(f"User already exists: {telegram_user.username} ({telegram_user.id})")
        bot.reply_to(message, f"Welcome back {telegram_user.username}! You are already registered.")
    
bot.infinity_polling()