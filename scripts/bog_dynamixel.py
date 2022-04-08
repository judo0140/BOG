#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

from dynamixel_sdk import * # Uses Dynamixel SDK library

MY_DXL = 'X_SERIES'   

# Control table address
if MY_DXL == 'X_SERIES' or MY_DXL == 'MX_SERIES':
    ADDR_TORQUE_ENABLE          = 64
    ADDR_GOAL_POSITION          = 116
    ADDR_GOAL_VELOCITY          = 104
    ADDR_PRESENT_POSITION       = 132
    ADDR_PRESENT_VELOCITY       = 128
    ADDR_PRO_TORQUE_ENABLE      = 64               
    ADDR_PRO_GOAL_POSITION      = 116
    ADDR_PRO_PRESENT_POSITION   = 132
    ADDR_PROFILE_VELOCITY       = 112
    ADDR_PROFILE_ACCELERATION   = 108
    DXL_MINIMUM_POSITION_VALUE  = 0         # Refer to the Minimum Position Limit of product eManual
    DXL_MAXIMUM_POSITION_VALUE  = 4095      # Refer to the Maximum Position Limit of product eManual
    BAUDRATE                    = 57600
    ADDR_PRO_GOAL_VELOCITY      = 104
    ADDR_PRO_OPERATING_MODE     = 11
    DXL_POSITION_MODE           = 4
    DXL_VELOCITY_MODE           = 1

PROTOCOL_VERSION            = 2.0

DXL_ID                      = 1

DEVICENAME                  = '/dev/ttyACM0'

TORQUE_ENABLE               = 1     # Value for enabling the torque
TORQUE_DISABLE              = 0     # Value for disabling the torque
DXL_MOVING_STATUS_THRESHOLD = 10    # Dynamixel moving status threshold

index = 0
dxl_goal_position = [682, 1364, 2046, 2728, 3410, 4095, 4777, 5459, 6141, 6823, 7505, 8190, 8872, 9554, 10236, 10918, 11600, 12285]  

portHandler = PortHandler(DEVICENAME)

packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    quit()

# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

# Set dxl's operating mode = position mode
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_PRO_OPERATING_MODE, DXL_POSITION_MODE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))


# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

# Write profile velocity
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_PROFILE_VELOCITY, 30)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Write profile acceleration
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_PROFILE_ACCELERATION, 1)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

class dynamixel:
    def __init__(self):
	rospy.Subscriber("guide1_position", String, self.callback1)
	rospy.Subscriber("guide2_position", String, self.callback2)
	rospy.Subscriber("guide3_position", String, self.callback3)

	self.guide1_position_str = "side"
	self.guide2_position_str = "side"
	self.guide3_position_str = "side"

	rospy.Subscriber("dynamixel_position", String, self.add_callback)
	self.dynamixel_position_str = "none"

    def add_callback(self, data):
	rospy.loginfo("I heard %s", data.data)
	self.dynamixel_position_str = data.data

	if self.guide1_position_str == "side" and self.guide2_position_str == "side" and self.guide3_position_str == "side":
	    if self.dynamixel_position_str == "d0":
		index = 0
	    elif self.dynamixel_position_str == "d1":
		index = 1
	    elif self.dynamixel_position_str == "d2":
		index = 2
	    elif self.dynamixel_position_str == "d3":
		index = 3
	    elif self.dynamixel_position_str == "d4":
		index = 4
	    elif self.dynamixel_position_str == "d5":
		index = 5
	    elif self.dynamixel_position_str == "d6":
		index = 6
	    elif self.dynamixel_position_str == "d7":
		index = 7
	    elif self.dynamixel_position_str == "d8":
		index = 8
	    elif self.dynamixel_position_str == "d9":
		index = 9
	    elif self.dynamixel_position_str == "d10":
		index = 10
	    elif self.dynamixel_position_str == "d11":
		index = 11
	    elif self.dynamixel_position_str == "d12":
		index = 12
	    elif self.dynamixel_position_str == "d13":
		index = 13
	    elif self.dynamixel_position_str == "d14":
		index = 14
	    elif self.dynamixel_position_str == "d15":
		index = 15
	    elif self.dynamixel_position_str == "d16":
		index = 16
	    elif self.dynamixel_position_str == "d17":
		index = 17

	    # Write goal position
	    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, dxl_goal_position[index]+130)
	    if dxl_comm_result != COMM_SUCCESS:
	        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
	    elif dxl_error != 0:
	        print("%s" % packetHandler.getRxPacketError(dxl_error))

	else :
	    print("Check the table")
	    return

    def callback1(self, data):
	rospy.loginfo("I heard the CUP1 is on %s", data.data)
	self.guide1_position_str = data.data

    def callback2(self, data):
	rospy.loginfo("I heard the CUP2 is on %s", data.data)
	self.guide2_position_str = data.data

    def callback3(self, data):
	rospy.loginfo("I heard the CUP3 is on %s", data.data)
	self.guide3_position_str = data.data

if __name__ == '__main__':

    rospy.init_node('dynamixel', anonymous=False)
    dynamixel()
    rospy.spin()
