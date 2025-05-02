from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import pytest
import logging
import json
import time
import data

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Recuperar código de confirmación

def retrieve_phone_code(driver) -> str:
    code = None
    for _ in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message") and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if code:
            return code
    raise Exception("No se encontró el código de confirmación del teléfono.")

# Página principal de Urban Routes

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from_address(self, from_address):
        from_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "from")))
        from_input.clear()
        from_input.send_keys(from_address)

    def set_to_address(self, to_address):
        to_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "to")))
        to_input.clear()
        to_input.send_keys(to_address)

    def set_route(self, from_address, to_address):
        self.set_from_address(from_address)
        self.set_to_address(to_address)

    def select_comfort_tariff(self):
        comfort_tariff = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='tariff-button' and .//div[text()='Comfort']]"))
        )
        comfort_tariff.click()

    def enter_phone_number(self, phone):
        phone_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "phone")))
        phone_input.clear()
        phone_input.send_keys(phone)
        send_code_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Enviar código')]"))
        )
        send_code_button.click()

    def enter_confirmation_code(self, code):
        code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "code")))
        code_input.send_keys(code)
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirmar')]"))
        )
        confirm_button.click()

    def add_credit_card(self, card_number, card_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Agregar tarjeta')]"))
        ).click()

        number_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "number")))
        number_input.clear()
        number_input.send_keys(card_number)

        code_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "code")))
        code_input.clear()
        code_input.send_keys(card_code)
        code_input.send_keys(Keys.TAB)

        link_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Enlace')]"))
        )
        link_button.click()

    def write_message_for_driver(self, message):
        message_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "comment")))
        message_input.clear()
        message_input.send_keys(message)

    def request_blanket_and_tissues(self):
        blanket_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Manta')]"))
        )
        blanket_checkbox.click()

        tissues_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Pañuelos')]"))
        )
        tissues_checkbox.click()

    def request_ice_cream(self, quantity=2):
        plus_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Helado')]/following-sibling::div//button[contains(., '+')]"))
        )
        for _ in range(quantity):
            plus_button.click()

    def get_from_address(self):
        return self.driver.find_element(By.ID, "from").get_attribute("value")

    def get_to_address(self):
        return self.driver.find_element(By.ID, "to").get_attribute("value")

# Clase de prueba
class TestUrbanRoutes:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_user_can_order_taxi(self):
        self.driver.get(data.urban_routes_url)
        page = UrbanRoutesPage(self.driver)

        page.set_route(data.address_from, data.address_to)
        page.select_comfort_tariff()
        page.enter_phone_number(data.phone_number)

        code = retrieve_phone_code(self.driver)
        page.enter_confirmation_code(code)

        page.add_credit_card(data.card_number, data.card_code)
        page.write_message_for_driver(data.message_for_driver)
        page.request_blanket_and_tissues()
        page.request_ice_cream()

        assert page.get_from_address() == data.address_from
        assert page.get_to_address() == data.address_to
