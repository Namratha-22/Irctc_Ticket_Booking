# TATKAL-TICKET
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import  Keys
from time import sleep, strftime


def login():
    driver.get('https://www.irctc.co.in/eticketing/loginHome.jsf')
    wait=WebDriverWait(driver, 60)
    wait.until(EC.presence_of_element_located((By.NAME, 'j_username'))).send_keys(IRCTC_USERNAMEW)
    driver.find_element_by_name('j_password').send_keys(IRCTC_PASSWORD)
    driver.find_element_by_name('j_captcha').send_keys('')

def planjourney():
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'jpform:fromStation'))).send_keys(FROM_STATION)
    driver.find_element_by_id('jpform:toStation').send_keys(TO_STATION)
    driver.find_element_by_id('jpform:journeyDateInputDate').send_keys(DATE)
    train_nums=driver.find_elements_by_xpath("//div/h3[@class='ico22 black fontQuick']")
    for i in train_nums:
        if i == TRAIN_NO :
            driver.find_element_by_id('jpform:jpsubmit').click() 
    

def filldetails():
    WebDriverWait(driver, 60).until(EC.title_contains('Book Ticket'))
    for name, el in zip(NAME, driver.find_elements_by_class_name('psgn-name')):
        el.send_keys(name)
    for age, el in zip(AGES, driver.find_elements_by_class_name('psgn-age')):
        el.send_keys(age)
    for gender, el in zip(GENDERS, driver.find_elements_by_class_name('psgn-gender')):
        Select(el).select_by_value(gender)
    for berth, el in zip(BERTHS, driver.find_elements_by_clas_name('psgn-berth-choice')):
        Select(el).select_by_value(berth)
    driver.find_element_by_xpath("//div/button[text()='SAVE']").click()     
    

def sbi():
    driver.find_element_by_id('//div/button[text()="Pay ₹ 200"]').click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'debitCardNumber'))
        ).send_keys(SBI_CARD_NUMBER)
    driver.find_element_by_id('debitCardholderName').send_keys(SBI_CARD_NAME)
    driver.find_element_by_id('debiMonth').send_keys(SBI_CARD_EXPIRY_MM)
    driver.find_element_by_id('debiYear').send_keys(SBI_CARD_EXPIRY_YYYY)
    driver.find_element_by_id('cardPin').send_keys(SBI_CARD_PIN)
   
    


IRCTC_USERNAME = 'IRCTC_USERNAME'  #Enter you irctc username
IRCTC_PASSWORD = 'IRCTC_PASS'  #Enter you irctc password
FROM_STATION = 'LUCKNOW NR - LKO' #Enter the name of the boarding station.
FROM_STATION_CODE = 'LKO'
TO_STATION = 'PRAYAG - PRG' #Enter the name of the deboarding station.
TO_STATION_CODE = 'PRG'
DATE = '27-03-2016'   #Enter the date of journey
TRAIN_NO = '14210'   #Enter the train number
CLASS = 'CC'         #Enter the class
CLASS_INDEX = '0'    #Enter the class index that you will find the source code 
NAMES = ['NAME1'] #Passenger name list
AGES = ['20']            #Passenger age list
GENDERS = ['M']          #Passenger sex list
BERTHS = ["  "]          #Passenger preference list. Double space represent no preference.    

SBI_CARD_NUMBER = ''
SBI_CARD_EXPIRY_MM=''
SBI_CARD_EXPIRY_YYYY=''
SBI_CARD_PIN='ATM'   #ATM PIN
SBI_CARD_NAME=''  

if __name__ == '__main__':
    driver =webdriver.Chrome(executable_path="C:\python practice\py_driver\chromedriver_win32\chromedriver.exe")

    login()
    planjourney()
    filldetails()
    sbi()
