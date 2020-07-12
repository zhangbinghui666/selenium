'''文件上传是web页面上很常见的一个功能，自动化成功中操作起来却不是那么简单。
一般分两个场景：一种是input标签，这种可以用selenium提供的send_keys()方法轻松解决；
另外一种非input标签实现起来比较困难，可以借助autoit工具或者SendKeys第三方库。
本篇以博客园的上传图片为案例，通过send_keys()方法解决文件上传问题'''

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox()
driver.get("http://www.cnblogs.com/")
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id('input1').send_keys('15239687008')
driver.find_element_by_id('input2').send_keys('zbh@911915')
driver.find_element_by_id('remember_me').click()
time.sleep(2)
driver.find_element_by_id('signin').click()
b=driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/div/div[2]/div[2]/div/div[3]')
ActionChains(driver).move_to_element(b).perform()
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span[1]').click()
time.sleep(5)
driver.maximize_window()
driver.find_element_by_link_text('我的博客').click()
time.sleep(3)
driver.find_element_by_link_text('管理').click()
time.sleep(2)
driver.find_element_by_link_text('添加新随笔').click()
time.sleep(3)   #必须添加休息时间
driver.find_element_by_css_selector("img.mceIcon").click()
time.sleep(5)
#定位到所有iframe，取第二个
iframe=driver.find_elements_by_tag_name('iframe')[1]
#切换到iframe上
driver.switch_to.frame(iframe)

driver.find_element_by_name("file").send_keys(r"D:\test.png")

time.sleep(5)
driver.switch_to.default_content()   #退出iframe
driver.find_element_by_id('Editor_Edit_txbTitle').send_keys('富文本测试')
#重点要讲的富文本的编辑，这里编辑框有个iframe，所以需要先切换
driver.switch_to.frame('Editor_Edit_EditorBody_ifr')
time.sleep(4)
driver.find_element_by_id('tinymce').send_keys('富文本测试1')
time.sleep(2)