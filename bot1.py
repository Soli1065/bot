from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests


# GET Request
# defining a params dict for the parameters to be sent to the API 
##PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
##r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
##data = r.json()


# POST Request  
# defining the api-endpoint  
##API_ENDPOINT = "http://pastebin.com/api/api_post.php"
  
# your API key here 
##API_KEY = "XXXXXXXXXXXXXXXXX"
  
# your source code here 
##source_code = ''' 
##print("Hello, world!") 
##a = 1 
##b = 2 
##print(a + b) 

  
# data to be sent to api 
##data = {'api_dev_key':API_KEY, 
  ##      'api_option':'paste', 
    ##    'api_paste_code':source_code, 
      ##  'api_paste_format':'python'} 
  
# sending post request and saving response as response object 
##r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
##pastebin_url = r.text 
##print("The pastebin URL is:%s"%pastebin_url) 





a=[]
browser = webdriver.Chrome()
browser.get(('https://ivapwa.sadadpsp.ir/'))


##telNum = '09059492746'
####sender_card_number = '6362141051999168'
####second_pass = '34221040'
####cvv2 = '1847'
####month = '09'
####year = '00'

####des_card_number = '6362144502916294'
####amount = '1000'
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


####################################################################################################
####### First JSON Receive
#open the file
with open('data0.json') as first:
  data = json.load(first)
  id = json.load(data['id'])
  telNum = id


#####################################################################################################

time.sleep(10)


try:
	choice = browser.find_element_by_xpath("//button[@class='btn btn-warning btn-block']")
	choice.click()

except Exception:
    print("Unable to locate button ENTER")
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
    print("Unable to locate button NEXT")
    pass


#a = driver.find_elements_by_class_name("iva-input form-control  ");
#a.click();

time.sleep(10)

#############################################################################################################
#### Second JSON file



found = False

while not found:
    time.sleep(4)
    try:
        with open('data1.json') as second:
            data = json.load(second)
            security_code = json.load(data['verification_code'])
            found = True
    except:
        print('not valid JSON')
        pass

#############################################################################################################
##security_code = input('Type the security code here: ')

time.sleep(3)

try:
	security = browser.find_element_by_xpath("//input[@class='iva-input form-control  ']")
	security.send_keys(security_code)

except Exception:
    print("Unable to locate place for security_code")
    pass

time.sleep(2)


try:
	choice = browser.find_element_by_xpath("//button[@class='btn btn-block btn-warning']")
	choice.click()

except Exception:
    print("Unable to locate button next")
    pass



time.sleep(3)

try:
	cardtocardd = browser.find_element_by_xpath("//div[@class='Menu-Title' and text()='کارت به کارت']")
    #cardtocardd = browser.find_element_by_xpath("//input[@class='iva-input form-control pan ' and @tabindex='']")
	#cardtocardd = browser.find_element_by_xpath("//div[@class='Menu-Icon' and @style='background-image: url(/images/service/CardToCardService.png)']")
	cardtocardd.click()

except Exception:
    print("Unable to locate button CardToCardService")
    pass

time.sleep(4)



#########################################################################################################################
######CARD INFO

found = False

while not found:
    time.sleep(4)
    try:
        with open('data2.json') as third:
            data = json.load(third)
            sender_card_number = json.load(data['sender_card_number'])
            second_pass = json.load(data['second_pass'])
            cvv2 = json.load(data['cvv2'])
            month = json.load(data['exp_month'])
            year = json.load(data['exp_year'])
            amount = json.load(data['amount'])
            des_card_number = json.load(data['des_card_number'])
            found = True
    except:
        print('not valid JSON')
        pass

#######################################################################################################################

time.sleep(6)

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






