from selenium.webdriver.common.by import By


class ReqresPageLocators:
    LIST_USERS = (By.CSS_SELECTOR, 'li[data-id="users"]')
    SINGLE_USERS = (By.CSS_SELECTOR, 'li[data-id="users-single"]')
    SINGLE_USERS_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="users-single-not-found"]')
    LIST_RESOURCE = (By.CSS_SELECTOR, 'li[data-id="unknown"]')
    SINGLE_RESOURCE = (By.CSS_SELECTOR, 'li[data-id="unknown-single"]')
    SINGLE_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="unknown-single-not-found"]')
    CREATE_USERS = (By.CSS_SELECTOR, 'li[data-id="post"]')
    UPDATE_USERS = (By.CSS_SELECTOR, 'li[data-id="put"]')
    UPDATE_USERS_PATCH = (By.CSS_SELECTOR, 'li[data-id="patch"]')
    DELETE_USERS = (By.CSS_SELECTOR, 'li[data-id="delete"]')
    REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-successful"]')
    REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-unsuccessful"]')
    LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-successful"]')
    LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-unsuccessful"]')
    DELAYED_RESPONSE = (By.CSS_SELECTOR, 'li[data-id="delay"]')

    RESPONSE = (By.CSS_SELECTOR, 'span[class="response-code"]')
    RESPONSE_BAD = (By.CSS_SELECTOR, 'span[class="response-code bad"]')
