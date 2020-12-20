import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTaniHub():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    def test_tanihub_number_1(self):
        self.driver.get('https://tanihub.com/')
        jabodetabek_option = self.driver.find_element_by_xpath("//p[text()='Jabodetabek']")
        user_image_button = self.driver.find_element_by_xpath("//img[@alt='profile']")
        time.sleep(5)
        jabodetabek_option.click()
        time.sleep(2)
        assert user_image_button.is_displayed()
        user_image_button.click()
        email_text_box = self.driver.find_element_by_xpath("//input[@type='email' and @id='input-icon-3']")
        assert email_text_box.is_displayed()
        email_text_box.send_keys('testinguser@mailinator.com')
        selanjutnya_msk_btn = self.driver.find_element_by_xpath("//button[@type='submit' and @id='Button-2']")
        assert selanjutnya_msk_btn.is_enabled()
        selanjutnya_msk_btn.click()
        time.sleep(2)
        password_txt_box = self.driver.find_element_by_xpath("//input[@type='password' and @id='input-password-4']")
        assert password_txt_box.is_displayed()
        password_txt_box.send_keys('admin123')
        selanjutnya_msk_btn.click()
        search_text_box = self.driver.find_element_by_xpath("//input[@id='input-icon-3' and @type='text']")
        assert search_text_box.is_displayed()
        search_text_box.send_keys('Minyak Goreng Rose Brand 2 L Karton')
        search_text_box.send_keys(Keys.ENTER)
        time.sleep(5)
        search_result_first_cart_button = self.driver.find_element_by_xpath("//button[@id='CardProduct-1601' and @type='button']")
        # assert search_result_first_cart_button.is_displayed()
        search_result_first_cart_button.click()
        keranjang_btn = self.driver.find_element_by_xpath("//button[@id='Button-2' and @type='button']/span")
        assert keranjang_btn.is_displayed()
        keranjang_btn.click()
        time.sleep(5)
        checkout_btn = self.driver.find_element_by_xpath("//button[text()='Checkout' and @type='button']")
        assert checkout_btn.is_displayed()
        checkout_btn.click()
        time.sleep(5)
        self.driver.quit()

    def test_tanihub_number_2(self):
        self.driver.get('http://timvroom.com/selenium/playground/')
        title_page = self.driver.title
        answer_box_1 = self.driver.find_element_by_id("answer1")
        answer_box_1.send_keys(title_page)
        name_txt_box = self.driver.find_element_by_id("name")
        name_txt_box.send_keys('Kilgore Trout')
        occupation_dropdown = self.driver.find_element_by_id("occupation")
        Select(occupation_dropdown).select_by_value('scifiauthor')
        list_blue_box = self.driver.find_elements_by_class_name("bluebox")
        answer_box_4 = self.driver.find_element_by_id("answer4")
        answer_box_4.send_keys(str(len(list_blue_box)))
        click_me_link = self.driver.find_element_by_xpath("//a[text()='click me']")
        click_me_link.click()
        red_box_element = self.driver.find_element_by_id("redbox")
        answer_box_6 = self.driver.find_element_by_id("answer6")
        answer_box_6.send_keys(str(red_box_element.get_attribute("class")))
        self.driver.execute_script('return ran_this_js_function()')
        value_script = self.driver.execute_script('return got_return_from_js_function()')
        answer_box_8 = self.driver.find_element_by_id("answer8")
        answer_box_8.send_keys(str(value_script))
        wrote_book_rdbtn = self.driver.find_element_by_xpath("//input[@type='radio' and @name='wrotebook']")
        wrote_book_rdbtn.click()
        answer_box_10 = self.driver.find_element_by_id("answer10")
        orange_box = self.driver.find_element_by_id("orangebox").location
        green_box = self.driver.find_element_by_id("greenbox").location
        answer_box_11 = self.driver.find_element_by_id("answer11")
        if green_box['y'] > orange_box['y']:
            answer_box_11.send_keys('orange')
        else:
            answer_box_11.send_keys('green')
        answer_box_10.send_keys(str(red_box_element.text))
        self.driver.set_window_size(850, 650)
        answer_box_13 = self.driver.find_element_by_id("answer13")
        answer_box_14 = self.driver.find_element_by_id("answer14")
        try:
            is_here_element = self.driver.find_element_by_id("ishere")
            if is_here_element.is_displayed():
                answer_box_13.send_keys('yes')
            else:
                answer_box_13.send_keys('no')
        except:
            answer_box_13.send_keys('no')
        try:
            purple_box = self.driver.find_element_by_id("purplebox")
            if purple_box.is_displayed():
                answer_box_14.send_keys('yes')
            else:
                answer_box_14.send_keys('no')
        except:
            answer_box_14.send_keys('no')
        click_then_wait_link = self.driver.find_element_by_xpath("//a[text()='click then wait']")
        click_then_wait_link.click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='click after wait']")))
        click_after_wait_link = self.driver.find_element_by_xpath("//a[text()='click after wait']")
        click_after_wait_link.click()
        self.driver.switch_to.alert.accept()
        submit_button = self.driver.find_element_by_id("submitbutton")
        submit_button.click()
        check_results = self.driver.find_element_by_id("checkresults")
        check_results.click()
        self.driver.quit()

def test_selenium_number_1():
    TestTaniHub().test_tanihub_number_1()

def test_selenium_number_2():
    TestTaniHub().test_tanihub_number_2()