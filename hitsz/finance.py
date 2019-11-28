#!/usr/bin/env python3
# encoding=utf-8


import os
import platform
from time import sleep
from random import choice
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
log_dir = "https://sso.hitsz.edu.cn:7002/cas/login?service=http%3A%2F%2Fzcgl.hitsz.edu.cn%2Fsfw_hitsz%2Flogin%2Findex"
cw_dir = "http://zcgl.hitsz.edu.cn/sfw/user/index.jsp?_t=1573223503040"


class Work:
    def __init__(self):
        pass

    def work(self):
        driver = webdriver.Chrome()
        driver.get(log_dir)
        driver.maximize_window()

        # 定位到资产列表
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("username").send_keys('20038002')
        driver.find_element_by_id("password").send_keys("W@26033618")
        driver.find_element_by_class_name('login_box_landing_btn').click()
        sleep(1)
        # 这个按钮是动态id, 也就是说点击之后url不变, 这就导致这个按钮新产生的按钮无法查找??
        driver.find_element_by_id('popedom_3010100').click()
        driver.switch_to.frame('assets_index_mainContent')
        sleep(3)

        # # 搜索符合条件的资产
        js = 'document.querySelectorAll("select")[0].style.display="block";'
        driver.execute_script(js)
        search = driver.find_element_by_css_selector("[class='form-element selectinput']")
        keyword = Select(search.find_element_by_tag_name('select'))
        keyword.select_by_value('roomName')
        select_word = driver.find_element_by_class_name("selectinput-input").find_element_by_class_name("form-control")
        select_word.send_keys('C栋')
        search_class = 'btn bg-primary-400 btn-xs btn-shadow querybutton'
        driver.find_element_by_css_selector("[class='{}']".format(search_class)).click()

        # Select(driver.find_element_by_css_selector("[class='form-control input-sm']")).select_by_index(0)
        devices = driver.find_elements_by_class_name('odd')
        devices.extend(driver.find_elements_by_class_name('even'))

        # 对资产进行操作
        while len(devices) != 0:
            try:
                devices = driver.find_elements_by_class_name('odd')
                devices.extend(driver.find_elements_by_class_name('even'))
                devices[0].find_elements_by_class_name('table-index-input')[0].click()
                sleep(2)
                # 批量修改按钮
                # set = driver.find_element_by_css_selector("[class='btn btn-default btn-sm  btn-shadow']")
                driver.find_element_by_class_name('icon-pen').click()
                sleep(2)

                driver.switch_to.parent_frame()
                driver.switch_to.frame('_inner')
                local = driver.find_element_by_css_selector("[class='form-control ui-autocomplete-input']")
                orign_value = local.get_attribute('value')
                if "C栋" in orign_value:
                    local.clear()
                    local.send_keys("L栋1717室")
                    remark = driver.find_element_by_name('remarkMine')
                    remark.clear()
                    remark.send_keys('2019年10月从C栋305C搬到了L栋1717室')
                else:
                    remark = driver.find_element_by_name('remarkMine')
                    ramark.get_attribute('value')
                    remark.clear()
                    remark.send_keys('2019.11.09已审查')

                save_class = 'btn btn-default btn-sm  btn-shadow'
                driver.find_element_by_css_selector("[class='{}']".format(save_class)).click()
                sleep(3)
                driver.switch_to.parent_frame()
                driver.switch_to.frame('assets_index_mainContent')
                sleep(2)

            except Exception as e:
                print(e)
                continue
        pass

if __name__ == "__main__":
    c = Work()
    c.work()
