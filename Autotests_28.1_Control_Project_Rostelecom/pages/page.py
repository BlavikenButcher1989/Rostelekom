"""Функции заполнения полей и открытия некоторых ссылок"""
import allure

from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locator
from data_for_negative_test.data_for_test import DataForTests as data

class Page(BasePage):

    @allure.step('Авторизация с валидными данными')
    def authorization_form_fill_fields_and_submit_with_valid_data(self):  # Заполнение полей на форме авторизации и вход в учетную запись (позитивный сценарий)
        self.element_is_visible(Locator.EMAIL_TAB).click()
        self.element_is_visible(Locator.EMAIL_INPUT).clear()
        self.element_is_visible(Locator.EMAIL_INPUT).send_keys(data.valid_email)
        self.element_is_visible(Locator.PASSWORD).clear()
        self.element_is_visible(Locator.PASSWORD).send_keys(data.valid_password)
        self.element_is_visible(Locator.BUTTON_ENTER).click()


    @allure.step('Авторизация с верным Email и неверным паролем')
    def authorization_form_fill_fields_and_submit_with_valid_email_and_invalid_password(self):  # Заполнение полей на форме авторизации с неверным паролем (негативный сценарий)
        self.element_is_visible(Locator.EMAIL_TAB).click()
        self.element_is_visible(Locator.EMAIL_INPUT).clear()
        self.element_is_visible(Locator.EMAIL_INPUT).send_keys(data.valid_email)
        self.element_is_visible(Locator.PASSWORD).clear()
        self.element_is_visible(Locator.PASSWORD).send_keys(data.invalid_password)
        self.element_is_visible(Locator.BUTTON_ENTER).click()

    @allure.step('Регистрация с валидными данными')
    def registration_form_fill_fields_and_submit_with_valid_data(self):  #  Заполненеи полей на форме регистрации и регистрация (позитивный сценарий)
        self.element_is_visible(Locator.FIRST_NAME).send_keys('Иван')
        self.element_is_visible(Locator.LAST_NAME).send_keys('Иванов')
        self.element_is_visible(Locator.EMAIL).send_keys('ivan@ivanov.ru')
        self.element_is_visible(Locator.PASSWORD_FIRST).send_keys('Ivan2023@')
        self.element_is_visible(Locator.PASSWORD_CONFIRM).send_keys('Ivan2023@')
        self.element_is_visible(Locator.BUTTON_REGISTER).click()


    def registration_form_fill_fields_and_submit_with_valid_data_without_field_email(self):  #  Заполненеи всех полей на форме регистрации кроме поля Email и мобильный телефон (негативный сценарий)
        self.element_is_visible(Locator.FIRST_NAME).send_keys('Иван')
        self.element_is_visible(Locator.LAST_NAME).send_keys('Иванов')
        self.element_is_visible(Locator.PASSWORD_FIRST).send_keys('Ivan2023@')
        self.element_is_visible(Locator.PASSWORD_CONFIRM).send_keys('Ivan2023@')


    def registration_with_exist_account(self):  #  Регистрация с существующей учетной записью
        self.element_is_visible(Locator.FIRST_NAME).send_keys('Денис')
        self.element_is_visible(Locator.LAST_NAME).send_keys('Тестеров')
        self.element_is_visible(Locator.EMAIL).send_keys(data.valid_email)
        self.element_is_visible(Locator.PASSWORD_FIRST).send_keys(data.valid_password)
        self.element_is_visible(Locator.PASSWORD_CONFIRM).send_keys(data.valid_password)
        self.element_is_visible(Locator.BUTTON_REGISTER).click()

    @allure.step('Нажатие кнопки выхода из учетной записи')
    def logout_button_push(self):  #  Выход из учетной записи
        self.element_is_visible(Locator.BUTTON_LOGOUT).click()

    @allure.step('Открытие ссылки пользовательского соглашения')
    def terms_of_use_open(self):  #  Открытие ссылки пользовательского соглашения на странице авторизации
        self.element_is_visible(Locator.TERMS_OF_USE_LINK).click()

    @allure.step('Открытие формы регистрации')
    def registration_form_open(self):  #  Открытие формы регистрации на странице авторизации
        self.element_is_visible(Locator.REGISTRATION_FORM_LINK).click()

    @allure.step('Открытие ссылки формы восстановления пароля')
    def forgot_password_form_open(self):  #  Открытие формы восстановления пароля на странице авторизации
        self.element_is_visible(Locator.FORGOT_PASSWORD_FORM_LINK).click()