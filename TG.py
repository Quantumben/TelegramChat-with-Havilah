import requests

# Your bot's API token
TOKEN = 'YOUR_API_TOKEN_HERE'
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
            # Extract the message text and chat ID
            message_text = update['message']['text']
            chat_id = update['message']['chat']['id']

            # Respond to the message
            send_message(chat_id, f'You said: {message_text}')

            # Update the offset to avoid processing the same message twice
            offset = update['update_id'] + 1

if __name__ == '__main__':
    main()
