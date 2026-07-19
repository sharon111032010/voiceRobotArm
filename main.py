from pyniryo import *
import time

# ==========================
# 連線
# ==========================
robot = NiryoRobot("192.168.0.4")

robot.calibrate_auto()
robot.update_tool()
robot.clear_collision_detected()
robot.move_to_home_pose()

# ==========================
# 固定姿態
# ==========================
ROLL = 0.0
PITCH = 1.57
YAW = 0.0

SAFE_Z = 0.15      # 安全高度
PICK_Z = 0.10      # 抓取高度

# ==========================
# 六個區域座標
# (請依實際量測修改)
# ==========================
AREA = {
    1: (0.20,  0.10),
    2: (0.20,  0.00),
    3: (0.20, -0.10),
    4: (0.30,  0.10),
    5: (0.20,  0.00),   # Home
    6: (0.30, -0.10),
}

def move_pose(x, y, z):
    robot.move_linear_pose(
        x,
        y,
        z,
        ROLL,
        PITCH,
        YAW
    )
def move_area(area):
    x, y = AREA[area]
    move_pose(x, y, SAFE_Z)

def open_gripper():
    robot.release_with_tool()

def close_gripper():
    robot.grasp_with_tool()

def down(area):
    x, y = AREA[area]
    move_pose(x, y, PICK_Z)

def up(area):
    x, y = AREA[area]
    move_pose(x, y, SAFE_Z)
    
def home():
    move_area(5)

def pick(area):

    move_area(area)

    open_gripper()

    down(area)

    close_gripper()

    up(area)

def put(area):

    move_area(area)

    down(area)

    open_gripper()

    up(area)

def move_block(start, end):

    pick(start)

    put(end)
try:

    home()

    # move_block(6, 4)

    # move_block(3, 1)

    move_block(2, 5)

    home()
    robot.close_connection()
except :
    print("err")