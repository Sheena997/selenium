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
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\send.html")
driver.get(file_path)
driver.maximize_window()

time.sleep(6)

driver.find_element_by_xpath("/html/body/input").click()
#alert框的定位
alert = driver.switch_to.alert

#在alert框中输入文字
alert.send_keys(u"乃万")
time.sleep(5)

#输出alert框里的内容
print("alert:" + alert.text)
alert.accept()
#alert.dismiss()

#confirm的定位


time.sleep(10)
driver.quit()


'''
#alert.html
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<title>alert</title>
<script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
<link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrapcombined.min.css" rel="stylesheet" />
<script type="text/javascript"> $(document).ready(function(){ $('#tooltip').tooltip({"placement":
"right"}); $('#tooltip').click(function(){ alert('watir-webdriver better than seleniumwebdriver') }); }); </script>
</head>
<body>
<div class="row-fluid">
<div class="span6 well">
<h3>alert</h3>
<a id="tooltip" href="#" data-toggle="tooltip" title="watir-webdriver better than seleniumwebdriver">hover to see tooltip</a>
</div>
</div>
</body>
<script src="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js">
</script>
</html>

#send.html
<html>
<head>
<meta charset="UTF-8">
<title></title>
<script type="text/javascript">
function disp_prompt(){
var name=prompt("Please enter yourname","")
if (name!=null &&name!=""){
document.write("Hello " +name + "!")
}
}
</script>
</head>
<body>
<input type="button" onclick="disp_prompt()"
value="请点击"/>
</body>
</html>
'''