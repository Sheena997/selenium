# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
time.sleep(3)
driver.get("http://www.baidu.com")
time.sleep(3)

#方法一：用ID定位
driver.find_element_by_id("kw").send_keys("赵小棠") #kw为输入框id 输入赵小棠
driver.find_element_by_id("su").click() #su为百度一下id点击百度一下

#方法二：用name定位，不是每一个元素都可以用name定位，因为百度一下按钮没有name
#当两个元素name一样时就不可以用name去唯一定位
driver.find_element_by_name("wd").send_keys("虞书欣") #wd为输入框name
driver.find_element_by_id("su").click()

#方法三：用class name去定位：因为class name和tag name不唯一，所以不可以用

#方法四：用link text去定位通过链接内容去定位
driver.find_element_by_link_text("hao123").click()

#方法五：用xpath一种路径
#xpath写法： //*[@id = " "]     //*[@name=" "]
driver.find_element_by_xpath("//*[@id='kw']").send_keys("孔雪儿")
driver.find_element_by_xpath("//*[@id='su']").click()

#方法六：用css定位,用id也可以用class也可以....
driver.find_element_by_css_selector("#kw").send_keys("张楚寒")
driver.find_element_by_css_selector("#su").click()


time.sleep(6)

driver.quit()