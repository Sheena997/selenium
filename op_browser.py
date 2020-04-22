# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
time.sleep(3)
driver.get("http://www.baidu.com")
time.sleep(3)

#操作测试对象
#click 点击对象
#send_keys 在对象上模拟按键输入
#clear 清除对象的内容，如果可以的话
#submit 提交对象的内容，如果可以的话
#text 用于获取元素的文本信息

#text输出,可以通过id、name、link_text都可以输出
data = driver.find_element_by_id("virus-2020").text
print(data)
data = driver.find_element_by_link_text("新闻").text
print(data)


#添加等待
#clear和implictitly_wait()为智能等待，time.sleep()为固定等待
#time.sleep()为等待固定时间，
#driver.implicitly.wait()为在一个时间范围内等待
#WebDriverWait等待10秒钟等待元素"乃万_百度百科"被加载出来，每隔500ms扫描一次

#driver.find_element_by_id("kw").send_keys("虞书欣")
time.sleep(8)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("乃万")
driver.find_element_by_id("su").submit() #可以用submit代替click

#WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_id("乃万_百度百科"))
driver.implicitly_wait(10)
driver.find_element_by_link_text("乃万_百度百科").click()


#打印信息
#打印title和url
driver.find_element_by_link_text("hao123").click()
time.sleep(5)
t = driver.title
print(t)
url = driver.current_url
print(url)


#对浏览器的操作

#浏览器的最大化和最小化和自定义设置浏览器的大小
driver.maximize_window()
driver.find_element_by_link_text("hao123").click()
time.sleep(5)
driver.set_window_size(400, 800)
time.sleep(5)
driver.minimize_window()

#浏览器的前进和后退
driver.find_element_by_id("kw").send_keys(u"乃万") #因为里面写的是汉字不是英文所以要写u（utf-8）
driver.find_element_by_id("su").click()
time.sleep(6)
driver.back() #后退
time.sleep(6)
driver.forward() #前进

#控制浏览器的滚动条
driver.find_element_by_id("kw").send_keys("乃万")
driver.find_element_by_id("su").click()
driver.set_window_size(400, 900)
time.sleep(3)
#将页面滚动条拖动到底部
js = "var q=document.documentElement.scrollTop=100000" #javascript脚本
driver.execute_script(js)
time.sleep(6)
#将页面滚动条拖动到顶部
js = "var q=document.documentElement.scrollTop=0" #javascript脚本
driver.execute_script(js)


time.sleep(6)
driver.quit()
