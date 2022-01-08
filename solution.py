from bs4 import BeautifulSoup
import pyautogui
pyautogui.write(''.join([' ' for _ in range(100)]) + ' '.join([''.join([letter.text for letter in word]) for word in BeautifulSoup(open("test.html", encoding='utf-8'), "html.parser").find(id="words")]), interval=0.01)