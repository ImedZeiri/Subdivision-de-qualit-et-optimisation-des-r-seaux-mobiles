import os
import gtts

class Talk:
    def Talk(text):
        t1 = gtts.gTTS(text)
        t1.save("Welcome.mp3")
        file = "Welcome.mp3"
        os.system("mpg123 " + file)
    Talk
