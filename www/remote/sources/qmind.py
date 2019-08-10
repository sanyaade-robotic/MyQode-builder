# -*- coding: utf-8 -*-
import urllib
import urllib2
# import json
import time

url = 'http://127.0.0.1:12345'

def post_request(path, values):
	data = urllib.urlencode(values)
	req = urllib2.Request(url + path, data)
	response = urllib2.urlopen(req)
	result = response.read()
	# print result.decode()
	return result

class Qmind:
    def __init__(self, name):
        self.name = name
    # 设置电机前后左右运动,速度默认为80
    def set_motor_type(self, type, speed):
        values = {'TYPE': type, 'SPEED': speed}
        time.sleep(0.3)
        post_request('/set_motor_type', values)

    # 设置板载电机“M1/M2”“顺时针/逆时针”运动，以速度“输入框”
    def set_motor_direction(self, direction, clock, speed):
        values = {'DIRECTION': direction, 'CLOCK': clock, 'SPEED': speed}
        time.sleep(0.3)
        post_request('/set_motor_direction', values)

    # 停止板载电机运动
    def set_motor_stop(self):
        values = {}
        time.sleep(0.3)
        post_request('/set_motor_stop', values)

    #外置电机
    def set_external_motor(self,port,types,s1,s2):
        values = {'PORT': port, 'TYPE': types, 's1': s1,'s2':s2}
        time.sleep(0.3)
        post_request('/set_external_motor', values)

    #舵机
    def motion_steering_engine(self,port,types,s1,s2):
        values = {'PORT': port, 'TYPE': types, 's1': s1,'s2':s2}
        time.sleep(0.3)
        post_request('/motion_steering_engine', values)
    # 外观
    def show_matrix(self, port,value):
        values = {'PORT': port, 'VALUE':value}
        time.sleep(0.3)
        post_request('/show_matrix', values)

    def hide_matrix(self, port):
        values = {'PORT': port, 'VALUE': "[['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],]"}
        time.sleep(0.3)
        post_request('/hide_matrix', values)

    def set_led(self, direction, r, g, b):
        if direction == 0:
            light = 2
        elif direction == 1:
            light = 0
        else:
            light = 1

        values = {'LIGHT': light, 'RED': r, 'GREEN':g, 'BLUE': b}
        time.sleep(0.3)
        post_request('/set_led', values)

    def gs_matrix_rgb_led4(self,port,data):
        values = {'PORT': port,'COLOR': data}
        post_request('/gs_matrix_rgb_led4', values)

    def set_ultrasonic(self, port, r, g, b):
        values = {'PORT': port, 'RED': r, 'GREEN': g, 'BLUE': b}
        time.sleep(0.3)
        post_request('/set_ultrasonic', values)

    # 声音
    def set_sound(self, tune, duration):
        values = {'SOUND': tune, 'SECOND': duration}
        time.sleep(0.3)
        post_request('/set_sound', values)
    # 控制MP3模块
    def set_mp3_play(self,port,action):
        values = {'PORT': port, 'ACTION': action}
        time.sleep(0.3)
        post_request('/gs_sensing_mp3Play2', values)
    # 设置MP3模块音量
    def set_mp3_volume(self,port,sound):
        values = {'PORT': port, 'SOUND': sound}
        time.sleep(0.3)
        post_request('/gs_sensing_mp3Play3', values)
    # 获取超声波传感器的值
    def get_ultrasonic(self, port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_ultrasonic', values)
        result = float(result)
        return result
    # 获取巡线传感器的值
    def get_line_patrol(self, port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_line_patrol', values)
        result = float(result)
        return result
    # 获取声音传感器的值
    def get_sound(self, port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_sound', values)
        result = float(result)
        return result
    # 获取光线传感器的值
    def get_light(self, port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_light', values)
        result = float(result)
        return result
    # 获取温度传感器的值
    def get_temperature(self,port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_temperature', values)
        result = float(result)
        return result

    def get_temperature2(self, port, probe):
        values = {'PORT': port, 'PROBE': probe}
        time.sleep(0.3)
        result = post_request('/get_temperature2', values)
        result = float(result)
        return result

    # 获取湿度传感器的值
    def get_humidity(self,port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_humidity', values)
        result = float(result)
        return result
    # 获取人体红外传感器
    def get_infraredValue(self,port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/get_infraredValue', values)
        result = float(result)
        return result

    # 获取陀螺仪传感器的值
    # VALUETYPE x:0 y:1 z:2
    def getSensingGyroValue(self,port,type):
        values = {'PORT': port,'VALUETYPE':type}
        time.sleep(0.3)
        result = post_request('/getSensingGyroValue', values)
        result = float(result)
        return result
    # 获取颜色传感器的值
    # type 红色：red 黄色：yellow 绿色：green 蓝色：blue 紫色：purple 白色：white 无色：colorless
    def gsSensingColor(self,port,type):
        values = {'PORT': port, 'COLOR': type}
        time.sleep(0.3)
        result = post_request('/gsSensingColor', values)
        result = float(result)
        return result
    # 获取颜色传感器灰度值
    def gsSensingColorGrey(self,port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/gsSensingColorGrey', values)
        result = float(result)
        return result
    # 设置数码管
    def shows_digital1(self, port, num):
        values = {'PORT': port, 'NUMBER': num}
        time.sleep(0.3)
        post_request('/shows_digital1', values)
    
    def shows_digital2(self, port, mins, sec):
        values = {'PORT': port, 'M': mins, 'S': sec}
        time.sleep(0.3)
        post_request('/shows_digital2', values)

    def shows_digital3(self, port):
        values = {'PORT': port}
        time.sleep(0.3)
        post_request('/shows_digital3', values)

    def shows_digital4(self, port):
        values = {'PORT': port}
        time.sleep(0.3)
        post_request('/shows_digital4', values)

    def set_led_animal(self, port, animalType, speed):
        values = {'PORT': port, 'ANIMATION': animalType, 'SPEED': speed}
        time.sleep(0.3)
        post_request('/set_led_animal', values)

    def set_led_color(self, port, location, r, g, b):
        values = {'PORT': port, 'LEDNUM': location, 'RED': r, 'GREEN': g, 'BLUE': b}
        time.sleep(0.3)
        post_request('/set_led_color', values)

    def close_led(self, port, location):
        values = {'PORT': port, 'LEDNUM': location}
        time.sleep(0.3)
        post_request('/close_led', values)
