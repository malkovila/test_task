import pika, sys, os
import smtplib
from email.mime.text import MIMEText

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='Errors')
    
 

    def callback(ch, method, properties, body):
        decoded_string = body.decode('utf-8') #декодируем полученные byte от rabbit в строку
        msg = MIMEText('Error!')
        msg['Subject'] = f'Error! Namme of file: {decoded_string}'
        msg['From'] = 'ilamalkov886@gmail.com'
        msg['To'] = email
        try:
            s = smtplib.SMTP('localhost')
            s.sendmail('ilamalkov886@gmail.com', [email], msg.as_string())
            s.quit()
        except:
            print("Почта недействительна.")
                


    channel.basic_consume(queue='Errors', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    print("Введите почту, на которую присылать сообщения об ошибках:\n")
    email = input()
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)