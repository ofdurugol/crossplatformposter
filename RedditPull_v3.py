# Change Log V2
#
# Fixed the issue of i.redd.it links not opening properly on some connections by getting img directly from
# grid view of posts.


def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import urllib.request

    driver = webdriver.Chrome('./assets/chromedriver')
    driver.get("https://www.reddit.com/r/dankmemes/")
    driver.implicitly_wait(10)

    rank = 1
    media_div = driver.find_elements(By.XPATH, '//div[@data-click-id="media"]')[rank]
    title_div = media_div.find_element(By.XPATH, '../..//div[@theme="[object Object]"]')

    if len(media_div.find_elements(By.TAG_NAME, 'video')) > 0:
        media_div = driver.find_elements(By.XPATH, '//div[@data-click-id="media"]')[rank+1]
        title_div = media_div.find_element(By.XPATH, '../..//div[@theme="[object Object]"]')

    media = media_div.find_element(By.TAG_NAME, 'img')
    src = media.get_attribute('src')
    # https://stackoverflow.com/a/17362187
    urllib.request.urlretrieve(src, "./assets/hot.png")

    post_title = title_div.find_element(By.TAG_NAME, 'h3')
    title_text = post_title.text

    text_file = open('./assets/title.txt', 'r+')
    text_file.truncate(0)
    text_file.write(title_text)
    text_file.close()

    driver.close()


if __name__ == '__main__':
    main()


# https://stackoverflow.com/a/14573061
