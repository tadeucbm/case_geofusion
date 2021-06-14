import pandas as pd
import json
import requests

from flask import Flask, request, Response


# constants
TOKEN = '1894420150:AAEjzlWq8q-_viM0Uey5YJlt5UktnH6voWg'

# info sobre o bot
#https://api.telegram.org/bot1894420150:AAEjzlWq8q-_viM0Uey5YJlt5UktnH6voWg/getMe

# get updates
#https://api.telegram.org/bot1894420150:AAEjzlWq8q-_viM0Uey5YJlt5UktnH6voWg/getUpdates

# get updates
#https://api.telegram.org/bot1894420150:AAEjzlWq8q-_viM0Uey5YJlt5UktnH6voWg/set


def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
    url = url + 'sendMessage?chat_id={}'.format(chat_id)
    
    r = requests.post(url, json={'text': text})
    print('Status Code {}'.format(r.status_code))

    return None


#def hello():
    




def parse_message(message):
    chat_id = message['message']['chat']['id']
    value = message['message']['text']

    return chat_id, value




# Iniciando a API
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    while True:
        if request.method == 'POST':

            message = request.get_json()
            chat_id, value = parse_message(message)

            send_message(chat_id, 'Olá! Gostaria de fazer uma previsão para um bairro?')
            
            if request.method == 'POST':
                message = request.get_json()
                chat_id, value = parse_message(message)

                if value == 1:
                    
                    send_message(chat_id, 'Deu Certo')
                    break

                else:
                    send_message(chat_id, 'Deu Certo')
                    break
            

            return Response('ok', status=200)


        

        

        #send_message(chat_id, 'teste')
    
        #if chat_id != 'error':
            # loading message
            #if message != 'error':

                #return Response('Ok', status=200)











        #else:
           # send_message(chat_id, )

   # else:
       # return '<h1> Geo Telegram BOT </h1>'
            


        


    else:
        return '<h1> Geo Telegram BOT </h1>'


if __name__ == '__main__':
    port = app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=port)
