from typing import NoReturn

from base.base_class import Base


class DriverAdd(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    driver_owner_button = {
        "xpath": "//button[contains(@class, 'vz-form-item') and .//div[@class='ant-input flexbox']]",
        "name": "driver_owner_button"
    }
    select_first_radio = {
        "xpath": "(//input[@type='radio'])[3]",
        "name": "select_first_radio"
    }
    confirm_owner_button = {
        "xpath": "//button[@class='ant-btn margin-left-15 ant-btn-primary']",
        "name": "confirm_owner_button"
    }
    surname_input = {
        "xpath": "//input[@id='surname']",
        "name": "surname_input"
    }
    name_input = {
        "xpath": "//input[@id='name']",
        "name": "name_input"
    }
    patronymic_input = {
        "xpath": "//input[@id='patronymic']",
        "name": "patronymic_input"
    }
    passport_id_input = {
        "xpath": "//input[@id='passportId']",
        "name": "passport_id_input"
    }
    passport_by_input = {
        "xpath": "//input[@id='passportIssuedBy']",
        "name": "passport_by_input"
    }
    passport_code_input = {
        "xpath": "//input[@id='passportUnitCode']",
        "name": "passport_code_input"
    }
    """Date of birth"""
    date_of_birth_input = {
        "xpath": "//*[@id='dateOfBirth']/div/input",
        "name": "date_of_birth_input"
    }
    """Passport issued at date"""
    passport_date_input = {
        "xpath": "//*[@id='passportIssuedAtDate']/div/input",
        "name": "passport_date_input"
    }
    driver_inn_input = {
        "xpath": "//input[@id='inn']",
        "name": "driver_inn_input"
    }
    license_id_input = {
        "xpath": "//input[@id='driverLicenseId']",
        "name": "license_id_input"
    }
    """Driver license expires at date"""
    license_date_reset = {
        "xpath": "//*[@id='driverLicenseExpiresAtDate']/div/i[1]",
        "name": "license_date_reset"
    }
    license_date_input_close = {
        "xpath": "//*[@id='driverLicenseExpiresAtDate']/div/input",
        "name": "license_date_input_close"
    }
    license_date_input_open = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "license_date_input_open"
    }
    license_toggl = {
        "xpath": "//*[@id='dlRusResident']",
        "name": "license_toggl"
    }
    license_issued_by_input = {
        "xpath": "//*[@id='driverLicenseIssuedBy']",
        "name": "license_issued_by_input"
    }
    license_issued_please_input = {
        "xpath": "//*[@id='driverLicensePlaceOfBirth']",
        "name": "license_issued_please_input"
    }
    license_issued_date_input = {
        "xpath": "(//input[contains(@class, 'ant-calendar-picker-input') and @placeholder='дд.мм.гггг'])[4]",
        "name": "license_issued_date_input"
    }
    app_phone_input = {
        "xpath": "//input[@id='applicationPhone']",
        "name": "app_phone_input"
    }
    contact_phone_input = {
        "xpath": "//input[@id='contactPhone']",
        "name": "contact_phone_input"
    }
    reg_address_input = {
        "xpath": "//input[@id='registrationAddress']",
        "name": "reg_address_input"
    }
    fact_address_input = {
        "xpath": "//input[@id='factAddress']",
        "name": "fact_address_input"
    }
    """Sanitary book date"""
    sanitary_book_toggl = {
        "xpath": "//*[@id='hasSanitaryBook']",
        "name": "sanitary_book_toggl"
    }
    sanitary_book_date_input_close = {
        "xpath": "//*[@id='sanitaryBookExpiresAtDate']/div/input",
        "name": "sanitary_book_date_input_close"
    }
    sanitary_book_date_input_open = {
        "xpath": "//input[@class='ant-calendar-input ']",
        "name": "sanitary_book_date_input_open"
    }
    create_driver_button = {
        "xpath": "//button[text()='Добавить водителя']",
        "name": "create_driver_button",
        "reference_xpath": "//span[@class='ant-modal-confirm-title' and text()='Водитель был успешно создан']",
        "reference": "Водитель был успешно создан"
    }
    confirm_button = {
        "xpath": "//button[@class='ant-btn ant-btn-primary']",
        "name": "confirm_button"
    }
    driver_edit_button = {
        "xpath": "//button[contains(text(), 'Редактировать Профиль')]",
        "name": "driver_edit_button"
    }
    passport_toggl = {
        "xpath": "//*[@id='passportRusResident']",
        "name": "sanitary_book_toggl"
    }
    """Driver country drop-down list"""
    driver_country_select = {
        "xpath": "//*[@id='country']",
        "name": "driver_country_select"
    }
    driver_city_input = {
        "xpath": "//*[@id='placeOfBirth']",
        "name": "driver_city_input"
    }
    save_button = {
        "xpath": "//button[@class='semi-wide margin-left-16 element-button theme-primary']",
        "name": "save_button",
        "reference_xpath": "//span[contains(text(), 'Данные водителя успешно обновлены')]",
        "reference": "Данные водителя успешно обновлены"
    }

    # Methods
    def add_base_driver(self) -> NoReturn:
        """
        Добавляет информацию о водителе. Включает заполнение личных данных, идентификационных номеров и адресов, а
        также управление санитарной книжкой. Процесс завершается созданием и подтверждением создания записи о водителе.

        Parameters
        ----------
        Нет входных параметров.

        Returns
        -------
        NoReturn
            Ничего не возвращает. Побочные эффекты: изменения на веб-странице.
        """
        # Ввод информации о водителе
        self.input_in_field(self.surname_input, f"Ф-{self.get_timestamp()}")
        self.input_in_field(self.name_input, f"И-{self.get_timestamp()}")
        self.input_in_field(self.patronymic_input, f"О-{self.get_timestamp()}")
        self.input_in_field(self.passport_id_input, self.random_value_int_str(1000000000, 9999999999))
        self.input_in_field(self.passport_by_input, "Верховный рулевой")
        self.click_and_input_in_field(self.passport_code_input, self.random_value_int_str(100000, 999999))
        self.input_in_field(self.license_id_input, self.random_value_int_str(1000000000, 9999999999))
        self.click_button(self.license_date_input_close)
        self.backspace_len_and_input(self.license_date_input_open, '45')
        # Ввод контактной информации
        self.click_and_input_in_field(self.app_phone_input, self.random_value_int_str(9650000000, 9659999999))
        self.click_and_input_in_field(self.contact_phone_input, self.random_value_int_str(9650000000, 9659999999))
        self.input_in_field(self.reg_address_input, "Мой адрес – Не дом и не улица")
        self.input_in_field(self.fact_address_input, "Мой адрес – Советский Союз.")
        # Управление настройками санитарной книжки и подтверждение создания водителя
        buttons_to_click = [
            {'button': self.sanitary_book_toggl, 'do_assert': False, 'wait': None},
            {'button': self.create_driver_button, 'do_assert': True, 'wait': 'form'},
            {'button': self.confirm_button, 'do_assert': False, 'wait': 'lst'}
        ]
        for button_info in buttons_to_click:
            self.click_button(button_info['button'], do_assert=button_info.get('do_assert', False),
                              wait=button_info.get('wait', None))

    def add_base_inner_driver(self) -> NoReturn:
        """
        Добавляет информацию о водителе внктреннего перевозчика. Включает выбор владельца, заполнение личных данных,
        идентификационных номеров и адресов, а также управление санитарной книжкой. Процесс завершается созданием и
        подтверждением создания записи о водителе.

        Parameters
        ----------
        Нет входных параметров.

        Returns
        -------
        NoReturn
            Ничего не возвращает. Побочные эффекты: изменения на веб-странице.
        """
        # Выбор владельца водителя
        buttons_to_click = [
            {'button': self.driver_owner_button, 'do_assert': False, 'wait': "lst"},
            {'button': self.select_first_radio, 'do_assert': False, 'wait': None},
            {'button': self.confirm_owner_button, 'do_assert': False, 'wait': None}
        ]
        for action in buttons_to_click:
            self.click_button_located(action['button'], do_assert=action.get('do_assert', False),
                                      wait=action.get('wait', None))
        # Ввод информации о водителе
        self.input_in_field(self.surname_input, f"ВФ-{self.get_timestamp()}")
        self.input_in_field(self.name_input, f"ВИ-{self.get_timestamp()}")
        self.input_in_field(self.patronymic_input, f"ВО-{self.get_timestamp()}")
        self.input_in_field(self.passport_id_input, self.random_value_int_str(1000000000, 9999999999))
        self.input_in_field(self.passport_by_input, "Верховный рулевой")
        self.click_and_input_in_field(self.passport_code_input, self.random_value_int_str(100000, 999999))
        self.input_in_field(self.license_id_input, self.random_value_int_str(1000000000, 9999999999))
        self.click_button(self.license_date_input_close)
        self.backspace_len_and_input(self.license_date_input_open, '45')
        # Ввод контактной информации
        self.click_and_input_in_field(self.contact_phone_input, self.random_value_int_str(9650000000, 9659999999))
        self.input_in_field(self.reg_address_input, "Мой адрес – Не дом и не улица")
        self.input_in_field(self.fact_address_input, "Мой адрес – Советский Союз.")
        # Управление настройками санитарной книжки и подтверждение создания водителя
        buttons_to_click = [
            {'button': self.sanitary_book_toggl, 'do_assert': False, 'wait': None},
            {'button': self.create_driver_button, 'do_assert': True, 'wait': 'form'},
            {'button': self.confirm_button, 'do_assert': False, 'wait': 'lst'}
        ]
        for button_info in buttons_to_click:
            self.click_button(button_info['button'], do_assert=button_info.get('do_assert', False),
                              wait=button_info.get('wait', None))
