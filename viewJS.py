from selenium import webdriver

#phamtomJS is deprecated 
# driver = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-linux-x86_64/bin/phantomjs')  # PhantomJs

#chrome headless driver
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('headless')
options.add_argument('window-size=1200x600')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.zooniverse.org/projects/zooniverse/muon-hunter/collections')  #get url 

pageSource = driver.page_source  #get source code of webpage
print(pageSource)
driver.close()  #terminate browser
