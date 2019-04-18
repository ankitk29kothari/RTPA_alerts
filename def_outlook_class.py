from pip import install_import
install_import('win32com.client','pypiwin32')


from pip import install_import
install_import('selenium','selenium')

from pip import install_import
install_import('pandas','pandas')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import sys
import win32com.client
import win32com
import re
import pandas as pd
import datetime
import time


name='kirti'
print(name)

class outlook:

	def __init__(self,folder):
		self.folder=folder

	def country(self,country):
		values_dict={'US':'United States of America','UK':'United Kingdom'}

		for keys,values in values_dict.items():
			
			#print(keys.lower(),subject[4])
			if keys.lower() in country.lower():
				print(keys,values,country)
				return values
			else:
				country1=country

		return country1





	def values (self,subject):
		#Convert RTPA LAYER
		global layer
		global rtpa_type
		
		values1_dict={'AP':'Wireless','WLC':'Wireless','SWITCH':'LAN','LAN':'LAN','IP':'WAN','STEELHEAD':"WAN Optimization",'Riverbed':'WAN Optimization','LINK':'WAN','Perofrmance':'Performance Issue','Bandwidth':'WAN'}
		values2_dict={'low':'Yellow','Medium':'Orange','High':'Red'}


		for keys,values in values1_dict.items():
			#print(keys.lower(),subject[4])
			if keys.lower() in subject[4].lower():
					layer=values
					print("Convert: ",keys,values)

		#Convert RTPA TYPE
		for keys,values in values2_dict.items():
			#print(keys.lower(),subject)
			if keys.lower() in subject[2].lower():
				rtpa_type=values



	def logs(self,status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,check):
		dict = {'Status': status,'Incident_no': incident_no, 'Layer': layer,'Rtpa_type': rtpa_type,'Country': country,'City': city,
		'Logs': check,'Tittle': tittle,'Impact': impact,'Action_taken': action_taken,'Next_step': next_step }
		df = pd.DataFrame(dict, index=[datetime.datetime.now()])
		# saving the dataframe 
		#df.to_csv('Logs.csv',mode='a')
		df.to_csv('Logs.csv',mode='a',header=False)


	def pprint(self,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step):
		#print ("Incident No.",incident_no)
		print ("Tittle- ",tittle)
		print ("Type- ",rtpa_type)
		print ("Impact- ",impact)
		#print ("Action Taken- ",action_taken)
		#print ("Next Step-", next_step)
		print ("Country- ",country)
		print ("City- ",city)
		print ("Layer-", layer)
		#df.to_csv('Logs.csv',mode='a') 

	def rtpa_finished(self,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step):
		self.pprint(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step)
		driver.get("https://tt-gateway5.orange-business.com/serviceApi/qa/history.html")
		time.sleep(5)
		html_source = driver.page_source
		if incident_no in html_source:
			d_layer = driver.find_element_by_link_text(incident_no)
			d_layer.click()
			time.sleep(2)
			d_comment = driver.find_element_by_id('rtpa_incNumber')
			d_comment.send_keys(action_taken)
			close_button = Select(driver.find_element_by_xpath('//*[@data-ng-model="formData.rtpaStatus"]'))
			close_button.select_by_visible_text('Closed')
			submit = driver.find_element_by_xpath('//*[@type="submit"]')
			submit.click()
			time.sleep(5)
			html_source = driver.page_source
			if "RTPA Updated Successfully." in html_source:
				print ('Submit Sucess')
				return ("Submit")
			else:
				self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,"unable to detect Submit button")






	def rtpa_updated(self,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step):
		self.pprint(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step)
		driver.get("https://tt-gateway5.orange-business.com/serviceApi/qa/history.html")
		time.sleep(5)
		html_source = driver.page_source
		if incident_no in html_source:
			d_layer = driver.find_element_by_link_text(incident_no)
			d_layer.click()
			time.sleep(2)
			d_comment = driver.find_element_by_id('rtpa_incNumber')
			d_comment.send_keys(action_taken)
			submit = driver.find_element_by_xpath('//*[@type="submit"]')
			submit.click()
			time.sleep(5)
			html_source = driver.page_source
			if "RTPA Updated Successfully." in html_source:
				print ('Submit Sucess')
				return ("Submit")
			else:
				self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,"unable to detect Submit button")



	def rtpa_new(self,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step):
		self.pprint(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step)
		driver.get("https://tt-gateway5.orange-business.com/serviceApi/qa/history.html")
		time.sleep(5)
		html_source = driver.page_source
		if incident_no in html_source:
			print(Dulicate)
			return ("Duplicate")
		driver.get("https://tt-gateway5.orange-business.com/serviceApi/qa/index.html")
		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@data-ng-options="rtpaService as rtpaService.serviceName for rtpaService in rtpaServiceList track by rtpaService.serviceId"]')))
		time.sleep(4)
		d_title = driver.find_element_by_id('rtpa_title')
		d_incident_no = driver.find_element_by_id('rtpa_incNumber')
		d_rtpa_impact = driver.find_element_by_id('rtpa_impact')
		d_layer = Select(driver.find_element_by_xpath('//*[@data-ng-options="rtpaService as rtpaService.serviceName for rtpaService in rtpaServiceList track by rtpaService.serviceId"]'))
		d_rtpa_type = Select(driver.find_element_by_xpath('//*[@data-ng-options="rtpaType as rtpaType.rtpaTypeName for rtpaType in rtpaTypeList track by rtpaType.rtpaTypeId"]'))
		d_rtpa_country = Select(driver.find_element_by_xpath('//*[@data-ng-options="country as country.countryName for country in countryList track by country.countryId"]'))
		d_rtpa_city = Select(driver.find_element_by_xpath('//*[@data-ng-options="site as site.siteName for site in siteList track by site.siteId"]'))

		d_title.send_keys(tittle)
		d_incident_no.send_keys(incident_no)
		d_layer.select_by_visible_text(layer)

		for o in d_rtpa_country.options:
			if country.lower() in o.text.lower():
				d_rtpa_country.select_by_visible_text(o.text)
		time.sleep(2)
		for o in d_rtpa_city.options:
			search = re.search(city.lower(), o.text.lower())
			if (search):
				d_rtpa_city.select_by_visible_text(o.text)
				break
		else:
			(d_rtpa_city.select_by_visible_text("Other"))
					
		d_rtpa_type.select_by_visible_text(rtpa_type)
		d_rtpa_impact.send_keys('['+incident_no+'] '+impact)
		time.sleep(2)
		submit = driver.find_element_by_xpath('//*[@type="submit"]')
		submit.click()
		time.sleep(5)
		html_source = driver.page_source
		if "RTPA Submitted Successfully." in html_source:
			print ('Submit Sucess')
			return ("Submit")
		else:
			self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,"unable to detect Submit button")


	
		
		
	
    #read mail from outlook
	def mail_read(self):
		outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
		accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;
		#connection with outlook
		for account in accounts:
			global inbox
			inbox = outlook.Folders(account.DeliveryStore.DisplayName)
			print(account.DisplayName)
			folders = inbox.Folders
			messages = folders[self.folder].Items
			for message2 in messages:
				if(1==1):
					sender = str(message2.Sender)
					receiver = str(message2.To)
					cc = message2.Cc
					subject = str(message2.Subject)
					print('Subject ',subject)
					body = str(message2.Body)
					print('Body ',body)
					if (message2.Unread == True) :
					#if (1==1):
						
						subject=subject.split('--')
						
						
						incident_no=subject[0].split(" ")[-1].upper()

						print("==========================")
						print ("Incident No.",incident_no)
						
						type=subject[2]
						status=subject[1].lower()
						body=body.split("\xa0\t")

						#print(body)
						tittle=str(body[1].strip()).split('\t')[1]
						impact=str(body[5]).strip().split('\r\n')[1]
						#print(body)
						action_taken=str(body[6]).strip().split('\t')[1]
						action_taken=action_taken[:300]
						
						next_step=str(body[7].strip()).split('\t')[1]


						location=body[8].split(";")
						
						"""j=0
						for i in body:
							j+=1
							print(j,': ',i)"""
						country=location[0].split("\t")[1].strip()
						try:
							city=location[1].split('\t')[0].strip()
							city=city.split(" ")[0]
							
							#city=city.replace('(TOP 50)','')
							
											
						except Exception as e:
							city="Other"
						
						print('Status-' ,status)


						# Call function to convert values

						self.values(subject)
						country=self.country(country)
						#print('Country - ',country)
						check=" "

						try:
							self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,check)
						except:
							pass


						if (status=='new') and (rtpa_type !='Yellow'):
							
							check=self.rtpa_new(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step)
							if (check == "Submit") or (check=='Duplicate'):
								message2.Unread = False
								self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,check)

						elif (status=='updated'):
							check=self.rtpa_updated(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step)
							if (check == "Submit"):
								message2.Unread = False
								self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,check)

						elif (status=='finished'):
							check=self.rtpa_finished(incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step)
							if (check == "Submit"):
								message2.Unread = False
								self.logs(status,incident_no,tittle,layer,rtpa_type,impact,country,city,action_taken,next_step,check)

						


	
					

					#(sender=='ww.rtpa.notification@GSK.COM')
					
					
					

					#print('From',sender)
					#print('Subject',subject)
					#message2.Unread = False
					

				#except Exception as e:
					#print('Error',e)	
					
					
					
					
		
def chrome():
	from selenium import webdriver
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import Select
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver.chrome.options import Options
	global driver

	driver = webdriver.Chrome(executable_path=r"chromedriver.exe")



	



	







chrome()


#rtpa_tool(1,2,"LAN","SWAT","ORANGE","Spain","Aranda")

while True:
	time.sleep(5)
	#if __name__ == '__main__':
	a=outlook("inbox")
	#a=outlook(18)
	try:
		a.mail_read()
	except Exception as e:
		print('Error-',e)
		try:
			a.logs("","","","","","","","","","",e)
		except:
			pass






