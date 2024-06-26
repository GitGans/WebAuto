import time
import allure
from tests.base_test import base_test_with_login
from pages.cargo_place_add_page import CargoPlaceAdd
from pages.cargo_place_list_page import CargoPlaceList


@allure.story("Critical path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЭ. Тест маршрутизации ГМ ГВ: создаем - ГМ ГВ, маршрутизируем - ТС 20т/90м3/ 33пал')
def test_cargo_place_routing_lke(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lke'
    base, sidebar = base_test_with_login(domain=domain, role='lke')
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор владельца грузоместа "Auto LKZ"
    add_cp.dropdown_click_input_click(add_cp.cargo_place_owner_select, "Auto LKZ")
    # Выбор типа грузоместа "Короб"
    add_cp.dropdown_click_input_click(add_cp.lke_cp_type_select, "Короб")
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.input_in_field(add_cp.cp_quantity_input, add_cp.random_value_float_str(1, 10))
    add_cp.input_in_field(add_cp.cp_weight_input, add_cp.random_value_float_str(10, 20000))
    add_cp.input_in_field(add_cp.cp_value_input, add_cp.random_value_float_str(0.1, 35.0))
    add_cp.input_in_field(add_cp.cp_cost_input, add_cp.random_value_float_str(100, 1000000))
    # Выбор статуса грузоместа "Новое"
    add_cp.dropdown_click_input_click(add_cp.lke_cp_status_select, "Новое")
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод штрихкода грузоместа
    add_cp.input_in_field(add_cp.lke_bar_code_input, cp_stamp)
    # Ввод адресов отправления и доставки
    add_cp.dropdown_click_input_wait_enter(add_cp.departure_address_select, "Auto LKZ")
    add_cp.dropdown_click_input_wait_enter(add_cp.delivery_address_select, "Auto LKZ")
    # Клик по кнопке создания грузоместа
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")

    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор первого чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке маршрутизировать ГМ
    cp_list.click_button(cp_list.multi_route_button)
    # Выбор типа ТС для маршрутизации
    cp_list.dropdown_click_input_click(cp_list.vehicle_type_select, dd_index=2, option_text="20т / 90м3 / 33пал.")
    # Ввод кол-ва ТС для маршрутизации
    cp_list.input_in_field(cp_list.quantity_vehicle_input, "1")
    # Выбор временного периода для маршрутизации ГМ от сегодня
    cp_list.click_button(cp_list.calendar_picker_button)
    cp_list.click_button(cp_list.today_button)
    # Выбор временного периода для маршрутизации ГМ до сегодня + час
    new_time = cp_list.naw_time_change(60)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    time.sleep(1)
    cp_list.click_button(cp_list.today_button)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    cp_list.backspace_num_and_input(cp_list.calendar_input, num=5, value=new_time)
    cp_list.click_button(cp_list.calendar_ok_button)
    # Клик по кнопке отправить ГМ на маршрутизацию
    cp_list.click_button(cp_list.send_button, do_assert=True)
    # Подтверждение успешного отправления на маршрутизацию
    cp_list.click_button(cp_list.ok_button)

    # Завершение теста
    sidebar.test_finish()


@allure.story("Critical path test")
@allure.feature('Маршрутизация грузомест')
@allure.description('ЛКЗ. Тест маршрутизации ГМ: создаем - ГМ, маршрутизируем - ТС 20т/90м3/ 33пал')
def test_cargo_place_routing_lkz(domain):
    # Инициализация базовых объектов и авторизация под ролью 'lkz'
    base, sidebar = base_test_with_login(domain=domain, role='lkz')
    
    # Переход к списку грузомест
    sidebar.move_and_click(move_to=sidebar.assignments_hover, click_to=sidebar.cargo_place_list_button,
                           do_assert=True, wait="lst")
    time.sleep(1.5)
    cp_list = CargoPlaceList(base.driver)
    # Клик по кнопке добавления грузоместа
    cp_list.click_button(cp_list.add_cargo_place_button, wait="form")
    
    add_cp = CargoPlaceAdd(base.driver)
    # Выбор типа грузоместа "Короб"
    add_cp.dropdown_click_input_click(add_cp.lkz_cp_type_select, "Короб")
    # Ввод рандомизированных данных для количества, веса, объема и стоимости груза
    add_cp.input_in_field(add_cp.cp_quantity_input, add_cp.random_value_float_str(1, 10))
    add_cp.input_in_field(add_cp.cp_weight_input, add_cp.random_value_float_str(10, 20000))
    add_cp.input_in_field(add_cp.cp_value_input, add_cp.random_value_float_str(0.1, 35.0))
    add_cp.input_in_field(add_cp.cp_cost_input, add_cp.random_value_float_str(100, 1000000))
    # Выбор статуса грузоместа "Новое"
    add_cp.dropdown_click_input_click(add_cp.lkz_cp_status_select, "Новое")
    # Генерация уникального идентификатора для грузоместа
    cp_stamp = f"ГМ-{add_cp.get_timestamp()}"
    # Ввод штрихкода грузоместа
    add_cp.input_in_field(add_cp.lkz_bar_code_input, cp_stamp)
    # Ввод адресов отправления и доставки
    add_cp.dropdown_click_input_wait_enter(add_cp.departure_address_select, "Екатеринбург")
    add_cp.dropdown_click_input_wait_enter(add_cp.delivery_address_select, "Екатеринбург")
    # Клик по кнопке создания грузоместа
    add_cp.click_button(add_cp.create_cargo_place_button, do_assert=True)
    # Клик по кнопке подтверждения добавления
    add_cp.click_button(add_cp.confirm_add_button, wait="lst")
    
    cp_list = CargoPlaceList(base.driver)
    # Сброс фильтров
    cp_list.click_button(cp_list.reset_button, wait="lst")
    # Ввод штрихкода грузоместа в поле фильтрации
    cp_list.input_in_field(cp_list.barcode_filter, value=cp_stamp, wait="lst")
    # Клик по кнопке экшен меню
    cp_list.click_button(cp_list.action_menu_button)
    # Клик по кнопке мультивыбор ГМ
    cp_list.click_button(cp_list.multi_select_button)
    # Выбор первого чек-бокса
    cp_list.click_button(cp_list.cp_list_checkbox, index=3)
    # Клик по кнопке маршрутизировать ГМ
    cp_list.click_button(cp_list.multi_route_button)
    # Выбор типа ТС для маршрутизации
    cp_list.dropdown_click_input_click(cp_list.vehicle_type_select, dd_index=2, option_text="20т / 90м3 / 33пал.")
    # Ввод кол-ва ТС для маршрутизации
    cp_list.input_in_field(cp_list.quantity_vehicle_input, "1")
    # Выбор временного периода для маршрутизации ГМ от сегодня
    cp_list.click_button(cp_list.calendar_picker_button)
    cp_list.click_button(cp_list.today_button)
    # Выбор временного периода для маршрутизации ГМ до сегодня + час
    new_time = cp_list.naw_time_change(60)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    time.sleep(1)
    cp_list.click_button(cp_list.today_button)
    cp_list.click_button(cp_list.calendar_picker_button, index=2)
    cp_list.backspace_num_and_input(cp_list.calendar_input, num=5, value=new_time)
    cp_list.click_button(cp_list.calendar_ok_button)
    # Клик по кнопке отправить ГМ на маршрутизацию
    cp_list.click_button(cp_list.send_button, do_assert=True)
    # Подтверждение успешного отправления на маршрутизацию
    cp_list.click_button(cp_list.ok_button)
    
    # Завершение теста
    sidebar.test_finish()
    