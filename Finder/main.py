import logging
import time
from pathlib import Path

# pip install watchdog
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import shutil
import pika
import logging
import os.path
import re

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# папка, где ищем новые файлы
path = "C:\\Users\\79144\\PycharmProjects\\test_task\\ForFiles"



#переопределение метода для отслеживания файлов
class CustomEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            pass
        else:
            shutil.copy(event.src_path, "C:\\Users\\79144\\PycharmProjects\\test_task\\volumes\\files\\Analizator")
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel() #устанавливаем соединение с rabbitMQ
            #print(event.src_path.split('\\')[-1].split('.')[-1])
            if event.src_path.split('\\')[-1].split('.')[-1]=='txt': #проверяем формат файла
                channel.queue_declare(queue='Parsing') #создаем очередь
                channel.basic_publish(exchange='',
                        routing_key='Parsing',        
                        body=(event.src_path.split('\\')[-1]))
            else:
                channel.queue_declare(queue='Errors') #создаем очередь
                channel.basic_publish(exchange='',
                        routing_key='Errors',        
                        body=(event.src_path.split('\\')[-1]))



            connection.close()

event_handler = CustomEventHandler()

observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

# для функционирования программы по тз переопределена функция def on_created в watchdog/events.py, которая отвечает за отслеживание добавления файла


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()