import logging
import time
from pathlib import Path

# pip install watchdog
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# папка, где ищем новые файлы
path = "C:\\Users\\79144\\PycharmProjects\\test_task\\ForFiles"

event_handler = LoggingEventHandler()

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