import allure
import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


@allure.step
def get_yaml(file):
    with open(file, "r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


config_file = get_yaml("config.yaml")
xpath_file = get_yaml("xpath.yaml")


@allure.step
def start_driver():
    driver = webdriver.Remote(
        config_file["server_url"], options=UiAutomator2Options(
        ).load_capabilities(config_file["capabilities"]))
    return driver


@allure.step
def get_url(driver: webdriver.Remote, url: str):
    driver.get(url)
    return driver


@allure.step
def click_element(driver: webdriver.Remote, name: str):
    xpath = xpath_file[name]["xpath"]
    element = driver.find_element(By.XPATH, xpath)
    element.click()


@allure.step
def input_keys(driver: webdriver.Remote, name: str, text: str):
    xpath = xpath_file[name]["xpath"]
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)


@allure.step
def get_screen_size(driver: webdriver.Remote):
    screen_size = driver.get_window_size()
    screen_width = screen_size["width"]
    screen_height = screen_size["height"]

    start_x = screen_width * 0.5
    start_y = screen_height * 0.8
    end_x = start_x
    end_y = screen_height * 0.2
    return start_x, start_y, end_x, end_y


@allure.step
def swipe_screen(driver: webdriver.Remote, start_x, start_y, end_x, end_y, duration=3000):
    driver.swipe(start_x=start_x, start_y=start_y,
                 end_x=end_x, end_y=end_y, duration=duration)


@allure.step
def select_streamer(driver: webdriver.Remote, name: str):
    xpath = xpath_file[name]["xpath"]
    streamer = driver.find_elements(By.XPATH, xpath)
    streamer[0].click()


@allure.step
def screenshot(driver: webdriver.Remote, filename: str):
    driver.get_screenshot_as_file(filename)


@allure.step
def stop_driver(driver: webdriver.Remote):
    driver.quit()
