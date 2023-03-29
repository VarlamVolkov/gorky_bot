from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

from lexicon.lexicon_ru import LEXICON_RU

# Главное меню
where_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_RU['where_button'],
    callback_data='where_button_pressed')
search_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_RU['search_button'],
    callback_data='search_button_pressed'),
than_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_RU['than_button'],
    callback_data='than_button_pressed')
keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[where_button],
                     [search_button],
                     [than_button]])
