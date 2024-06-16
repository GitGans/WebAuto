import allure
from tests.base_test import base_test_with_login
from pages.driver_add_page import DriverAdd
from pages.driver_list_page import DriverList


@allure.story("Critical path test")
@allure.feature('Создание и редактирование водителей')
@allure.description('ЛКЭ. Тест создания и редактирование собственного водителя Экспедитора: '
                    '1) создаем: ФИО - ФИО-timestamp, паспорт/права - РФ/РФ, № паспорт/код/права/тлф.апп/тлф. - Рандом,'
                    ' книжка - Нет.'
                    '2) редактируем: ФИО - ФИО-timestamp, паспорт/права - Другой/РФ, страна - Албания, город - Тирана, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, книжка - Да.')
def test_own_driver_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Создание нового собственного водителя
    surname = add_driver.add_base_driver()
    
    # Поиск и выбор созданного водителя по фамилии
    driver_list.input_in_field(driver_list.surname_filter, value=surname, wait="lst")
    driver_list.click_button(driver_list.first_driver_link, wait="form")
    
    # Редактирование данных водителя
    add_driver.click_button(add_driver.driver_edit_button, wait="form")
    add_driver.click_button(add_driver.passport_toggl)
    add_driver.dropdown_click_input_click(add_driver.driver_country_select, "Албания / Albania / ALB")
    add_driver.input_in_field(add_driver.driver_city_input, "Тирана")
    add_driver.backspace_all_and_input(add_driver.surname_input, f"Ф-{base.get_timestamp()}")
    add_driver.backspace_all_and_input(add_driver.name_input, f"И-{base.get_timestamp()}")
    add_driver.backspace_all_and_input(add_driver.patronymic_input, f"О-{base.get_timestamp()}")
    add_driver.backspace_all_and_input(add_driver.passport_id_input,
                                       base.random_value_float_str(1000000000, 9999999999))
    add_driver.backspace_all_and_input(add_driver.passport_by_input, "Верховный водилокомандующий")
    add_driver.backspace_all_and_input(add_driver.passport_code_input,
                                       base.random_value_float_str(100000, 999999), click_first=True)
    add_driver.backspace_all_and_input(add_driver.license_id_input,
                                       base.random_value_float_str(1000000000, 9999999999), click_first=True)
    add_driver.backspace_all_and_input(add_driver.contact_phone_input,
                                       base.random_value_float_str(9650000000, 9659999999), click_first=True)
    add_driver.backspace_all_and_input(add_driver.reg_address_input, "Мой адрес – Тирана")
    add_driver.backspace_all_and_input(add_driver.fact_address_input, "Мой адрес – Албания.")
    add_driver.click_button(add_driver.sanitary_book_toggl)
    add_driver.click_button(add_driver.sanitary_book_date_input_close)
    add_driver.input_in_field(add_driver.sanitary_book_date_input_open, '10102045')
    # Сохранение изменений
    add_driver.click_button(add_driver.save_button, do_assert=True)
    add_driver.click_button(add_driver.ok_button, wait="form")
    
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Создание и редактирование водителей')
@allure.description('ЛКЭ. Тест создания и редактирование внутреннего водителя Экспедитора: '
                    '1) создаем: ФИО - ФИО-timestamp, паспорт/права - РФ/РФ, № паспорт/код/права/тлф.апп/тлф. - Рандом,'
                    ' книжка - Нет.'
                    '2) редактируем: ФИО - ФИО-timestamp, паспорт/права - РФ/Другой, выдал - Кто-то, город - Другой, '
                    '№ паспорт/код/права/тлф.апп/тлф. - Рандом, книжка - Да.')
def test_inner_driver_edit_lke(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку водителей
    sidebar.move_and_click(move_to=sidebar.directories_hover, click_to=sidebar.drivers_list_button,
                           do_assert=True, wait="lst")
    
    driver_list = DriverList(base.driver)
    # Клик по кнопке добавления водителя
    driver_list.click_button(driver_list.add_driver_button, wait="form")
    
    add_driver = DriverAdd(base.driver)
    # Создание нового водителя
    surname = add_driver.add_base_inner_driver()
    
    # Поиск и выбор созданного водителя по фамилии
    driver_list.input_in_field(driver_list.surname_filter, value=surname, wait="lst")
    driver_list.click_button(driver_list.first_driver_link, wait="form")
    
    # Редактирование данных водителя
    add_driver.click_button(add_driver.driver_edit_button, wait="form")
    add_driver.backspace_all_and_input(add_driver.surname_input, f"ВФ-{base.get_timestamp()}")
    add_driver.backspace_all_and_input(add_driver.name_input, f"ВИ-{base.get_timestamp()}")
    add_driver.backspace_all_and_input(add_driver.patronymic_input, f"ВО-{base.get_timestamp()}")
    add_driver.backspace_all_and_input(add_driver.passport_id_input,
                                       base.random_value_float_str(1000000000, 9999999999))
    add_driver.backspace_all_and_input(add_driver.passport_by_input, "Верховный водилокомандующий")
    add_driver.backspace_all_and_input(add_driver.passport_code_input,
                                       base.random_value_float_str(100000, 999999), click_first=True)
    add_driver.click_button(add_driver.license_toggl)
    add_driver.input_in_field(add_driver.license_issued_by_input, "Кто-то")
    add_driver.input_in_field(add_driver.license_issued_please_input, "Другой")
    add_driver.input_in_field(add_driver.license_issued_date_input, "10102010")
    add_driver.backspace_all_and_input(add_driver.license_id_input,
                                       base.random_value_float_str(1000000000, 9999999999), click_first=True)
    add_driver.backspace_all_and_input(add_driver.contact_phone_input,
                                       base.random_value_float_str(9650000000, 9659999999), click_first=True)
    add_driver.backspace_all_and_input(add_driver.reg_address_input, "Мой адрес – Другой.")
    add_driver.backspace_all_and_input(add_driver.fact_address_input, "Мой адрес – Другой.")
    add_driver.click_button(add_driver.sanitary_book_toggl)
    add_driver.click_button(add_driver.sanitary_book_date_input_close)
    add_driver.input_in_field(add_driver.sanitary_book_date_input_open, '10102045')
    # Сохранение изменений
    add_driver.click_button(add_driver.save_button, do_assert=True)
    add_driver.click_button(add_driver.ok_button, wait="form")
    
    sidebar.test_finish()

    