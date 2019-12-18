# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import time
import urllib

options = webdriver.ChromeOptions()
store_path = r'D:\carbon'
if not os.path.exists(store_path):
    os.makedirs(store_path)
prefs = {'download.default_directory': store_path, 'profile.default_content_settings.popups': 0}
options.add_experimental_option('prefs', prefs)
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
reqStr = """每日简报
数据概览
今日实时数据：
今日用户：13人 访问用户：75人 访问次数：1735 打开次数：380次 平均停留时长：1.48S 跳出率：39.12%
昨日
新增用户：14人 访问用户： 67人 访问次数：1875 打开次数：280次 平均停留时长：1.48S 跳出率：39.12%

核心业务转换漏斗
步骤					处罚用户数		较上一步转化率			最终转化率

进入首页				72				100%				100%

行驶证OCR识别成功		  46			  63.89%			  63.89%

报价成功				33				71.74%				45.83%

核保成功				5				15.15%				6.94%"""
reqStr = urllib.parse.quote(reqStr)
reqStr = urllib.parse.quote(reqStr)
driver.get(
    "https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&t=base16-light&wt=none&l=vue&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=" + reqStr)
driver.find_element_by_class_name("jsx-789403696 ").click()
time.sleep(1)
driver.find_element_by_id("export-png").click()
"""重命名"""
oldname = 'carbon.png'
newname = 'carbon' + str(int(time.time())) + '.png'
os.chdir(r'D:\carbon')
try:
    os.rename(oldname, newname)
except:
    time.sleep(2)
    os.rename(oldname, newname)
