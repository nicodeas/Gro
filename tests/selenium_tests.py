# Does not work due to database errors
import unittest
import time
from server import app, db
from server.models import User
from werkzeug.security import generate_password_hash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

class TestMainPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        db.create_all()
        test_user = User(first_name='test-fname', last_name='test-lname',
                        username='test-uname', password_hash=generate_password_hash('test-pass'))
        db.session.add(test_user)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.driver.quit()
  
    def test_existing_account(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.maximize_window()
        # Test that the game link is not present if logged out
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.LINK_TEXT, "Game")
        login = self.driver.find_element(By.CSS_SELECTOR, ".glyphicon-log-in")
        login.click()
        self.driver.find_element(By.ID, "username-input").send_keys("test-uname")
        self.driver.find_element(By.ID, "password-input").send_keys("test-pass")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(2)
        # Test that the game link becomes visible once logged in
        game = self.driver.find_element(By.LINK_TEXT, "Game")
        self.assertTrue(game.is_displayed)
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()
    
    def test_new_account_creation(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.maximize_window()
        # Test that the game link is not present if logged out
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element(By.LINK_TEXT, "Game")
        signup = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .btn")
        signup.click()
        self.driver.find_element(By.ID, "first-name-input").send_keys("new_test_first")
        self.driver.find_element(By.ID, "last-name-input").send_keys("new_test_last")
        self.driver.find_element(By.ID, "username-input").send_keys("new_test_user")
        self.driver.find_element(By.ID, "password-input").send_keys("new_test_password")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(2)
        # Test that the game link becomes visible once logged in
        game = self.driver.find_element(By.LINK_TEXT, "Game")
        self.assertTrue(game.is_displayed)
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()


if __name__ == '__main__':
    unittest.main(verbosity=2)