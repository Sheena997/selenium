# coding = utf-8
from selenium import webdriver
import time
import os

#get_attribute获取属性
from selenium.webdriver import ActionChains


#下拉框处理
#switch_to.frame()
#switch_to.window()
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
time.sleep(3)
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\drop_down.html")
driver.get(file_path)
driver.maximize_window()
#等待10秒钟等待元素“ShippingMethod”被加载出来，每隔500ms扫描一次
WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("ShippingMethod"))
#方法一：用xpath定位
ship = driver.find_element_by_id("ShippingMethod")
ship.find_element_by_xpath("//*[@value='10.69']").click()
#方法二：for循环：定位一组元素，根据属性遍历数组sing为
lists = driver.find_elements_by_tag_name("option")
for lst in lists:
    if lst.get_attribute('value') == "10.69":
        lst.click()
#或者不用遍历直接
#lists[2].click()


time.sleep(10)
driver.quit()



'''
<html>
<body>
<select id="ShippingMethod"
onchange="updateShipping(options[selectedIndex]);" name="ShippingMethod">
<option value="12.51">UPS Next Day Air ==> $12.51</option>
<option value="11.61">UPS Next Day Air Saver ==> $11.61</option>
<option value="10.69">UPS 3 Day Select ==> $10.69</option>
<option value="9.03">UPS 2nd Day Air ==> $9.03</option>
<option value="8.34">UPS Ground ==> $8.34</option>
<option value="9.25">USPS Priority Mail Insured ==> $9.25</option>
<option value="7.45">USPS Priority Mail ==> $7.45</option>
<option value="3.20" selected="">USPS First Class ==> $3.20</option>
</select>
</body>
</html>
'''