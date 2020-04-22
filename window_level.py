# coding = utf-8
from selenium import webdriver
import time
import os

#get_attribute获取属性
from selenium.webdriver import ActionChains


#多层框架/窗口定位
#switch_to.frame()
#switch_to.window()
driver = webdriver.Firefox()
time.sleep(3)
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\frame.html")
driver.get(file_path)
driver.maximize_window()

#要先到第一层然后才可以到第二层然后才可以用第二层的东西
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("张楚寒")
driver.find_element_by_id("su").click()

#此时如果要用f1页面的东西必须先跳转回到默认页面然后再进入f1页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()

'''
#frame.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>frame</title>
<link
href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstra
p-combined.min.css" rel="stylesheet" />
<script type="text/javascript">$(document).ready(function(){
});
</script>
</head>
<body>
<div class="row-fluid">
<div class="span10 well">
<h3>frame</h3>
<iframe id="f1" src="inner.html" width="800",
height="600"></iframe>
</div>
</div>
</body>
<script
src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.
min.js"></script>
</html>

#inner.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>inner</title>
</head>
<body>
<div class="row-fluid">
<div class="span6 well">
<h3>inner</h3>
<iframe id="f2" src="http://www.baidu.com"
width="700"height="500"></iframe>
<a href="javascript:alert('watir-webdriver better than
selenium webdriver;')">click</a>
</div>
</div>
</body>
</html>
'''


#层级定位
driver = webdriver.Firefox()
time.sleep(3)
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\level_locate.html")
driver.get(file_path)
driver.maximize_window()
driver.find_element_by_link_text("Link1").click()
driver.implicitly_wait(10)
lst = driver.find_element_by_id("dropdown1").find_element_by_link_text("Another action")
ActionChains(driver).move_to_element(lst).perform()
#方法二：
#lst = driver.find_element_by_id("dropdown1").find_element_by_link_text("Action")
#ActionChains(driver).move_to_element(lst[0]).perform()

'''
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>Level Locate</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<link
href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css"
rel="stylesheet" />
</head>
<body>
<h3>Level locate</h3>
<div class="span3">
<div class="well">
<div class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown"
href="#">Link1</a>
<ul class="dropdown-menu" role="menu"
aria-labelledby="dLabel" id="dropdown1" >
<li><a tabindex="-1" href="#">Action</a></li>
<li><a tabindex="-1" href="#">Another action</a></li>
<li><a tabindex="-1" href="#">Something else here</a></li>
<li class="divider"></li>
<li><a tabindex="-1" href="#">Separated link</a></li>
</ul>
</div>
</div>
</div>
<div class="span3">
<div class="well">
<div class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown"
href="#">Link2</a>
<ul class="dropdown-menu" role="menu"
aria-labelledby="dLabel" >
<li><a tabindex="-1" href="#">Action</a></li>
<li><a tabindex="-1" href="#">Another action</a></li>
<li><a tabindex="-1" href="#">Something else here</a></li>
<li class="divider"></li>
<li><a tabindex="-1" href="#">Separated link</a></li>
</ul>
</div>
</div>
</div>
</body>
<script
src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
</html>
'''

time.sleep(6)
driver.quit()