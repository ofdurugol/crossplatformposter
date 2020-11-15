from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import autoit
import time

mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options, executable_path='./assets/chromedriver')

driver.get('https://www.instagram.com')
driver.implicitly_wait(10)

jump_to_login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]').click()

username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys('Insert Your Username')

password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('Insert Your Password')

login_button = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

not_now1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

cancel_home = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()

if len(driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")) > 0:
    driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

# https://stackoverflow.com/a/50912377

ActionChains(driver).move_to_element(
    driver.find_element(By.XPATH, '//div[@data-testid="new-post-button"]')).click().perform()
handle = "[CLASS:#32770; TITLE:Open]"
autoit.win_wait(handle, 60)
autoit.control_set_text(handle, "Edit1", r"C:\Users\GrainsBrains\PycharmProjects\AutomatedInstagramPoster\assets\hot"
                                         r".png")
autoit.control_click(handle, "Button1")

# https://stackoverflow.com/a/50912377

next_button = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]').click()

text_area = driver.find_element(By.CLASS_NAME, '_472V_')
text_file = open(r'C:/Users/GrainsBrains/PycharmProjects/AutomatedInstagramPoster/assets/title.txt', 'r+')
post_text = text_file.readline()
text_area.send_keys(
    post_text + '\nFollow: @angory.mario' + 6 * '\n.' + "\n#meme #memes #memesdaily #memestagram #memepage "
                                         "#memelord "
                                         "#memeoftheday #memeita #memesfordays #memesita #memeaccount "
                                         "#memesaremee #memer #memecucks #memegod #memeindonesia "
                                         "#memeinajah #memesespa #memedaily #memelife #memez "
                                         "#memecomicindonesia #memeitalia")

share_button = driver.find_element(By.XPATH, '//button[contains(text(), "Share")]').click()
# https://stackoverflow.com/a/9188374

time.sleep(5)

driver.close()
