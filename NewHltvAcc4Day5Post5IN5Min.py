#########################################
#	Created By Luiz Guilherme Fritsch	#
#			17/12/2018					#
#	www.github.com/luizfritsch			#
#	fritsch.guilherm3@gmail.com 		#
#########################################
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
i = 1
while i<6:
	driver = webdriver.Chrome()
	driver.get("https://www.hltv.org")
	driver.maximize_window()
	driver.find_element_by_xpath("/html/body/div[1]/nav/div[9]").click()
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='loginpopup']/form/input[1]").send_keys("")
	driver.find_element_by_xpath("//*[@id='loginpopup']/form/input[2]").send_keys("")
	driver.find_element_by_xpath("//*[@id='loginpopup']/form/button").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[4]/aside[1]/h1/a").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/div[1]/div[5]/div[1]/a/div[1]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/a").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[3]/div[3]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[21]/div[1]/textarea").send_keys("+1")
	time.sleep(300)
	#WebElement cell = driver.findElement(By.xpath("//table/tbody/tr[2]/td[3]"));