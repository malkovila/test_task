import pymysql
import time
import sys, os
from email.mime.text import MIMEText
import smtplib
from multiprocessing import Process

from flask import Flask, request

app = Flask(__name__)

def main():
 #подключаемся к базе данных
    try:
        connection_db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='first_user',
            password='qwerty',
            database='db_name',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)

        while True:
            with connection_db.cursor() as cursor:
                zapros = f"SELECT word FROM  count_of_words GROUP BY word HAVING {n} < sum(count) DISTINCT;"
                cursor.execute(zapros) 

                rows = cursor.fetchall() # список слов с превышением

                for i in rows: 
                    zapros2 = f"SELECT path FROM count_of_words WHERE word = {i} DISTINCT;"
                    cursor.execute(zapros2)
                    paths = cursor.fetchall()#получаем список всех путей для данного слова
                    for j in paths: #обнуляем пути
                        zapros4 = f"UPDATE path SET path = NULL WHERE path = {j}"

                    msg = MIMEText('ReadMaster!')
                    msg['Subject'] = f'Слово - {i}, пути - volumes\\files\\Analizator\\{paths}'
                    msg['From'] = 'ilamalkov886@gmail.com'
                    msg['To'] = email
                    s = smtplib.SMTP('localhost')
                    s.sendmail('ilamalkov886@gmail.com', [email], msg.as_string())
                    s.quit() 

                for i in rows:
                    zapros3 = f"UPDATE count_of_words SET count = 0 WHERE word = {i}"
                    cursor.execute(zapros3) #обнуляем значения
                    connection_db.commit()

                    

            time.sleep(20)

    except Exception as ex:
            print("Connection refused...")
            print(ex)        


@app.route('/info')
def get_info(): #для вывода инфы из таблицы
    try:
        connection_db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='first_user',
        password='qwerty',
        database='db_name',
        cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        with connection_db.cursor() as cursor:
            zapros2 = f"SELECT * FROM count_of_words;"
            cursor.execute(zapros2)

            rows = cursor.fetchall()
            string = ""
            for i in rows:
                for j in i:
                    string = string + ' ' + j
                string = string + '\n'

            connection_db.close() 
            return string
        
    except Exception as ex:
            print("Connection refused...")
            print(ex)        


def call_get_info():
    app.run(debug=True)
    while True:
        get_info()


if __name__ == '__main__':
    print("Введите email:")
    email = input()

    print("Введите максимальное возможное колличество повторений слова:")
    n = int(input())
    p1 = Process(target=call_get_info, daemon=True)
    p1.start()

    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
