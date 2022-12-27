import telebot


bot = telebot.TeleBot('TELEGRAM BOT TOKEN')
chatid= CHAT ID

last_line= ""

while True:
    try:
        with open("PATH OF EXILE Client.txt PATH", "r", encoding="utf8") as f:
            lines = f.readlines()
        current_line = lines[-1]
        if current_line != last_line:
            last_line = current_line
            if "@From" in current_line:
                words = current_line.split()
                reach_at_from = False
                filtered_words = []
                for word in words: 
                    if word == "@From":
                        reach_at_from = True
                    if reach_at_from:
                        filtered_words.append(word)
                filtered_line = " ".join(filtered_words)
                bot.send_message(chat_id=chatid, text=filtered_line)
                print(filtered_line)
    except KeyboardInterrupt:
        break
