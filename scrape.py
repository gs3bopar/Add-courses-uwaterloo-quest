from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from random import randint


def tryToAddACourseIfOpen():
  # open chrome window
  options = webdriver.ChromeOptions()
  options.binary_location = "/Applications/Google Chrome 3.app/Contents/MacOS/Google Chrome"
  chrome_driver_binary = "/Users/../Downloads/chromedriver"
  driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

  # open url source
  driver.get('https://adfs.uwaterloo.ca/adfs/ls/idpinitiatedsignon.aspx?LoginToRP=urn:quest.ss.apps.uwaterloo.ca')

  # input data
  enter_email = driver.find_element_by_id('userNameInput')
  enter_email.send_keys('') # add your uwaterloo quest email address
  enter_email.submit()

  # enter password
  enter_password = driver.find_element_by_id('passwordInput')
  enter_password.send_keys('') # add your uwaterloo quest password
  enter_password.submit()

  # it takes a bit of time to load data here
  sleep(3)

  # click on enroll tab
  course_selection_enroll = driver.find_element_by_id('win0divPTNUI_LAND_REC_GROUPLET$2')
  course_selection_enroll.click()

  sleep(3)

  # there is a trick to it as they uses iframe therefore
  driver.switch_to.frame(0)

  sleep(3)

  for x in range(3):
    javaScript = "return document.getElementById('win0divDERIVED_REGFRM1_SSR_STATUS_LONG$" + str(x) + "').getElementsByTagName('div')[0].getElementsByTagName('img')[0].alt"
    ret_value = driver.execute_script(javaScript)
    print ('Course is ' + ret_value)
    if (ret_value == 'Open'):
      print("Hoorray course is open! Trying to add")

      # proceed to adding courses
      proceed_next_step = driver.find_element_by_id('DERIVED_REGFRM1_LINK_ADD_ENRL$82$')
      proceed_next_step.click()

      sleep(4)

      # Finishing enrolling courses
      finish_enroll = driver.find_element_by_id('DERIVED_REGFRM1_SSR_PB_SUBMIT')
      finish_enroll.click()

      sleep(4)

      # check is class has been added if yes then exit the script
      for x in range(3):
        javaScript = "return document.getElementById('win0divDERIVED_REGFRM1_SSR_STATUS_LONG$" + str(x) + "').getElementsByTagName('div')[0].getElementsByTagName('img')[0].alt"
        ret_value = driver.execute_script(javaScript)
        print ('Course added ' + ret_value)
        if (ret_value == 'Success'):
          driver.close()
          return True

  # close the current driver and try next time
  driver.close()
  return False


while True:
  checkifWorked = tryToAddACourseIfOpen()
  if (checkifWorked):
    break
  print("No couse is open right now. Will try in next 20-30 minutes!")
  sleep(randint(1860, 2820)) # sleeps for somewhere around 31 to 47 minutes


print("Course has been added! Exiting...")
