import requests

# Your bot's API token
TOKEN = '7321066472:AAEcgCI50MUDyl1Khmgc1qVAl-oQN0qAPfc'
URL = f'https://api.telegram.org/bot{TOKEN}/'

def get_updates(offset=None):
    # Send a GET request to get updates
    url = URL + 'getUpdates'
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    # Send a POST request to send a message
    url = URL + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates['result']:
            message_text = update['message']['text']
            chat_id = update['message']['chat']['id']
           
            # Using if-elif-else statement
            if message_text == 'hi':
                send_message(chat_id, 'Hello! Welcome to my world')
            elif message_text == 'What is your name':
                send_message(chat_id, 'My name is havybot, and I was created by 2 crazy developers Havilah and Quantum Ben')
            else:
                send_message(chat_id, f'Hey unknown, you said: {message_text}')
               
            offset = update['update_id'] + 1

if __name__ == '__main__':
    main()