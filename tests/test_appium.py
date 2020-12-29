from appium import webdriver
import unittest
import time

from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AppiumTest(unittest.TestCase):
    desired_cap = {}
    appium_driver = None
    appium_service = None

    def setUp(self):
        self.appium_service = AppiumService()
        self.appium_service.start(args=['--address', '127.0.0.1', '-p', '4723'])
        self.desired_cap['appPackage'] = "com.android.vending"
        self.desired_cap['appActivity'] = "com.android.vending.AssetBrowserActivity"
        self.desired_cap['platformName'] = 'Android'
        self.desired_cap['deviceName'] = 'AndroidPNuggy'
        self.appium_driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_cap)

    def tearDown(self):
        self.appium_driver.quit()
        self.appium_service.stop()

    def test_add_listings(self):
        self.appium_driver.implicitly_wait(150)
        WebDriverWait(self.appium_driver, 20).until(expected_conditions.visibility_of_element_located((By.ID, "com.android.vending:id/0_resource_name_obfuscated")))
        time.sleep(30)
        search_txt_box = self.appium_driver.find_element_by_id("com.android.vending:id/0_resource_name_obfuscated")
        assert search_txt_box.is_displayed()
        search_txt_box.click()
        search_txt_box.send_keys("TaniHub")
        search_txt_box.submit()
        install_btn = self.appium_driver.find_element_by_xpath("//android.widget.Button[@text='Install']")
        assert install_btn.is_displayed()
        install_btn.click()
        WebDriverWait(self.appium_driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text='Open']")))
        open_btn = self.appium_driver.find_element_by_xpath("//android.widget.Button[@text='Open']")
        assert open_btn.is_displayed()
        open_btn.click()
        explore_btn = self.appium_driver.find_element_by_xpath("//android.widget.TextView[@text='Explore Sekarang']")
        explore_btn.click()
        WebDriverWait(self.appium_driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text='Jabodetabek']")))
        jabodetabek_btn = self.appium_driver.find_element_by_xpath("//android.view.ViewGroup/android.widget.TextView[@text='Jabodetabek']")
        jabodetabek_btn.click()
        search_item = self.appium_driver.find_element_by_xpath("//android.widget.TextView[@text='Cari buah, sayur, beras...']")
        search_item.click()
        search_item.send_keys('Minyak Goreng Rose Brand 2 L Karton')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)