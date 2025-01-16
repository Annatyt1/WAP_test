import time
import allure
from wap_func import start_driver, get_url, click_element, input_keys, get_screen_size, swipe_screen, select_streamer, screenshot, stop_driver


@allure.title("Test twitch mobile")
@allure.description("This test is for Twitch mobile WAP")
def test_wap():

    driver = start_driver()
    get_url(driver, "https://m.twitch.tv/")

    click_element(driver, "search_icon")

    time.sleep(1)

    click_element(driver, "search_box")

    time.sleep(1)

    click_element(driver, "input")

    input_keys(driver, "input", "StarCraft II")

    time.sleep(1)

    click_element(driver, "select")

    time.sleep(1)

    start_x, start_y, end_x, end_y = get_screen_size(driver)

    for i in range(2):
        swipe_screen(driver, start_x, start_y, end_x, end_y)

    select_streamer(driver, "select_streamer")

    time.sleep(5)

    screenshot(driver, "screenshot.png")

    time.sleep(3)

    stop_driver(driver)
