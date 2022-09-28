from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    @pytest.mark.UI
    def test_login(self, test_setup):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element_by_id("username").send_keys("student")
        driver.find_element_by_id("password").send_keys("Password123")
        driver.find_element_by_id("submit").click()
        x = driver.title
        assert x == "Test Login | Practice Test Automation"

    #
    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")
