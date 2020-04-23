# coding = utf-8
from selenium import webdriver
import time
import os

#get_attribute获取属性
from selenium.webdriver import ActionChains


#alert、confirm、prompt的处理
#switch_to.frame()
#switch_to.window()
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
time.sleep(3)
#定位
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\upload.html")
driver.get(file_path)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(6)

#上传文件操作
driver.find_element_by_name("file").send_keys("C:\\Users\\99742\\Desktop\\test_041401.py")


time.sleep(10)
driver.quit()


'''
#upload.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>upload_file</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<link
href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstra
p-combined.min.css" rel="stylesheet" />
<script type="text/javascript">
</script>
</head>
<body>
<div class="row-fluid">
<div class="span6 well">
<h3>upload_file</h3>
<input type="file" name="file" />
</div>
</div>
</body>
<script
src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.
min.js"></script>
</html>
'''