import time

from locators.page_locators import ReqresPageLocators
from pages.base_page import BasePage


class ReqresPage(BasePage):
    locators = ReqresPageLocators()

    def reqres_click_list_user(self):
        self.element_is_visible(self.locators.LIST_USERS).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_single_user(self):
        self.element_is_visible(self.locators.SINGLE_USERS).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_single_user_not_found(self):
        self.element_is_visible(self.locators.SINGLE_USERS_NOT_FOUND).click()
        status = self.element_is_present(self.locators.RESPONSE_BAD).text
        return status

    def reqres_click_list_resource(self):
        self.element_is_visible(self.locators.LIST_RESOURCE).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_single_resource(self):
        self.element_is_visible(self.locators.SINGLE_RESOURCE).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_single_resource_not_found(self):
        self.element_is_visible(self.locators.SINGLE_RESOURCE_NOT_FOUND).click()
        status = self.element_is_present(self.locators.RESPONSE_BAD).text
        return status

    def reqres_click_create_user(self):
        self.element_is_visible(self.locators.CREATE_USERS).click()
        time.sleep(2)
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_update_user(self):
        self.element_is_visible(self.locators.UPDATE_USERS).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_update_user_patch(self):
        self.element_is_visible(self.locators.UPDATE_USERS_PATCH).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_delete_user(self):
        self.element_is_visible(self.locators.DELETE_USERS).click()
        status = self.element_is_present(self.locators.RESPONSE_BAD).text
        return status

    def reqres_click_register_successful(self):
        self.element_is_visible(self.locators.REGISTER_SUCCESSFUL).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_register_unsuccessful(self):
        self.element_is_visible(self.locators.REGISTER_UNSUCCESSFUL).click()
        status = self.element_is_present(self.locators.RESPONSE_BAD).text
        return status

    def reqres_click_login_successful(self):
        self.element_is_visible(self.locators.LOGIN_SUCCESSFUL).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status

    def reqres_click_login_unsuccessful(self):
        self.element_is_visible(self.locators.LOGIN_UNSUCCESSFUL).click()
        status = self.element_is_present(self.locators.RESPONSE_BAD).text
        return status

    def reqres_click_delayed_response(self):
        self.element_is_visible(self.locators.DELAYED_RESPONSE).click()
        status = self.element_is_present(self.locators.RESPONSE).text
        return status








