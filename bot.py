from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


a=[]
browser = webdriver.Chrome()
browser.get(('https://ivapwa.sadadpsp.ir/'))

/////////////////////////////////////////////////









................................................
/////////////////////////////////////////////////
#telNum = input("Please input your phone number: ")
#sender_card_number = input("Please Enter your card 16 digit number: ")
#second_pass = input("Second Pass: ")
#cvv2 = input("cvv2: ")
#month = input("month: ")
#year = input("year: ")

#des_card_number = input("des_card_number: ")
#amount = input("amount:  ")

#WebElementTel = browser.findElement(By.cssSelector(“button[class*=‘iva-input form-control  ’]”));


#b = browser.find_elements_by_class_name("btn btn-warning btn-block");
#b.click();

#c = browser.find_element_by_xpath("//*[text()='ورود']").text
#c.click()
time.sleep(10)

try:
	choice = browser.find_element_by_xpath("//button[@class='btn btn-warning btn-block']")
	choice.click()

except Exception:
    print("Unable to locate button")
    pass

time.sleep(5)
try:
	choice = browser.find_element_by_xpath("//input[@class='iva-input form-control  ']")
	choice.send_keys(telNum)

	#(ActionChains(browser)
     #       .move_to_element(telNum)
      #      .click()
       #     .perform())

except Exception:
    print("Unable to locate label")
    pass

time.sleep(3)


try:
	choice = browser.find_element_by_xpath("//button[@class='btn btn-block btn-warning']")
	choice.click()

except Exception:
    print("Unable to locate button")
    pass


#a = driver.find_elements_by_class_name("iva-input form-control  ");
#a.click();

time.sleep(10)

security_code = input('Type the security code here: ')

try:
	security = browser.find_element_by_xpath("//input[@class='iva-input form-control  ']")
	security.send_keys(security_code)

except Exception:
    print("Unable to locate button")
    pass

time.sleep(5)


try:
	choice = browser.find_element_by_xpath("//button[@class='btn btn-block btn-warning']")
	choice.click()

except Exception:
    print("Unable to locate button next")
    pass



time.sleep(5)

try:
	cardtocardd = browser.find_element_by_xpath("//div[@class='Menu-Title' and text()='کارت به کارت']")
    #cardtocardd = browser.find_element_by_xpath("//input[@class='iva-input form-control pan ' and @tabindex='']")
	#cardtocardd = browser.find_element_by_xpath("//div[@class='Menu-Icon' and @style='background-image: url(/images/service/CardToCardService.png)']")
	cardtocardd.click()

except Exception:
    print("Unable to locate button CardToCardService")
    pass

time.sleep(7)




#sender card info





try:

	sender = browser.find_element_by_xpath("//input[@class='iva-input form-control pan ' and @tabindex='1']")
	sender.click()
	sender.send_keys(sender_card_number)

except Exception:
    print("Unable to locate sender")
    pass


time.sleep(3)

#second_pass
try:
	#secondd = browser.find_element_by_xpath("//div[@class='iva-input form-control  ' and @tabindex='2']")
	#secondd = browser.find_element_by_xpath()
    secondd = browser.find_element_by_id('input-pin2')
    secondd.click()
    secondd.send_keys(second_pass)

except Exception:
    print("Unable to locate second_pass")
    pass

time.sleep(3)


try:
    cvv = browser.find_element_by_id('input-cvv2')
    cvv.click()
    cvv.send_keys(cvv2)

except Exception:
    print("Unable to locate cvv2")
    pass

time.sleep(3)

try:
    monthh = browser.find_element_by_id('input-expd-month')
    monthh.click()
    monthh.send_keys(month)

except Exception:
    print("Unable to locate month")
    pass


time.sleep(3)



try:
    yearr = browser.find_element_by_id('input-expd-year')
    yearr.click()
    yearr.send_keys(year)

except Exception:
    print("Unable to locate year")
    pass

time.sleep(3)


try:
	#dess = browser.find_element_by_xpath("//input[@class='iva-input form-control pan ']")
	dess= browser.find_element_by_xpath("//input[@class='iva-input form-control pan ' and @tabindex='6']")
	dess.click()
	dess.send_keys(des_card_number)

except Exception:
    print("Unable to locate des_card")
    pass

time.sleep(3)


try:
	amountt = browser.find_element_by_xpath("//input[@class='iva-input form-control  ' and @tabindex='7']")
	amountt.click()
	amountt.send_keys(amount)

except Exception:
    print("Unable to locate amount")
    pass



time.sleep(10)

try:
	est = browser.find_element_by_xpath("//button[@class='btn btn-block btn-warning  ']")
	est.click()

except Exception:
    print("Unable to locate button est")
    pass

time.sleep(7)

try:
	est = browser.find_element_by_xpath("//button[@class='btn btn-block btn-warning  ']")
	est.click()

except Exception:
    print("Unable to locate button est")
    pass

time.sleep(5)



.......................
/////////////////////////
telNum = '09059492746'
sender_card_number = '6362141051999168'
second_pass = '34221040'
cvv2 = '1847'
month = '09'
year = '00'

des_card_number = '6362144502916294'
amount = '30000'
///////////////////////


