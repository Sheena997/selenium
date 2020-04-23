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

#text返回alert/confirm/prompt中的文字信息
#alert框就是警告框
#accept点击确认按钮
#dismiss点击取消按钮，如果有的话
#send_keys输入值，这alert\confirm没有对话框就不能用了，不然会报错
#注意：switch_to_alert()只能处理原生的alert
driver = webdriver.Firefox()
time.sleep(3)
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\modal.html")
driver.get(file_path)
driver.maximize_window()

time.sleep(6)

#DIV对话框处理
#点击click按钮
driver.find_element_by_id("show_modal").click()
time.sleep(8)
div1 = driver.find_element_by_class_name("modal-body")
div1.find_element_by_id("click").click()
time.sleep(8)
#如果多个div里面都有button
#buttons = driver.find_element_by_class_name("modal-footer")
buttons = driver.find_elements_by_tag_name("button")
buttons[0].click() #close



time.sleep(10)
driver.quit()


'''
#modal.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>modal</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<link
href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css"
rel="stylesheet" />
<script type="text/javascript">
$(document).ready(function(){
$('#click').click(function(){
$(this).parent().find('p').text('Click on the link to success!');
});
});
</script>
</head>
<body>
<h3>modal</h3>
<div class="row-fluid">
<div class="span6">
<!-- Button to trigger modal -->
<a href="#myModal" role="button" class="btn btn-primary"
data-toggle="modal" id="show_modal">Click</a>
<!-- Modal -->
<div id="myModal" class="modal hide fade" tabindex="-1"
role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal"
aria-hidden="true">×</button>
<h3 id="myModalLabel">Modal header</h3>
</div>
<div class="modal-body">
<p>Congratulations, you open the window!</p>
<a href="#" id="click">click me</a>
</div>
<div class="modal-footer">
<button class="btn" data-dismiss="modal"
aria-hidden="true">Close</button>
<button class="btn btn-primary">Save changes</button>
</div>
</div>
</div>
</div>
</body>
<script
src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
</html>
'''