# coding = utf-8
from selenium import webdriver
import time
import os

#get_attribute获取属性
driver = webdriver.Firefox()
time.sleep(3)
file_path = 'file:///' + os.path.abspath("C:\\Users\\99742\\Desktop\\text.html")
driver.get(file_path)
inputs = driver.find_elements_by_tag_name("input")
time.sleep(3)
for input in inputs:
    if input.get_attribute('type') == "checkbox": #找出属性type值为checkbox的
        input.click() #点击打钩

time.sleep(6)
driver.quit()

#HTML文件text.html

<html>
<head>
<meta https-equiv="content-type" content="text/html;charset=utf-8"/>
<title>checkbox</title>
</head>

<body>
<h3>text</h3>
<div class="well">
<form class="form-horizontal">
<div class="control-group">
<label class="control-label" for="c1">checkbox1</label>
<div class="controls">
<input type="checkbox" id="c1" />
</div>
</div>
<div class="control-group">
<label class="control-label" for="c2">checkbox2</label>
<div class="controls">
<input type="checkbox" id="c2" />
</div>
</div>
<div class="control-group">
<label class="control-label" for="c3">checkbox3</label>
<div class="controls">
<input type="checkbox" id="c3" />
</div>
</div>
<div class="control-group">
<label class="control-label" for="r">radio</label>
<div class="controls">
<input type="radio" id="r1" />
</div>
</div>
<div class="control-group">
<label class="control-label" for="r">radio</label>
<div class="controls">
<input type="radio" id="r2" />
</div>
</div>
</form>
</div>
</body>
</html>
</html>