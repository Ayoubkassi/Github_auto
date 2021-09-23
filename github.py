from selenium import webdriver
from time import sleep

project_name = input("Enter the project name : ")
username = input("Enter Github username : ")
password = input("Enter Github password : ")



class GithubBot:
	def __init__(self,username,pw):
		self.driver = webdriver.Chrome()
		self.username = username
		self.driver.get("https://github.com/login")
		sleep(2)
		login_field = self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
		password_field = self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
		login_butt = self.driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
        









my_bot = GithubBot(username,password)
