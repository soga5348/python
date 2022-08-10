from tkinter import BROWSE # ブラウズ機能のインポート
from selenium import webdriver # webdriver機能のインポート
'''
webdriver-manager
このライブラリを使うと、プログラム実行時に現在のGoogle Chromeのバージョンを確認し、
自動で適切なChrome Driverをあてて実行してくれます→お客さんにいちいちバージョン確認をしてもらう必要がない
'''
from webdriver_manager.chrome import ChromeDriverManager 
from time import sleep # time機能のインポート
import os, signal


browser = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
sleep(3)

elem_username = browser.find_element_by_id("username") # idで場所を取得している→class等でも取得できる
elem_username.send_keys("imanishi")

elem_password = browser.find_element_by_id("password")
elem_password.send_keys("kohei")

elem_login_btn = browser.find_element_by_id("login-btn")
elem_login_btn.click()

# browser.quit() # ブラウザを残さずchromedriverを閉じる
os.kill(browser.service.process.pid, signal.SIGTERM) # ブラウザを残したままchromedriverを閉じる