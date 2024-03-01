import requests


while True:
    print("Введите url адреса:")
    url = input()
    print("Введите имя нового документа:")
    name = input()
    
    html = requests.get(url)
    with open(f"C:\\Users\\79144\\PycharmProjects\\test_task\\ForFiles\\{name}.txt", "w", encoding="utf-8") as f:
        f.write(html.text)
    
