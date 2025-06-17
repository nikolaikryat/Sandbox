from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://hh.ru/applicant/resumes"
driver = webdriver.Chrome()

try:
    driver.get(link)

    input_mail = driver.find_element(By.CSS_SELECTOR, "#HH-React-Root > div > div.magritte-redesign > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div > div > div > div:nth-child(1) > div.magritte-icon-dynamic___KJ4yJ_11-0-7.magritte-icon-dynamic_full-width___vgWH5_11-0-7 > div > div > div:nth-child(3) > form > div.magritte-input___LVTID_7-2-13.magritte-large___9frRh_7-2-13 > div > div > div.magritte-content-container___s-0kX_7-2-13 > div.magritte-value-container___6ReT7_7-2-13 > input")
    input_mail.send_keys("nikolai.kryat@mail.ru")

    pass_button = driver.find_element(By.CSS_SELECTOR, "#HH-React-Root > div > div.magritte-redesign > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div > div > div > div:nth-child(1) > div.magritte-icon-dynamic___KJ4yJ_11-0-7.magritte-icon-dynamic_full-width___vgWH5_11-0-7 > div > div > div:nth-child(3) > form > div.account-login-actions.account-login-actions_column > div > a > div > span > span")
    pass_button.click()

    pass_input = driver.find_element(By.CSS_SELECTOR, "#HH-React-Root > div > div.magritte-redesign > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div > div > div > div:nth-child(1) > div.magritte-icon-dynamic___KJ4yJ_11-0-7.magritte-icon-dynamic_full-width___vgWH5_11-0-7 > div > div > form > div:nth-child(9) > div.magritte-position-container___kZnvZ_7-2-13 > div.magritte-hint-container___rGsD8_7-2-13 > div.magritte-content-container___s-0kX_7-2-13 > div.magritte-value-container___6ReT7_7-2-13 > input")
    pass_input.send_keys("qwerty19889")

    enter_button = driver.find_element(By.CSS_SELECTOR, "#HH-React-Root > div > div.magritte-redesign > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div > div > div > div > div > div:nth-child(1) > div.magritte-icon-dynamic___KJ4yJ_11-0-7.magritte-icon-dynamic_full-width___vgWH5_11-0-7 > div > div > form > div.account-login-actions.account-login-actions_column > button > div > span > span")
    enter_button.click()

    time.sleep(10)

    up_button = driver.find_element(By.CSS_SELECTOR, "#HH-React-Root > div > div.HH-MainContent.HH-Supernova-MainContent > div.main-content.main-content_broad-spacing > div > div > div.magritte-grid-row___3Zugo_2-2-25 > div.magritte-grid-column___rhP24_2-2-25.magritte-grid-column_xs-4___eVCYh_2-2-25.magritte-grid-column_s-8___vihhu_2-2-25.magritte-grid-column_m-8___EK0AC_2-2-25.magritte-grid-column_l-8___-hyNG_2-2-25.magritte-grid-column_xl-8___VT5-v_2-2-25.magritte-grid-column_xxl-8___XTTJ1_2-2-25 > div > div > div:nth-child(4) > div > div > div > div > div.magritte-card___bhGKz_7-0-17.magritte-card-style-primary___eZ6aX_7-0-17.magritte-card-shadow-level-0___RNbQK_7-0-17.magritte-card-stretched___0Uc0J_7-0-17.magritte-border-default___eT8Lg_7-0-17 > div.magritte-icon-dynamic___KJ4yJ_11-0-7.magritte-icon-dynamic_full-width___vgWH5_11-0-7 > div > div > div > div.footer--jyY20vQs7vcQkNMe > div.footer-buttons--NukbIBZcT4Q4fwhK > div > button > div")
    up_button.click()

finally:
    driver.quit()