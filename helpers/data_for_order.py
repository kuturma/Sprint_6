from locators.locators_order_page import ForWhoScooterPageLocators, AboutRentPageLocators

for_who = ForWhoScooterPageLocators()
about_rent = AboutRentPageLocators()

class User1ForWho:
    name = 'Антон'
    last_name = 'Кутурмин'
    address = 'Московская обл, г Люберцы, ул Инициативная, д 10В'
    metro_station = for_who.CHOICE_METRO_STATION_TAGANSKAYA
    phone_number = '+79999999999'
    date_order = '16.06.2025'
    coice_date = about_rent.CHOICE_DATE_16_06_2025
    rental_period = about_rent.CHOICE_DAY
    color = about_rent.COLOR_FIELD_BLACK_SWAN
    comment = 'Пожалуйста, позвоните мне перед доставкой'

class User2ForWho:
    name = 'Фарух'
    last_name = 'Кизлэр'
    address = 'Москва, ул Каланчевская, д 35'
    metro_station = for_who.CHOICE_METRO_STATION_KOMSOMOLSKAYA
    phone_number = '+71111111111'
    date_order = '17.06.2025'
    coice_date = about_rent.CHOICE_DATE_17_06_2025
    rental_period = about_rent.CHOICE_TWO_DAY
    color = about_rent.COLOR_FIELD_SILVER_DESPAIR
    comment = 'Пожалуйста, подберите мне самый красивый'