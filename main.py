# FIX : 
#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver 

chrome_path = r"C:\Users\padam\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

def scrape(city , search_term):
    driver.get("https://www.justdial.com/" + city + "/" + search_term + "/page-3")
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        popup = driver.find_elements_by_xpath('//*[@id="best_deal_div"]/section/span')
        if( popup is True ):
            popup.click()
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    lists = driver.find_elements_by_class_name("cntanr")
    return lists


def get_data(list_url):
    driver.get(list_url)
    
    #Phone Details
    phone = driver.find_elements_by_xpath('//*[@id="comp-contact"]/span[2]/a')
    phone_keys = {'9d011' : '+' , '9d010' : '9' , '9d001' : '0' , '9d002' : '1' , '9d006' : '5' , '9d007' : '6' , '9d008': '7', '9d009' : '8' , '9d003' : '2' , '9d004' : 3 ,'9d005' : '4' }
    phone_no = []
    for index in range(4,14):
        
        x = driver.execute_script("return window.getComputedStyle(document.querySelector('#comp-contact > span.telnowpr > a > span:nth-child("+str(index)+")'),'::before').getPropertyValue('content')")
        phone_no.append(phone_keys[ str(repr(x))[7:12] ])
    phone_final = "".join(phone_no)

    #Address
    address = driver.find_elements_by_xpath('//*[@id="fulladdress"]/span/span')
    address = address[0].text #result

    #Tags
    tags = driver.find_elements_by_xpath('//*[@id="setbackfix"]/div[1]/div/div[4]/div[1]/div[4]/ul')
    for tag in tags:
        tag_all = tag.text
    tag_all = tag_all.splitlines() # result

    #website
    website = driver.find_elements_by_xpath('//*[@id="comp-contact"]/li[3]/span/a')
    website = str(website[0].text) # result



x = '//*[@id="srchpagination"]/a[2]'
if __name__ == "__main__" :
    # check = scrape("Jaipur" , "Women's clothing")
    # for i in check:
    #     print(i.get_attribute("data-href"))
    # print(len(check))
    print(get_data('https://www.justdial.com/Jaipur/Miss-Melange-Boutique-Raja-Park/0141PX141-X141-150123125904-M2U4_BZDET?xid=SmFpcHVyIFdvbWVuIENsb3RoaW5nIEJvdXRpcXVlcw=='))
