import webbrowser
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pyautogui
import os



url = 'aykutceng.github.io/'
path_list = ["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe","C:/Program Files (x86)/Google/Chrome/Application/google-chrome.exe","C:/Program Files/Mozilla Firefox/firefox.exe","C:/Program Files/Mozilla Firefox/mozilla.exe","C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe","C:/Program Files (x86)/Internet Explorer/iexplore.exe"]
try:
    for path in path_list:
        if(os.path.isfile(path)):
            pathBrowser = path + ' %s'
            webbrowser.get(pathBrowser).open(url)
            break

except:
    pyautogui.alert('Mevcut tarayıcı yok veya dizin yolu farklı. Lütfen bir tarayıcı seçiniz!', "Title")
    
    Tk().withdraw()

    chrome_path = askopenfilename(title = "LÜTFEN BİR TARAYICI SEÇİNİZ!",filetypes=[('browser files','chrome.exe google-chrome.exe mozilla.exe firefox.exe iexplore.exe msedge.exe')])
    chrome_path += ' %s'
    webbrowser.get(chrome_path).open(url)