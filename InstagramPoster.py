from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import autoit as ait
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

mobile_emulation = {"deviceName": "iPad Air"}
chrome_options = Options()
# chrome_options.add_argument("window-size=1200x600")  # problems with clicking some buttons bc they're out of view
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.instagram.com')
driver.implicitly_wait(3)

# ENTER YOUR USERNAME AND PASSWORD HERE
username = ""
password = ""
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys(username)

password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys(password)

login_button = driver.find_elements(By.TAG_NAME, 'button')[1]  # [0] is Show/Hide button for password
login_button.click()
print("Pressed: Log In ")

not_now = driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
not_now.click()
print("Pressed: Not Now")

if len(driver.find_elements(By.CLASS_NAME, "_a9-- _a9_1")) > 0:
    not_again = driver.find_element(By.CLASS_NAME, "_a9-- _a9_1")
    not_again.click()
    print("Pressed: Another Not Now")

# cancel_home = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]").click()

if len(driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")) > 0:
    not_again = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
    not_again.click()
    print("Pressed: Just Another Not Now")

# https://stackoverflow.com/a/50912377

button_new_post = driver.find_element(By.CSS_SELECTOR, '[aria-label="New post"]')
button_new_post.click()
print("Pressed: New Post")
c = 0  # Wait till two buttons appear up, so we safely select the Select From Device button
while c == 0:
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    if len(buttons) > 1:
        c = 1
button_select_from_device = buttons[1]
button_select_from_device.click()
print("Pressed: Select From Device")

handle = "[CLASS:#32770; TITLE:Open]"
ait.win_wait(handle, 60)
ait.control_set_text(handle, "Edit1", r"C:\Users\MEMEPOSTERDIRECTORY\memeposter\assets\hot.png")
ait.control_click(handle, "Button1")
print("Pressed: Open (Upload File)")
# https://stackoverflow.com/a/50912377

next_button = driver.find_element(By.XPATH, '//*[@role="button"][contains(text(), "Next")]').click()
print("Pressed: Next")
next_button2 = driver.find_element(By.XPATH, '//*[@role="button"][contains(text(), "Next")]').click()
print("Pressed: Next")

text_area = driver.find_element(By.CSS_SELECTOR, '[role="textbox"]')
text_file = open(r'C:/Users/MEMEPOSTERDIRECTORY/memeposter/assets/title.txt', 'r+')
post_text = text_file.readline()
text_area.send_keys(
    post_text + '\nENTER MORE TEXT HERE IF WISHED")

share_button = driver.find_element(By.XPATH, '//*[@role="button"][contains(text(), "Share")]').click()
print("Pressed: Share")
# https://stackoverflow.com/a/9188374

sleep(5)  # Make sure the post is shared

driver.close()
