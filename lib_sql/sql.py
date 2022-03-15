import mysql.connector
from user_sql import UserSQL
from genre_sql import GenreSQL
from authors_qsl import AuthorsSQL
from books_sql import BooksSQL
from datetime import datetime

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Abc12345!',
    db = 'chat',
    autocommit = True

)

# Инструмент для запуска SQL Команды
cursor = db.cursor()

user_manager = UserSQL(cursor=cursor)
genre_manager = GenreSQL(cursor=cursor)
authors_manager = AuthorsSQL(cursor=cursor)
books_manager = BooksSQL(cursor)

# print(books_manager.get_books_full_info())
for (book_id, book_name, author_id, authror_name, genre_id, genre_name) in books_manager.get_books_full_info():
    print(f"Book_id: {book_id}")
    print(f"Book_name: {book_name}")
    print(f"Author_id: {author_id}")
    print(f"Author_name: {authror_name}")
    print(f"Genre_id: {genre_id}")
    print(f"Genre_name: {genre_name}")
    print('-------------------------------------------')

# print(authors_manager.get_author(3))
cursor.close()