from bs4 import BeautifulSoup
import pyautogui
import time
with open("test.html", encoding='utf-8') as f:
    word_str = ' '.join([''.join([letter.text for letter in word]) for word in BeautifulSoup(f, "html.parser").find(id="words")])
time.sleep(1.2)
pyautogui.write(word_str, interval=0.01)