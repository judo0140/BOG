#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from time import sleep
import RPi.GPIO as GPIO

PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 22  # Controller Enable Bit (High to Enable / LOW to Disable).

GPIO.setmode(GPIO.BCM)

GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)


print('Initialization Completed')

durationFwd = 16910 # This is the duration of the motor spinning. used for forward direction
durationBwd = 16910 # This is the duration of the motor spinning. used for reverse direction

delay = 0.000001

class guide1:
    def __init__(self):
        rospy.Subscriber("table_mode", String, self.callback)
	rospy.Subscriber("dynamixel_position", String, self.add_callback)
	self.pub = rospy.Publisher('guide1_position', String, queue_size=10)
	self.guide1_position_str = raw_input("Where is the CUP1? (side/center) : ")
	self.dynamixel_position_str = raw_input("Where is the teapot? : ")
	self.table_mode_str = "none"
	rospy.loginfo(self.guide1_position_str)
	self.pub.publish(self.guide1_position_str)
	rospy.sleep(rospy.Duration(0.2))
	print("Send message : The CUP1 is on the %s of table" % (self.guide1_position_str))

    def add_callback(self, data):
	rospy.loginfo("I heard teapot's position is %s", data.data)
	self.dynamixel_position_str = data.data

    def callback(self, data):
        rospy.loginfo("I heard %s", data.data)

        if data.data == "Hierarchical 1" or data.data == "Flat":
	    if self.guide1_position_str == "center":
	        self.reverse()
	        self.guide1_position_str = "side"
	        rospy.loginfo(self.guide1_position_str)
	        self.pub.publish(self.guide1_position_str)
	        rospy.sleep(rospy.Duration(0.2))
	        print("Send message : The CUP1 is on the side of table.")
	    elif self.guide1_position_str == "side":
		print("WRONG COMMAND")
		return
	    self.table_mode_str = data.data
	elif data.data == "Hierarchical 2" or data.data == "Hierarchical 3":
	    if self.guide1_position_str == "center":
	        sleep(4)
	        self.reverse()
	        self.guide1_position_str = "side"
	        rospy.loginfo(self.guide1_position_str)
	        self.pub.publish(self.guide1_position_str)
	        rospy.sleep(rospy.Duration(0.2))
	        print("Send message : The CUP1 is on the side of table.")
	    elif self.guide1_position_str == "side":
		print("WRONG COMMAND")
		return
	    self.table_mode_str = data.data
	elif data.data == "Return cups h":
	    if self.dynamixel_position_str == "d0" or self.dynamixel_position_str == "d6" or self.dynamixel_position_str == "d12":
		if self.guide1_position_str == "side":
		    if self.table_mode_str == "Hierarchical 1" or self.table_mode_str == "none":
		        self.forward()
		    elif self.table_mode_str == "Hierarchical 2" or self.table_mode_str == "Hierarchical 3":
			sleep(4)
			self.forward()
		    elif self.table_mode_str == "Flat":
			print("WRONG COMMAND")
			return
		    self.guide1_position_str = "center"
		    rospy.loginfo(self.guide1_position_str)
		    self.pub.publish(self.guide1_position_str)
		    rospy.sleep(rospy.Duration(0.2))
		    print("Send message : The CUP1 is on the center of table.")
		elif self.guide1_position_str == "center":
		    print("WRONG COMMAND")
		    return
	    else:
		print("Check the table")
		return
	elif data.data == "Return cups f":
	    if self.dynamixel_position_str == "d0" or self.dynamixel_position_str == "d6" or self.dynamixel_position_str == "d12":
		if self.guide1_position_str == "side":
		    if self.table_mode_str == "Flat" or self.table_mode_str == "none":
		        self.forward()
		        self.guide1_position_str = "center"
		        rospy.loginfo(self.guide1_position_str)
		        self.pub.publish(self.guide1_position_str)
		        rospy.sleep(rospy.Duration(0.2))
		        print("Send message : The CUP1 is on the center of table.")
		    else:
			print("WRONG COMMAND")
		elif self.guide1_position_str == "center":
		    print("WRONG COMMAND")
		    return
	    else:
		print("Check the table")
		return

    def forward(self):
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(DIR, GPIO.LOW)
        for x in range(durationFwd): 
            GPIO.output(PUL, GPIO.HIGH)
            sleep(delay)
            GPIO.output(PUL, GPIO.LOW)
            sleep(delay)
        GPIO.output(ENA, GPIO.LOW)
        return

    def reverse(self):
        GPIO.output(ENA, GPIO.HIGH)
        GPIO.output(DIR, GPIO.HIGH)
        for y in range(durationBwd):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(delay)
            GPIO.output(PUL, GPIO.LOW)
            sleep(delay)
        GPIO.output(ENA, GPIO.LOW)
        return


if __name__ == '__main__':

    rospy.init_node('guide1', anonymous=False)
    guide1()
    rospy.spin()
