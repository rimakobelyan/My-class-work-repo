from repodemo.histories_project.POM.lib.assertions import assert_that
from repodemo.histories_project.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class HowDidChristmasStart(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    first_header_text=(By.ID, 'how-did-christmas-start')

    def assert_first_header_text(self):
      actual_text= self.find(self.first_header_text,get_text=True)
      assert_that(actual_text,"How Did Christmas Start?")

    def go_to_main_page(self):
        self.go_to_backwards()