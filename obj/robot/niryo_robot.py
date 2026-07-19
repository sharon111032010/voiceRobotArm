from pyniryo import *


class NiryoController:


    def __init__(self, ip):

        self.robot = NiryoRobot(ip)

        self.robot.calibrate_auto()
        self.robot.update_tool()
        self.robot.clear_collision_detected()

        self.robot.move_to_home_pose()


        self.ROLL = 0
        self.PITCH = 1.57
        self.YAW = 0


        self.SAFE_Z = 0.15
        self.PICK_Z = 0.10


        self.AREA = {

            1:(0.30,-0.10),
            2:(0.30,0),
            3:(0.30,0.10),

            4:(0.20,-0.10),
            5:(0.20,0),
            6:(0.20,0.10)

        }



    def move_pose(self,x,y,z):

        self.robot.move_linear_pose(
            x,y,z,
            self.ROLL,
            self.PITCH,
            self.YAW
        )



    def move_area(self,area):

        x,y=self.AREA[area]

        self.move_pose(
            x,
            y,
            self.SAFE_Z
        )



    def down(self,area):

        x,y=self.AREA[area]

        self.move_pose(
            x,
            y,
            self.PICK_Z
        )



    def up(self,area):

        x,y=self.AREA[area]

        self.move_pose(
            x,
            y,
            self.SAFE_Z
        )



    def open_gripper(self):

        self.robot.release_with_tool()



    def close_gripper(self):

        self.robot.grasp_with_tool()



    def pick(self,area):

        self.move_area(area)

        self.open_gripper()

        self.down(area)

        self.close_gripper()

        self.up(area)



    def put(self,area):

        self.move_area(area)

        self.down(area)

        self.open_gripper()

        self.up(area)



    def move_block(self,start,end):

        print(
            f"搬運 {start} -> {end}"
        )

        self.pick(start)

        self.put(end)



    def home(self):

        self.move_area(5)



    def close(self):

        self.robot.close_connection()