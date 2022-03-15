
from email import message
from subprocess import call
import telebot
from config import TOKEN
from lib_sql.user_sql import UserSQL
from lib_sql.authors_qsl import AuthorsSQL
from lib_sql.genre_sql import GenreSQL
from lib_sql.books_sql import BooksSQL
from telebot import types
import mysql.connector

bot = telebot.TeleBot(TOKEN)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Abc12345!',
    db = 'chat',
    autocommit = True
)
cursor = db.cursor()


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    text = 'Welcome to the libriary-bot named after Ch.Aitmatov'
    markup = types.InlineKeyboardMarkup()
    my_cart = types.InlineKeyboardButton('My cart', callback_data='my_cart')
    genres = types.InlineKeyboardButton('Genres', callback_data='genre')
    search = types.InlineKeyboardButton('Search by name of books', callback_data='search')
    my_books = types.InlineKeyboardButton('My books', callback_data='my_books')
    markup.row_width = 1
    markup.add(my_cart, genres, search, my_books)

    bot.send_message(message.chat.id, text=text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='genre')
def send_all_genres(call):
    message = call.message
    genre_manager = GenreSQL(cursor)
    genres = genre_manager.get_all_genres()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    for (id, name) in genres:
        button = types.InlineKeyboardButton(name, callback_data=f'genre_{id}')
        markup.add(button)
    bot.edit_message_text(chat_id=message.chat.id, text='Chouse genre:', message_id=message.id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call:call.data=='my_books')
def send_user_books(call):
    message=call.message
    books_manager=BooksSQL(cursor)
    books = books_manager.get_books_full_info()
    markup = types.InlineKeyboardMarkup()
    for book in books:
        name = book[1]
        button = types.KeyboardButton(name, callback_data=f'book_{book[0]}')
        markup.add(button)
    markup.row_width = 2
    
    bot.edit_message_text(chat_id=message.chat.id, text='Chouse a book', message_id=message.id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: str(call.data).startswith('book_'))
def send_book_info(call):
    message=call.message
    book_manager = BooksSQL(cursor)
    book = call.data.split('_')
    book_id = book[1]
    book_data = book_manager.get_book_info(book_id)
    text = f"""
    Book name: {book_data[1]}
    Author: {book_data[3]}
    Genre: {book_data[5]}
    """
    bot.edit_message_text(
        chat_id = message.chat.id,
        text=text,
        message_id=message.id,
        reply_markup=None
        )

bot.infinity_polling()