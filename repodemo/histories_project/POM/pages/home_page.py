from repodemo.histories_project.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By

class HomePage(Helpers):
     def __init__(self, driver):
         super().__init__(driver)

     home_page_first_locator = (By.CLASS_NAME,'block-table-of-contents__link')

     def click_on_home_page_first_text_button(self):
         self.find_and_click(self.home_page_first_locator)


