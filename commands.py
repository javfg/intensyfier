# -*- coding: utf-8 -*-

import logging

from telegram import ParseMode

from utils import user_data

# Logging.
logging.basicConfig(format='[%(asctime)s] - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


#
# Info commands.
#
def start(update, context):
    """Sends welcome message when /start is issued."""
    logger.info(f"[{user_data(update)}] said hello")

    username = update.message.from_user.username

    update.message.reply_text(f"Hello {username}. Send me pics or ask for /help!")


def print_help(update, context):
    """Sends help message when /help is issued."""
    logger.info(f"[{user_data(update)}] asked for help")

    for help_msg in context.chat_data['help_msgs']:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=help_msg,
                                 parse_mode=ParseMode.MARKDOWN)


#
# Settings commands.
#
def set_stare(update, context):
    """Sets user config so next image will be a stare image."""
    logger.info(f"[{user_data(update)}] requested a stare")

    update.message.reply_text(f"Great! Send me a photo and I will try to find somebody in it.")

    context.user_data['command'] = 'stare'


def set_zoomstare(update, context):
    """Sets user config so next image will be a stare image."""
    logger.info(f"[{user_data(update)}] requested a zoomstare")

    update.message.reply_text(f"Great! Send me a photo and I will try to find somebody in it.")

    context.user_data['command'] = 'zoomstare'



#
# Action commands.
#
