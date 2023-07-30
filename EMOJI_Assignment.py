if __name__ == "__main__":
         message = input("> ")
         words = message.split( " ")
         output=""

emojis= { "disappointed":'🤦‍♀️',
         "clown":'🤡',
         "smile":'😊',
        "happy":"😀",
         "sad":"☹️",
         "lol" : "😂",
         "sick":"😨",
         "happy": "😀",
         "pissed off":"🤬",
         "I Hail ooo":'🙌',
         "in love": '😍',
         "love":"❤️",
         "kiss":'😘',
         "hug":'🤗',
         "cool":'😎',
         "okay":'👌',
         "rotfl":'🤣',





}

for word in words:
    output+= emojis.get(word, word) + " "
    print(output)
