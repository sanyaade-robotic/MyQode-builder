# -*- coding: utf-8 -*-
import socket
import json
import time

client = socket.socket()
host = '127.0.0.1'
port = 12345
addr = (host, port)
client.connect(addr)


class Qmind:
    def __init__(self, name):
        self.name = name
    # 动作
    def set_motor(self, direction, speed):
        d = {'event': 'set_motor', 'data': {'WHEEL': direction, 'TYPE': 1, 'SPEED': speed}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    # 外观
    def show_matrix(self, port):
        d = {'event': 'hide_matrix', 'data': {'PORT': port, 'VALUE': "[['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],['1','1','1','1','1','1','1','1','1','1','1','1','1','1',],]"}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def hide_matrix(self, port):
        d = {'event': 'show_matrix', 'data': {'PORT': port, 'VALUE': "[['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],['0','0','0','0','0','0','0','0','0','0','0','0','0','0',],]"}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def gs_matrix_rgb_led4(self,port,data):
        values = {'PORT': port,'COLOR': data}
        post_request('/gs_matrix_rgb_led4', values)

    def set_led(self, direction, r, g, b):
        if direction == 0:
            light = 2
        elif direction == 1:
            light = 0
        else:
            light = 1

        d = {'event': 'set_led', 'data': {'LIGHT': light, 'RED': r, 'GREEN':g, 'BLUE': b}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def set_ultrasonic(self, port, r, g, b):
        d = {'event': 'set_ultrasonic', 'data': {'PORT': port, 'RED': r, 'GREEN': g, 'BLUE': b}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    # 声音
    def set_sound(self, tune, duration):
        d = {'event': 'set_sound', 'data': {'SOUND': tune, 'SECOND': duration}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    # 传感器
    def get_ultrasonic(self, port):
        return 0

    def get_line_patrol(self, port):
        return 0

    def get_sound(self, port):
        return 0

    def get_light(self, port):
        return 0

        #获取陀螺仪传感器数值
    def getSensingGyroValue(self,port,type):
        values = {'PORT': port,'type':type}
        time.sleep(0.3)
        result = post_request('/getSensingGyroValue', values)
        return result

    def gsSensingColor(self,port,type):
        values = {'PORT': port, 'COLOR': type}
        time.sleep(0.3)
        result = post_request('/gsSensingColor', values)
        return result

    def gsSensingColorGrey(self,port):
        values = {'PORT': port}
        time.sleep(0.3)
        result = post_request('/gsSensingColorGrey', values)
        return result

    def shows_digital1(self, port, num):
        d = {'event': 'shows_digital1', 'data': {'PORT': port, 'NUMBER': num}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)
    
    def shows_digital2(self, port, mins, sec):
        d = {'event': 'shows_digital2', 'data': {'PORT': port, 'M': mins, 'S': sec}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def shows_digital3(self, port):
        d = {'event': 'shows_digital3', 'data': {'PORT': port}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def shows_digital4(self, port):
        d = {'event': 'shows_digital4', 'data': {'PORT': port}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def set_led_animal(self, port, animalType):
        d = {'event': 'set_led_animal', 'data': {'PORT': port, 'ANIMATION': animalType}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def set_led_color(self, port, location, r, g, b):
        d = {'event': 'set_led_color', 'data': {'PORT': port, 'LEDNUM': location, 'RED': r, 'GREEN': g, 'BLUE': b}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)

    def set_led_color(self, port, location):
        d = {'event': 'set_led_color', 'data': {'PORT': port, 'LEDNUM': location}}
        s = json.dumps(d)
        client.send(s)
        time.sleep(1)
