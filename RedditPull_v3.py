# Change Log V2
#
# Fixed the issue of i.redd.it links not opening properly on some connections by getting img directly from
# grid view of posts.


def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    import urllib.request

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # keep driver open if an exception throws up
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.reddit.com/r/dankmemes/")
    driver.implicitly_wait(3)

    rank = 2
    titles = driver.find_elements(By.CSS_SELECTOR, '[slot="title"]')
    title_text = titles[rank].text
    print("Title: ", title_text)

    ''' WHAT IF IT'S A VIDEO
    if len(media_div.find_elements(By.TAG_NAME, 'video')) > 0:
        media_div = driver.find_elements(By.XPATH, '//div[@data-click-id="media"]')[rank+1]
        title_div = media_div.find_element(By.XPATH, '../..//div[@theme="[object Object]"]')
    '''

    media = driver.find_elements(By.CSS_SELECTOR, '[content-href]')[rank]
    src = media.get_attribute('content-href')
    print('src: ', src)
    # https://stackoverflow.com/a/17362187
    urllib.request.urlretrieve(src, "./assets/hot.png")

    text_file = open('./assets/title.txt', 'r+')
    text_file.truncate(0)
    text_file.write(title_text)
    text_file.close()

    driver.close()


if __name__ == '__main__':
    main()


# why use main()? https://stackoverflow.com/a/14573061
