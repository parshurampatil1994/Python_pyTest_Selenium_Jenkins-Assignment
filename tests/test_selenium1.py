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
    def test_login(self):
        driver.get("http://localhost:8080/")
        driver.find_element_by_name("j_username").send_keys("parshuram")
        driver.find_element_by_name("j_password").send_keys("28031894@Pp")
        driver.find_element_by_name("Submit").click()
        x = driver.title
        assert x == "abc"

    #
    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")