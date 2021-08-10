from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
import time

#specify the path to chromedriver.exe (download and save on your computer)
browser = webdriver.Chrome('/Users/intisarmuhammad//Downloads/atom/chromedriver')

#open the webpage
browser.get("http://www.instagram.com")

#target username
username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("star_datascience")
password.clear()
password.send_keys("Tauheedah13$")

#target the login button and click it
button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

#Alerts
time.sleep(5)
alert = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
alert2 = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

def insta_details(urls):
    """Take a post url and return post details"""
    #browser = webdriver.Chrome('/Users/intisarmuhammad//Downloads/atom/chromedriver')
    post_details = []
    for link in urls:
        browser.get(link)
        age = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/div[2]/a/time').get_attribute('datetime')
        # xpath_comment = '/html/body/div[5]/div[2]/div/article/div[3]/div[1]'
        try:
            comment = browser.find_element_by_class_name('C4VMK').text
        except:
            comment = 'None'

        #likes = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div[2]/a/span')
        try:
            likes = browser.find_element_by_partial_link_text(' likes').text
            #likes = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[2]/div/div[2]/a').text
        except:
            likes = "None"
        insta_link = link.replace('https://www.instagram.com/p','')
        post_details.append({'username': comment.partition('\n')[0], 'link': link, 'likes': likes, 'age': age, 'caption': comment})
        #time.sleep(3)

    return post_details
all_links = ['https://www.instagram.com/p/CLFdqmrJU69/', 'https://www.instagram.com/p/CN58-k-pNZC/', 'https://www.instagram.com/p/CN0HqOQpeAu/', 'https://www.instagram.com/p/CNmyb0LJcgc/', 'https://www.instagram.com/p/CNYrkT1JmKv/', 'https://www.instagram.com/p/CNNlBO2JKi9/', 'https://www.instagram.com/p/CM0HODGpFbP/', 'https://www.instagram.com/p/CMrymb5J6fN/', 'https://www.instagram.com/p/CMh-ylKJPED/', 'https://www.instagram.com/p/CMfpvB9JQYh/', 'https://www.instagram.com/p/CN-nL0hBm2H/', 'https://www.instagram.com/p/CN8IZQOhY6p/', 'https://www.instagram.com/p/CN29KYgBure/', 'https://www.instagram.com/p/CNk9ANphkcU/', 'https://www.instagram.com/p/CNiXI0OBOk2/', 'https://www.instagram.com/p/CNaof6Nh27H/', 'https://www.instagram.com/p/CNYEG8YBAjK/', 'https://www.instagram.com/p/CNNvGMgB8H9/', 'https://www.instagram.com/p/CNImkCEJAaw/', 'https://www.instagram.com/p/CNVnZCILW80/', 'https://www.instagram.com/p/CNIxl_ergYP/', 'https://www.instagram.com/p/CMa4wbtLLz9/', 'https://www.instagram.com/p/CMFon0Qs8B-/', 'https://www.instagram.com/p/CL-YSVpsJYf/', 'https://www.instagram.com/p/CL5EnT4LRMm/', 'https://www.instagram.com/p/CL0F7H5LTiN/', 'https://www.instagram.com/p/CLzl8umLTyb/', 'https://www.instagram.com/p/CLuucm8L4BG/', 'https://www.instagram.com/p/COGhNBrJdet/', 'https://www.instagram.com/p/COD3DcdJOnk/', 'https://www.instagram.com/p/CNnUX31pRRn/', 'https://www.instagram.com/p/CNfsOAupMZn/', 'https://www.instagram.com/p/CNVUoUVJtaP/', 'https://www.instagram.com/p/CNNtZUNp0cP/', 'https://www.instagram.com/p/CNAzlk8pAI-/', 'https://www.instagram.com/p/CM7xFmPJZS2/', 'https://www.instagram.com/p/CM2mL2YpCUU/', 'https://www.instagram.com/p/COGGk3grmAc/', 'https://www.instagram.com/p/CNp9gG8rrLc/', 'https://www.instagram.com/p/CNkrc7SLbwY/', 'https://www.instagram.com/p/CNh47K5j2iC/', 'https://www.instagram.com/p/CNfOGqELIyz/', 'https://www.instagram.com/p/CNXk5DID_--/', 'https://www.instagram.com/p/CNU7JCgLVB_/', 'https://www.instagram.com/p/CNSpC7NL85w/', 'https://www.instagram.com/p/CNKs991ra05/', 'https://www.instagram.com/p/CMPmA1QpcJ9/', 'https://www.instagram.com/p/CL1pbfyqQ3b/', 'https://www.instagram.com/p/CJWRao7Jqq5/', 'https://www.instagram.com/p/CIV1iufJP4_/', 'https://www.instagram.com/p/CH-rII7pF2u/', 'https://www.instagram.com/p/CH28leSJ2iC/', 'https://www.instagram.com/p/CH0ZB1qpT2J/', 'https://www.instagram.com/p/CHxzGTwp2OH/', 'https://www.instagram.com/p/CHspkM1p0QV/', 'https://www.instagram.com/p/COGh3EYhfmA/', 'https://www.instagram.com/p/CN_jChYB4w_/', 'https://www.instagram.com/p/CN4AfXPBwv8/', 'https://www.instagram.com/p/CN3g9H7hdQo/', 'https://www.instagram.com/p/CN2w4SMBzcG/', 'https://www.instagram.com/p/CN1vRhqBaTe/', 'https://www.instagram.com/p/CN0hJq4h9Tr/', 'https://www.instagram.com/p/CNsip6oBdKf/', 'https://www.instagram.com/p/COBztTKJYXb/', 'https://www.instagram.com/p/CNsLrV5JUAR/', 'https://www.instagram.com/p/CNfs_8CpAFc/', 'https://www.instagram.com/p/CNN_--HpYOI/', 'https://www.instagram.com/p/CMyO_hRpp86/', 'https://www.instagram.com/p/CMbGniRJ1lA/', 'https://www.instagram.com/p/CMQFCLJpIAl/', 'https://www.instagram.com/p/CLzriGtJjgY/', 'https://www.instagram.com/p/CLX0x1jJdpU/', 'https://www.instagram.com/p/CN0SCFhnBKE/', 'https://www.instagram.com/p/CNqAJSInbU8/', 'https://www.instagram.com/p/CNk5rHxHMCh/', 'https://www.instagram.com/p/CNQWiadHKcT/', 'https://www.instagram.com/p/CNLD4R-njLM/', 'https://www.instagram.com/p/CNDYJKjnMzI/', 'https://www.instagram.com/p/CNA1CoTnd9F/', 'https://www.instagram.com/p/CM0JjwjHeaM/', 'https://www.instagram.com/p/CMxeV78nZtU/', 'https://www.instagram.com/p/COEXQDuAjZv/', 'https://www.instagram.com/p/CN5bP9fAgrc/', 'https://www.instagram.com/p/CN5YUtDgBwz/', 'https://www.instagram.com/p/CN3xiR9gVIk/', 'https://www.instagram.com/p/CN3g5MWgEZN/', 'https://www.instagram.com/p/CNyMoVOgWw5/', 'https://www.instagram.com/p/CNvpNmDLAxl/', 'https://www.instagram.com/p/CNth11SAv7H/', 'https://www.instagram.com/p/CNtMjxTAAXS/', 'https://www.instagram.com/p/CNmlDUvAnFo/', 'https://www.instagram.com/p/CNZsUIRgAfD/', 'https://www.instagram.com/p/CNRtYjeAa02/', 'https://www.instagram.com/p/CMmCj_Dg8UB/', 'https://www.instagram.com/p/CL1HBPGAnWD/', 'https://www.instagram.com/p/CLJM4b1AAC1/', 'https://www.instagram.com/p/CK0yk1ugMnY/', 'https://www.instagram.com/p/CKgIr0JAw6S/', 'https://www.instagram.com/p/CJ-j7IXAdA2/', 'https://www.instagram.com/p/COGxU-wJbi_/', 'https://www.instagram.com/p/COB6uPDpo3G/', 'https://www.instagram.com/p/COBzVSdJfrM/', 'https://www.instagram.com/p/CN_aHHfpeKu/', 'https://www.instagram.com/p/CN_Jt4JJ-jW/', 'https://www.instagram.com/p/CN5_sxTp_WI/', 'https://www.instagram.com/p/CN5twqapSWy/', 'https://www.instagram.com/p/CN3YYO5Jbv3/', 'https://www.instagram.com/p/CN3Lx6Yp-xw/']
print(len(all_links))


ig_data = insta_details(all_links)
print(ig_data)
#insta_scrape = pd.DataFrame(ig_data)
#print(insta_scrape.head())
#insta_scrape.to_csv('/Users/intisarmuhammad/Downloads/final_project.csv')
