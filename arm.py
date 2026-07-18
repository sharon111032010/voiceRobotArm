# 匯入 套件 pyniryo 是  控制套件
from pyniryo import *
import time 

robot = NiryoRobot("192.168.0.4")  # connect to Niryo arm by socket

robot.calibrate_auto()  # 動作校正 找每個馬達的零點 /確認 關節位置 
robot.update_tool() #更新 機械手臂上裝的是哪個爪子
robot.clear_collision_detected()
robot.move_to_home_pose() #回到預設安全手勢 斜直線 

#規範 X  Y  Z可以移動的範圍
def move_X(x:float):
	if not (0.2<= x<=0.4):
		print(f"x值{x}超出範圍")
		robot.close_connection()
	return x

def move_Y(y:float):
	if not (-0.3<=y<=0.3):
		robot.close_connection()
	return y

def move_Z(z:float):
	if not (0.1<= z <= 0.35):
		print(f"z值{z}超出範圍")
		robot.close_connection()
	return z  


x = 0.2  #
y = 0.0  # 爪具遠近
z = 0.15  # 爪具高度

POINTX = 0.2
POINTY = 0.0
POINTZ = 0.15
# 笛卡爾座標

roll = 0.0   # 爪具自轉軸
pitch = 1.57 # 爪具的上下軸
yaw = 0.0

# robot.move_linear_pose(x,y,z, roll, pitch,yaw)
# robot.release_with_tool() #開爪子 
# robot.grasp_with_tool() #關爪子 
def moveOn(Mx=x,My=y,Mz=z):
	robot.move_linear_pose(Mx,My,Mz,roll,pitch,yaw)
def moveMz(Mz):
	robot.move_linear_pose(x,y,Mz, roll, pitch,yaw)
def moveMy(My):
	robot.move_linear_pose(x,My,z, roll, pitch,yaw)
def moveMx(Mx):
	robot.move_linear_pose(Mx,y,z, roll, pitch,yaw)

def close():
	robot.grasp_with_tool()
def open():
	robot.release_with_tool()

# print(joints)

# 這是原點座標
time.sleep(0.1)
''' 前後 左右 上下 '''
# robot.move_linear_pose(0.2  , 0.0, 0.15, 0.0, 1.57, 0.0)
def setSide():
    global x, y, z
    x = 0.2
    y = 0.0
    z = 0.15
def go ():
	robot.move_linear_pose(x,y,z, roll, pitch,yaw)
def home ():
	robot.move_linear_pose(POINTX,POINTY,POINTZ, roll, pitch,yaw)
def catch ():
	robot.release_with_tool() #開爪子 
	#robot.move_linear_pose(0.2  , 0.0, 0.15, 0.0, 1.57, 0.0)
	#print("向下 0.15")

	robot.move_linear_pose(0.2  , 0.0, 0.10, 0.0, 1.57, 0.0)
	print("向下 到10")
	robot.grasp_with_tool()
	print("上升到0.15")
	robot.move_linear_pose(0.2  , 0.0, 0.15, 0.0, 1.57, 0.0)
	robot.grasp_with_tool()
def turnRight():
	robot.move_linear_pose(0.2,0.1,0.15, 0.0,1.57,0.0)
	robot.move_linear_pose(0.2,0.1,0.10, 0.0,1.57,0.0)
def turnUp():
	robot.move_linear_pose(0.2,0.1,0.13, 0.0,1.57,0.0)

home()
# moveMz(0.10)
catch()
# 放第四象限
y=-0.1
go()
# openClaw()
z=0.10
go()
open()
z=0.15
go()
home()
# 回中心





# turnRight()
# putdown()
# turnUp()
# close()
# home()
# close()
robot.close_connection()