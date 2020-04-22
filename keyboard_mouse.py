# coding = utf-8
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
time.sleep(3)
driver.get("http://www.baidu.com")
time.sleep(3)

#对键盘的操作
#send_keys(Keys.TAB) #TAB键
#send_keys(Keys.ENTER) #ENTER键、回车键
#键盘组合键用法
driver.find_element_by_id("kw").send_keys("张楚寒")
driver.find_element_by_id("su").click()
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a') #control+A全选
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x') #control+X剪切
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v') #control+V粘贴
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a') #control+A全选
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys("傅如乔")
driver.find_element_by_id("su").click()



#对鼠标的操作
#context_click() 右击
#double_click() 双击
#drag_and_drop() 拖动
#move_to_element() 移动
#ActionChains动作链
driver.find_element_by_id("kw").send_keys("劳动节")
su1 = driver.find_element_by_id("su")
driver.maximize_window()
ActionChains(driver).context_click(su1).perform() #右击
time.sleep(5)
ActionChains(driver).double_click(su1).perform() #双击
time.sleep(5)
tiltle = driver.find_element_by_link_text("劳动节_百度百科")
target = driver.find_element_by_id("su")
#把劳动节拖动到百度百科，拖不动
ActionChains(driver).drag_and_drop(tiltle, target).perform() #拖动

time.sleep(6)
driver.quit()