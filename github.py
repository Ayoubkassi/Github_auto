from selenium import webdriver
from time import sleep
import subprocess
import shlex


project_name = input("Enter the project name : ")
#username = input("Enter Github username : ")
password = input("Enter Github password : ")

link = "https://github.com/Ayoubkassi/"+project_name+".git"


class GithubBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://github.com/login")
        sleep(2)
        login_field = self.driver.find_element_by_xpath(
            '//*[@id="login_field"]').send_keys(username)
        password_field = self.driver.find_element_by_xpath(
            '//*[@id="password"]').send_keys(pw)
        login_butt = self.driver.find_element_by_xpath(
            '//*[@id="login"]/div[4]/form/div/input[12]').click()
        self.driver.get("https://github.com/new")
        sleep(2)
        repo_field = self.driver.find_element_by_xpath(
            '//*[@id="repository_name"]').send_keys(project_name)
        sleep(2)
        check_butt = self.driver.find_element_by_xpath(
            '//*[@id="repository_auto_init"]').click()
        sleep(2)
        create_butt = self.driver.find_element_by_xpath(
            '//*[@id="new_repository"]/div[4]/button').click()
        sleep(4)
        self.driver.close()


my_bot = GithubBot('Ayoubkassi', password)
subprocess.call(['bash', 'github.sh', link, project_name])
