import requests

# Your bot's API token
TOKEN = '7321066472:AAEcgCI50MUDyl1Khmgc1qVAl-oQN0qAPfc'  # Hide with environment variable. dont expose.
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


response_dictionary = {
    "hi": "Hello! Welcome to my world",
    "what is your name?": "My name is havybot, and I was created by 2 crazy developers Havilah and Quantum Ben",
    "i am hungry": "I am not a food bot , i am a telegram bot...no offence."
}


def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates['result']:
            message_text = str(update['message']['text']).lower()
            chat_id = update['message']['chat']['id']

            # Using if-elif-else statement
            # if message_text in response_dictionary:
            message_match = next((ban for ban in response_dictionary if ban in message_text), None)
            if message_match:
                print(message_match)
                send_message(chat_id, response_dictionary.get(message_match, ""))
            else:
                send_message(chat_id,
                             f"I'm sorry, my knowledge is limited\n I do not know the answer to '{message_text}.'")

            offset = update['update_id'] + 1


if __name__ == '__main__':
    """simple use case for testng
    Hi, how are you?
    What is your name?
    I am hungry, can I get food?
    Hey I am hungry."""
    main()
