from bs4 import BeautifulSoup
import pyautogui
import time

with open("test.html", encoding='utf-8') as f:
    soup = BeautifulSoup(f, "html.parser")

words = soup.find(id="words")
words_ls = []
for word in words:
    word_chars = []
    for letter in word:
        word_chars.append(letter.text)
    words_ls.append(word_chars)

word_str =  ' '.join([''.join(word) for word in words_ls])
print("word_str", word_str)

time.sleep(1)
pyautogui.write(word_str, interval=0.01)