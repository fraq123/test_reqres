from pages.elements_page import ReqresPage
from api_test.apishka import Location

response = Location()


class TestReqres:
    def test_reqres_list_user(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_list_user()
        api_result = response.test_list_users()
        assert int(web_result) == api_result

    def test_reqres_single_user(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_single_user()
        api_result = response.test_single_user()
        assert int(web_result) == api_result

    def test_reqres_single_user_not_found(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_single_user_not_found()
        api_result = response.test_single_user_not_found()
        assert int(web_result) == api_result

    def test_reqres_list_resource(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_list_resource()
        api_result = response.test_list_resource()
        assert int(web_result) == api_result

    def test_reqres_single_resource(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_single_resource()
        api_result = response.test_single_responce()
        assert int(web_result) == api_result

    def test_reqres_single_resource_not_found(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_single_resource_not_found()
        api_result = response.test_single_respoce_not_found()
        assert int(web_result) == api_result

    def test_reqres_create_user(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_create_user()
        api_result = response.test_post_create()
        assert int(web_result) == api_result

    def test_reqres_update_user(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_update_user()
        api_result = response.test_put_update()
        assert int(web_result) == api_result

    def test_reqres_update_user_patch(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_update_user_patch()
        api_result = response.test_patch_update()
        assert int(web_result) == api_result

    def test_reqres_delete_user(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_delete_user()
        api_result = response.test_delete()
        assert int(web_result) == api_result

    def test_reqres_register_successful(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_register_successful()
        api_result = response.test_register_successful()
        assert int(web_result) == api_result

    def test_reqres_register_unsuccessful(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_register_unsuccessful()
        api_result = response.test_register_unseccessful()
        assert int(web_result) == api_result

    def test_reqres_login_successful(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_login_successful()
        api_result = response.test_login_successful()
        assert int(web_result) == api_result

    def test_reqres_login_unsuccessful(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_login_unsuccessful()
        api_result = response.test_login_unsuccessful()
        assert int(web_result) == api_result

    def test_reqres_delayed_response(self,driver):
        click_reqres = ReqresPage(driver, 'https://reqres.in/')
        click_reqres.open()
        web_result = click_reqres.reqres_click_delayed_response()
        api_result = response.delayed_response()
        assert int(web_result) == api_result
