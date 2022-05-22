import unittest
import time
from server import app, db
from server.models import User
from werkzeug.security import generate_password_hash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager

class TestMainPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.vars = {}
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()
        test_user = User(first_name='test-fname', last_name='test-lname',
                         username='test-uname', password_hash=generate_password_hash('test-pass'))
        db.session.add(test_user)
        db.session.commit()
  
    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
  
    def test_existing_account(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()
        self.driver.find_element(By.ID, "username-input").click()
        self.driver.find_element(By.ID, "username-input").send_keys("test-uname")
        self.driver.find_element(By.ID, "password-input").send_keys("test-pass")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.LINK_TEXT, "Game").click()
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()
    
    def test_new_account_creation(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        self.driver.find_element(By.ID, "first-name-input").click()
        self.driver.find_element(By.ID, "first-name-input").send_keys("new_test_first")
        self.driver.find_element(By.ID, "last-name-input").send_keys("new_test_last")
        self.driver.find_element(By.ID, "username-input").send_keys("new_test_user")
        self.driver.find_element(By.ID, "password-input").send_keys("new_test_password")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(1)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Log Out").click()
        self.driver.find_element(By.LINK_TEXT, "Activity").click()
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()


if __name__ == '__main__':
    unittest.main(verbosity=2)