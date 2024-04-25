import time
import allure
from tests.base_test import base_test_with_login
from pages.tariff_ftl_add_page import FTLTariffAdd
from pages.tariff_ltl_add_page import LTLTariffAdd
from pages.tariff_luo_add_page import LUOTariffAdd
from pages.tariffs_list_page import TariffsList


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Копирование тарифов')
@allure.description('ЛКЗ. Тест удаления тарифа: тариф - Первый в списке')
def test_tariff_delete_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.click_button(tariff_list.first_tariff_link, wait="form")

    tariff = FTLTariffAdd(base.driver)
    tariff.click_button(tariff.delete_tariff_button, do_assert=True)
    tariff.click_button(tariff.confirm_button, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Копирование тарифов')
@allure.description('ЛКЗ. Тест копирования ПРР тарифа: фильтр - ПРР, название - ПРР-timestamp, '
                    'спец. - Старый, минималка/доплата/МКАД - Рандом, оригинал - Удалть')
def test_tariff_luo_copy_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.input_in_field(tariff_list.tariff_name_filter, "ПРР", wait="lst")
    time.sleep(2)
    tariff_list.click_button(tariff_list.first_tariff_link, wait="form")

    tariff = LUOTariffAdd(base.driver)
    tariff.click_button(tariff.action_menu_button)
    tariff.click_button(tariff.copy_tariff_button, wait="form")
    tariff.backspace_len_and_input(tariff.tariff_name_input, f"ПРР-{base.get_timestamp()}")
    tariff.click_button(tariff.price_input)
    tariff.backspace_len_and_input(tariff.params_input, base.random_value_int_str(2500, 4000))
    tariff.click_button(tariff.price_hour_input)
    tariff.backspace_len_and_input(tariff.params_input, base.random_value_int_str(500, 1000))
    tariff.click_button(tariff.price_mrr_input)
    tariff.backspace_len_and_input(tariff.params_input, base.random_value_int_str(100, 500))
    tariff.click_button(tariff.add_tariff_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button, do_assert=True, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Копирование тарифов')
@allure.description('ЛКЗ. Тест копирования FTL тарифа: фильтр - ПЧ, тип - Почасовой, округление - Час, '
                    'название - ПЧ-timestamp, ТС - Старый, кузов - Старый, минималка - Рандом')
def test_tariff_ftl_h_copy_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.input_in_field(tariff_list.tariff_name_filter, "ПЧ", wait="lst")
    time.sleep(2)
    tariff_list.click_button(tariff_list.first_tariff_link, wait="form")

    tariff = FTLTariffAdd(base.driver)
    tariff.click_button(tariff.action_menu_button)
    tariff.click_button(tariff.copy_tariff_button, wait="form")
    tariff.backspace_len_and_input(tariff.tariff_name_input, f"ПЧ-{base.get_timestamp()}")
    tariff.click_button(tariff.price_input)
    tariff.backspace_len_and_input(tariff.hourly_params_input, base.random_value_int_str(3000, 5000))
    tariff.click_button(tariff.add_hourly_tariff_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button, do_assert=True, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Копирование тарифов')
@allure.description('ЛКЭ. Тест копирования FTL тарифа: фильтр - ГГ, тип - Фиксированный, маршрут - Старый, название '
                    '- ГГ-timestamp, ТС - Старый, кузов - Старый, минималка/доп.адрес/ожидание - Рандом')
def test_tariff_ftl_cc_copy_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.input_in_field(tariff_list.tariff_name_filter, "ГГ", wait="lst")
    time.sleep(2)
    tariff_list.click_button(tariff_list.first_tariff_link, wait="form")

    tariff = FTLTariffAdd(base.driver)
    tariff.click_button(tariff.action_menu_button)
    tariff.click_button(tariff.copy_tariff_button, wait="form")
    tariff.backspace_len_and_input(tariff.tariff_name_input, f"ГГ-{base.get_timestamp()}")
    tariff.click_button(tariff.price_input)
    tariff.backspace_len_and_input(tariff.fixed_params_input, base.random_value_int_str(5000, 10000))
    tariff.click_button(tariff.address_cost_input)
    tariff.backspace_len_and_input(tariff.fixed_params_input, base.random_value_int_str(1000, 3000))
    tariff.click_button(tariff.free_downtime_input)
    tariff.backspace_len_and_input(tariff.fixed_params_input, base.random_value_int_str(10, 60))
    tariff.click_button(tariff.add_fm_tariff_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button, do_assert=True, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Копирование тарифов')
@allure.description('ЛКЗ. Тест копирования FTL тарифа: фильтр - ПБ, тип - Пробег, маршрут - Старый, '
                    'название - ПБ-timestamp, ТС - Старый, кузов - Старый, минималка/доп.адрес/ожидание - Рандом')
def test_ftl_ml_tariff_copy_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.input_in_field(tariff_list.tariff_name_filter, "ПБ", wait="lst")
    time.sleep(2)
    tariff_list.click_button(tariff_list.first_tariff_link, wait="form")

    tariff = FTLTariffAdd(base.driver)
    tariff.click_button(tariff.action_menu_button)
    tariff.click_button(tariff.copy_tariff_button, wait="form")
    tariff.backspace_len_and_input(tariff.tariff_name_input, f"ПБ-{base.get_timestamp()}")
    tariff.click_button(tariff.extra_mileage_input)
    tariff.backspace_len_and_input(tariff.mileage_params_input, base.random_value_int_str(10, 50))
    tariff.click_button(tariff.address_cost_input)
    tariff.backspace_len_and_input(tariff.mileage_params_input, base.random_value_int_str(1000, 3000))
    tariff.click_button(tariff.free_downtime_input)
    tariff.backspace_len_and_input(tariff.mileage_params_input, base.random_value_int_str(10, 60))
    tariff.click_button(tariff.add_min_price_button)
    tariff.backspace_len_and_input(tariff.mileage_params_input, base.random_value_int_str(2500, 10000))
    tariff.click_button(tariff.add_confirm_button)
    tariff.backspace_len_and_input(tariff.mileage_params_input, base.random_value_int_str(10, 30))
    tariff.backspace_len_and_input(tariff.mileage_params_input_2, base.random_value_int_str(1, 5))
    tariff.backspace_len_and_input(tariff.mileage_params_input_3, base.random_value_int_str(10, 60))
    tariff.click_button(tariff.add_fm_tariff_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button)
    tariff.click_button(tariff.confirm_button, do_assert=True, wait="lst")

    sidebar.finish_test()


@allure.epic("Стабильные тесты")
@allure.story("Extended test")
@allure.feature('Копирование тарифов')
@allure.description('ЛКЗ. Тест копирования LTL тарифа: фильтр - LTL, название - LTL-timestamp, тип - Старый, '
                    'мин.вес/объем вес/сбор прям./сбор обр. - Рандом, регион - Старый, '
                    'минималка/доплата/темп.коэф/срок - Рандом')
def test_tariff_ltl_copy_lkz(domain):
    base, sidebar = base_test_with_login(domain=domain, role='lkz')

    sidebar.move_find_and_click(move_to=sidebar.directories_hover, click_to=sidebar.tariffs_list_button,
                                do_assert=True, wait="lst")

    tariff_list = TariffsList(base.driver)
    tariff_list.input_in_field(tariff_list.tariff_name_filter, "LTL", wait="lst")
    time.sleep(2)
    tariff_list.click_button(tariff_list.first_tariff_link, wait="form")

    tariff = LTLTariffAdd(base.driver)
    tariff.click_button(tariff.action_menu_button)
    tariff.click_button(tariff.copy_tariff_button, wait="form")
    tariff.backspace_len_and_input(tariff.min_weight_input, base.random_value_int_str(10, 100))
    tariff.backspace_len_and_input(tariff.volumetric_weight_input, base.random_value_int_str(10, 100))
    tariff.backspace_len_and_input(tariff.direct_price_input, base.random_value_int_str(100, 500))
    tariff.backspace_len_and_input(tariff.reverse_price_input, base.random_value_int_str(100, 500))
    tariff.backspace_len_and_input(tariff.min_price_input, base.random_value_int_str(1000, 3000))
    tariff.backspace_len_and_input(tariff.kg_price_input, base.random_value_int_str(50, 200))
    tariff.backspace_len_and_input(tariff.temp_coeff_input, base.random_value_float_str(1.0, 5.0))
    tariff.backspace_len_and_input(tariff.delivery_time_input, base.random_value_int_str(5, 50))
    tariff.click_button(tariff.add_tariff_button)
    tariff.click_button(tariff.confirm_button, do_assert=True, wait="lst")

    sidebar.finish_test()
