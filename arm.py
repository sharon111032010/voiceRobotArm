from pyniryo import *
import time
robot = NiryoRobot("192.168.0.4")  # connect to Niryo arm by socket

robot.calibrate_auto()  # 動作校正
robot.update_tool()
robot.move_to_home_pose()
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


init_pose=PoseObject(0.3, 0.0, 0.15, 0.0,0.1,0.1)

#示範用法:
#init_pose=PoseObject(move_X(0.3),move_Y(0.2),move_Z(0.15),0.0,1.57,0.0)
robot.move_pose(init_pose)



#pose_read = robot.get_pose()  # x = 0.2001, y = 0.1000, z = 0.2499 roll = 0.604, pitch = 1.570, yaw = 0.605
# print(pose_read)
x = 0.2  #
y = 0.0  # 爪具遠近
z = 0.3  # 爪具高度

# 笛卡爾座標
roll = 0.0   # 爪具自轉軸
pitch = 1.57 # 爪具的上下軸
yaw = 0.0

print("release_with_tool")
#robot.release_with_tool()
print("move pose")
#				        x      y    z
robot.move_linear_pose(0.2  , 0.0, 0.15, 0.0, 1.57, 0.0)
print("grasp_with_tool")
robot.grasp_with_tool() # 控制爪具抓取

time.sleep(0.5)
print("move pose")
robot.move_linear_pose(0.2, 0.1, 0.15, 0.0, 1.57, 0.0)
robot.release_with_tool() # 控制爪具釋放

init_pose=PoseObject(0.3, 0.0, 0.15, 0.0,0.1,0.1)
robot.move_pose(init_pose)


# 這是原點座標
time.sleep(0.5)
robot.move_linear_pose(0.2  , 0.0, 0.15, 0.0, 1.57, 0.0)
print("grasp_with_tool")
robot.grasp_with_tool() # 控制爪具抓取

robot.close_connection()