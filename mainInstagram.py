from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
# pip install webdriver_manager
# pip install selenium
class IGBot:
    def __init__(self,username,password):
        self.username= username
        self.password=password
        self.bot= webdriver.Chrome(ChromeDriverManager().install())
    def loguearse(self):
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login')
        time.sleep(3)
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)
        time.sleep(3)
    def seguir(self,cuentas,cantidad):
        self.cuentas=cuentas
        bot = self.bot
        for user in cuentas:
            bot.get('https://www.instagram.com/'+user)
            time.sleep(4)
            bot.find_element_by_xpath('//a[@href="/'+ user +'/followers/"]').click()
            time.sleep(20)
            for i in range(1,cantidad):
                bot.find_element_by_xpath('//button[@class="sqdOP  L3NKy    _8A5w5    "]').click()

arrayCuentas = ["cristianbatti","surditto","leo_deluglio","elnesco","tinchoromagnoli","facunemmi","marcoscondomi","aloantonini"]
bot = IGBot("user","password")
bot.loguearse()
for x in range(1,10000):
    time.sleep(10)
    bot.seguir(arrayCuentas,10)




