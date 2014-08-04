from selenium import webdriver
import pickle
import time, os

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=selenium')
options.add_argument('--user-data-dir=./userChrome')
options.userDataDir='./userChrome'
print options.to_capabilities()
browser = webdriver.Chrome(desired_capabilities=options.to_capabilities())
print "Start browser"
browser.get('http://139.91.70.152:8080/image/')
if (os.path.isfile("./cookies.pkl")):
	print "found cookies"
	cookies = pickle.load(open("cookies.pkl", "rb"))
	for cookie in cookies:
			if "clockTest" in str(cookie):
				print cookie
				browser.add_cookie(cookie)
browser.get('http://139.91.70.152:8080')
time.sleep(10) #sec
pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
print "Close browser"
browser.close()
display.stop()
