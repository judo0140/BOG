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

def master():
    pub_order_cup = rospy.Publisher('table_mode', String, queue_size=10)
    pub_order_teapot = rospy.Publisher('dynamixel_position', String, queue_size=10)
    rospy.init_node('master', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        print("Will you continue? (yes : press anykey /no : press ESC)")
	if getch() == chr(0x1b):
	    break
	while 1:
	    order_cup = raw_input("What is the table's mode? (h/f/rh/rf/x): ")
	    if order_cup == "h":
		position_number = raw_input("Where is the senior? (1/2/3): ")
		if position_number == "1":
		    mode_str = "Hierarchical 1"
		    rospy.loginfo(mode_str)
		    pub_order_cup.publish(mode_str)
		    rate.sleep()
		    print("Send message : The table's mode is 'Hierarchical 1'")
		elif position_number == "2":
		    mode_str = "Hierarchical 2"
		    rospy.loginfo(mode_str)
		    pub_order_cup.publish(mode_str)
		    rate.sleep()
		    print("Send message : The table's mode is 'Hierarchical 2'")
		elif position_number == "3":
		    mode_str = "Hierarchical 3"
	  	    rospy.loginfo(mode_str)
		    pub_order_cup.publish(mode_str)
		    rate.sleep()
		    print("Send message : The table's mode is 'Hierarchical 3'")
		else:
		    print("You write a wrong answer. Please press 'r'")
		    
	    elif order_cup == "f":
		mode_str = "Flat"
		rospy.loginfo(mode_str)
		pub_order_cup.publish(mode_str)
		rate.sleep()
		print("Send message : The table's mode is 'Flat'")
	    elif order_cup == "rh":
		return_str = "Return cups h"
		rospy.loginfo(return_str)
		pub_order_cup.publish(return_str)
		rate.sleep()
		print("Send message : Return cups h")
	    elif order_cup == "rf":
		return_str = "Return cups f"
		rospy.loginfo(return_str)
		pub_order_cup.publish(return_str)
		rate.sleep()
		print("Send message : Return cups f")
	    elif order_cup == "x":
	        break

	    while 1:
	        order_teapot = raw_input("Please enter the teapot's position (d0/d1/d2/d3/x): ")
	        if order_teapot == "d0":
		    position_str = "d0"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 0")
	        elif order_teapot == "d1":
		    position_str = "d1"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 1")
	        elif order_teapot == "d2":
		    position_str = "d2"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 2")
	        elif order_teapot == "d3":
		    position_str = "d3"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 3")
	        elif order_teapot == "d4":
		    position_str = "d4"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 4")
	        elif order_teapot == "d5":
		    position_str = "d5"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 5")
	        elif order_teapot == "d6":
		    position_str = "d6"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 6")
	        elif order_teapot == "d7":
		    position_str = "d7"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 7")
	        elif order_teapot == "d8":
		    position_str = "d8"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 8")
	        elif order_teapot == "d9":
		    position_str = "d9"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 9")
	        elif order_teapot == "d10":
		    position_str = "d10"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 10")
	        elif order_teapot == "d11":
		    position_str = "d11"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 11")
	        elif order_teapot == "d12":
		    position_str = "d12"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 12")
	        elif order_teapot == "d13":
		    position_str = "d13"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 13")
	        elif order_teapot == "d14":
		    position_str = "d14"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 14")
	        elif order_teapot == "d15":
		    position_str = "d15"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 15")
	        elif order_teapot == "d16":
		    position_str = "d16"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 16")
	        elif order_teapot == "d17":
		    position_str = "d17"
		    rospy.loginfo(position_str)
		    pub_order_teapot.publish(position_str)
		    rate.sleep()
		    print("Send message : Teapot's position is 17")
		elif order_teapot == "x":
		    break


if __name__ == '__main__':
    try:
        master()
    except rospy.ROSInterruptException:
        pass
