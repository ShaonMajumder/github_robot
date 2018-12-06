#-*- coding:utf-8 -*-
import sys,os,os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bot_utility import *

def github_login(browser):
	browser.get("https://github.com/")
	while True:
		try:
			wait = WebDriverWait(browser, 1)
			browser.find_element_by_link_text("Sign in").click()
			#sign_in = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Sign in"]')))
			break
		except NoSuchElementException:
			pass
		except TimeoutException:
			pass

	#sign_in.click
	browser.find_element_by_id("login_field").clear()
	browser.find_element_by_id("login_field").send_keys("smazoomder@gmail.com")
	browser.find_element_by_id("password").click()
	browser.find_element_by_id("password").clear()
	browser.find_element_by_id("password").send_keys("sh170892")
	browser.find_element_by_name("commit").click()
	save_cookies(browser)
	browser.close()


def command_line():
	arguments = sys.argv
	if(query_yes_no("Are sure want to login github?")):
		browser = get_webdriver({'image':'no','cache':'yes','UI':'yes'})
		github_login(browser)


if __name__ == "__main__":
	command_line()
	
