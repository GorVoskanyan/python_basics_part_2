import telebot
import requests

bot = telebot.TeleBot("7818721634:AAEjjDZvmEHGG50jFyvp999HrFcRTnrZXN8")  # Токен, полученный от BotFather.
url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/btc.json'


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello world!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = requests.get(url).json()
    date = data['date']
    btc_to_bnb = data['btc']['bnb']

    if message.text == 'BTC':
        bot.reply_to(message, f"Current date: {date}\nBTC/BNB: {btc_to_bnb}")
    elif message.text == 'ALL':
        for key, value in data['btc'].items():
            print(f"{'BTC'} | {key}")
            result = [f"1 BTC = {value:.2f} {key}"]
            bot.reply_to(message, '\n'.join(result))
    else:
        bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
