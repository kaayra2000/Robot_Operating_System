#!/usr/bin/env python3

import rospy
import math
import numpy as np
import cv2 as cv
from sensor_msgs.msg import LaserScan
def callback(data):
	print(data.pose.pose.position.x)
	
def cb_scan(data):
	dizi=[]
	resim=np.zeros((360,360),dtype=np.uint8)
	for i,cor in enumerate(data.ranges):
		if not math.isinf(cor):
			dizi.append(kartezyen(cor,i))
	dizi=[(round((x+3.5)*51),round((y+3.5)*51)) for x,y in dizi]
	for x,y in dizi:
		resim[x][y]=255
	im=cv.cvtColor(resim,cv.COLOR_GRAY2BGR)
	cv.imshow("Naber",im)
	cv.waitKey(30)
	
def listener():

	rospy.init_node('listener' , anonymous=False)
	sub=rospy.Subscriber("/scan",LaserScan,cb_scan)
	rospy.spin()

def kartezyen(uzunluk,aci):
	x=uzunluk*math.cos(aci/180*math.pi)
	y=uzunluk*math.sin(aci/180*math.pi)
	return x,y

if __name__ == '__main__':
	listener()
