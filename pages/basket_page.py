from stepic_project.pages.base_page import BasePage
from stepic_project.pages.locators import BasketPageLocators


class BasketPage(BasePage): 

    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)


    def is_basket_empty(self):
<<<<<<< HEAD
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)
=======
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)
>>>>>>> 5770ec94eed869a9196a1a5e024a66a3ef4bf6b9
