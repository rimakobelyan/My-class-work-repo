import pytest

from repodemo.histories_project.POM.lib.helpers import Helpers


@pytest.mark.usefixtures("get_driver")
class TestTwoPagesFunctionality():
  def test_assert_that_first_text_is_equal_to_main_text(self):
      self.home_page.click_on_home_page_first_text_button()
      self.how_did_christmas_start_page.assert_first_header_text()
      self.how_did_christmas_start_page.go_to_main_page()

