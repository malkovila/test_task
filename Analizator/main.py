import pika, sys, os
import re
import pymysql

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='Parsing')
    
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

        # создаем таблицу
        with connection_db.cursor() as cursor:
            create_table_query = "CREATE TABLE count_of_words(id int AUTO_INCREMENT," \
                        " word varchar(32)," \
                        " count INT," \
                        " path varchar(32))"\
                        "INDEX name_index (name);"
            cursor.execute(create_table_query) 

    

    except Exception as ex:
        print("Connection refused...")
        print(ex)


    def callback(ch, method, properties, body):
        decoded_string = body.decode('utf-8') #декодируем полученные byte от rabbit в строку
        map ={}
        non_letter_regex = r'\W'

        with open(f"C:\\Users\\79144\\PycharmProjects\\test_task\\volumes\\files\\Analizator\\{decoded_string}", "r", encoding="utf-8") as f:
            text = f.read()
        
        s = re.split(non_letter_regex, text)
        
        
        for i in s: #счиатем колличество вхождений слов
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        
        f.close()
        
        for i in map:#обновление таблицы
            with connection_db.cursor() as cursor:

                zapros_update = f"INSERT INTO count_of_words(word, count, path) VALUES ({i}, {map[i]}, {decoded_string});" 
                cursor.execute(zapros_update)
                connection_db.commit()
                

    channel.basic_consume(queue='Parsing', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection_db.close()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)