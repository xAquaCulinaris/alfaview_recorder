#!/usr/bin/python3
import time
import pyautogui
import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from image_recognition import find_button

# ------Config---------
displayName = 'Marian Stucke'
roomNumber = 2
# --------------------


def open_browser():
    driver = webdriver.Chrome('/home/marian/Programming/alfaview/chromedriver')
    driver.get('https://app.alfaview.com/#/join/hochschule-furtwangen-furtwangen-university/5fa8632d-b4d7-44c4-9b1b-c88960333589/7200232b-a57a-46dc-9436-ffa1f61a3d00')

    time.sleep(2)

    name_field = driver.find_element_by_name('displayName')
    name_field.clear()
    name_field.send_keys(displayName)
    name_field.send_keys(Keys.ENTER)

    time.sleep(2)

    # find checkbox an click it
    terms_checkbox_list = driver.find_elements_by_name('acceptedTerms')
    for terms_checkbox in terms_checkbox_list:
        if terms_checkbox.get_attribute('type') == 'checkbox':
            terms_checkbox.click()

    # find second checkbox and click it
    privacy_checkbox_list = driver.find_elements_by_name('acceptedPrivacy')
    for privacy_checkbox in privacy_checkbox_list:
        if privacy_checkbox.get_attribute('type') == 'checkbox':
            privacy_checkbox.click()

    enter_button = driver.find_element_by_xpath("/html/body/div[@id='app']/div[@class='v-dialog__content v-dialog__content--active']/div[@class='v-dialog v-dialog--active']/div[@class='av-panel-wrapper']/div[@class='av-panel radius-large']/div[@class='av-panel__content']/div[@class='px-5 pt-4 av-guest-join__dialog-bottom-padding text-xs-center']/div[@class='px-3']/a[@class='button-min-width-x-large mt-4 v-btn v-btn--depressed v-btn--round theme--light av-button av-button--primary']")
    enter_button.click()

    # close browser
    time.sleep(2)
    open_alfaview()

    time.sleep(5)
    driver.quit()


def open_alfaview():
    print("opening alfaview")

    open_button = cv2.imread('buttons_to_find/open_button.png')
    skip_update_button = cv2.imread('buttons_to_find/skip_update_button.png')
    join_rooom_button = cv2.imread('buttons_to_find/join_room_button.png')




    pyautogui.screenshot("screenshot1.png")
    screenshot1 = cv2.imread('screenshot1.png')
    cord1 = find_button(screenshot1, open_button, 'result1.png')
    pyautogui.click(cord1[0], cord1[1])
    time.sleep(1)

    pyautogui.screenshot("screenshot2.png")
    screenshot2 = cv2.imread('screenshot2.png')
    cord2 = find_button(screenshot2, skip_update_button, 'result2.png')
    pyautogui.click(cord2[0], cord2[1])
    time.sleep(1)

    pyautogui.screenshot("screenshot3.png")
    screenshot3 = cv2.imread('screenshot3.png')
    cord3 = find_button(screenshot3, join_rooom_button, 'result3.png')
    pyautogui.click(cord3[0], cord3[1])
    time.sleep(1)



def close_alfaview():
    print("closing alfaview")
    pyautogui.click(3824, 1098)




def main():
    open_browser()


if __name__ == '__main__':
    main()
