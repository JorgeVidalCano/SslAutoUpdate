import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class updateSSLforFree():
	"""docstring for getSslForFree"""
	
	def setUp(self, web):
		""" Opens Chrome"""
		options = webdriver.ChromeOptions()
		#options.add_argument('headless')
		#self.driver = webdriver.Chrome(chrome_options=options)
		self.driver = webdriver.Chrome()
		self.driver.get(web)

	def login(self, user, passwordAccount):
		"""Writes the personal info and logs in""" 
		
		email = self.driver.find_element_by_xpath("//input[@name='email']")
		email.send_keys(user)
		password = self.driver.find_element_by_xpath("//input[@name='password']")
		password.send_keys(passwordAccount)

		if 'Cloudflare' in self.driver.title:
			password.send_keys(Keys.ENTER)			
		elif 'SSL For Free' in self.driver.title:
			login = self.driver.find_element_by_xpath("//button[contains(text(), 'Login')]")
			login.send_keys(Keys.ENTER)
	
	def pressRenew(self):
		""" Press Renew button """
		self.driver.implicitly_wait(5)
		renew = self.driver.find_element_by_xpath("//td/a[contains(text(), 'Renew')]")
		renew.send_keys(Keys.ENTER)#.perform() I think it works without the perform
		
	def pressVerify(self):
		""" Press Verify buton"""
		self.driver.implicitly_wait(10)
		#verify = self.driver.find_element_by_xpath("//button[contains(text(), 'Manually Verify Domain')]")
		verify = self.driver.find_elements_by_xpath("//form/button[contains(text(), 'Manually Verify Domain')]")
		for i in verify:
			print(i.getText)
		#verify = self.driver.find_element_by_xpath("//input[@name='manual']")
		verify.send_keys(Keys.ENTER)

	def copySllValue(self):
		""" Copies value """
		return self.driver.find_element_by_class("box_copy_text").getText()
	
	def select_acmeChallenge(self, value):
		""" Pastes _acme-Challenge """
		
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_xpath("//div/div[contains(text(), 'ortopediaplus.com')]").send_keys(Keys.ENTER) 
		self.driver.find_element_by_xpath("//span[contains(text(), 'DNS')]").send_keys(Keys.ENTER) 
		self.driver.find_element_by_xpath("//td[contains(text(), _acme-challenge)]//following-sibling::td").send_keys(Keys.ENTER)

	def closeChrome(self):
		""" Selects a name in the file"""
		self.driver.close()
		return


user = ''
## SslForFree data
webSsl = "https://www.sslforfree.com/login"
passSsl = ''

## Cloudflare data
webCloud = "https://dash.cloudflare.com/login"
passCloud = ''



Ssl = updateSSLforFree()
Ssl.setUp(webSsl)

#cloud = updateSSLforFree()
#cloud.setUp(webCloud)

try:

	Ssl.login(user, passSsl)
	Ssl.pressRenew()
	Ssl.pressVerify()
	# here I should get the keys for coping in cloudflare
	value = copySllValue()
	print(value)
	#value = "prueba"
	#cloud.login(user, passCloud)

	#cloud.select_acmeChallenge(value)
except Exception as e: 
	print(e)
finally:
	time.sleep(30)
	#Ssl.closeChrome()
	#cloud.closeChrome()

