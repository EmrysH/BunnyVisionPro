import time
from pathlib import Path
import numpy as np
from yourdfpy import URDF
from bunny_teleop.bimanual_teleop_client import TeleopClient
from bunny_teleop.init_config import BimanualAlignmentMode

# TASK_NAME = "bimanual_grasp"


def get_qpos_list():
    asset_path = (Path(__file__).parent.parent / "BunnyVisionPro/examples/assets").resolve()

    # Load a yourdfpy instance only for forward kinematics computation

    # left_urdf_path = asset_path / "urdf/assembly/xarm7_ability/xarm7_ability_left_hand.urdf"
    left_urdf_path = asset_path / "urdf/assembly/xarm7_ability/hans_left_hand.urdf"
    left_robot = URDF.load(str(left_urdf_path))

    # right_urdf_path = asset_path / "urdf/assembly/xarm7_ability/xarm7_ability_right_hand.urdf"
    right_urdf_path = asset_path / "urdf/assembly/xarm7_ability/hans_left_hand.urdf"
    right_robot = URDF.load(str(right_urdf_path))

    # Robot initial state
    robots = [left_robot, right_robot]
    joint_names = tuple(robot.actuated_joint_names for robot in robots)


    # xarm7
    # init_qpos = [-0.03141593, 0.13439035, 0.03141593, 0.23911011, 3.14159265, 1.46433124, -0.00349066] + [0] * 10

    # hans
    init_qpos = [-3.15, 0.399, -1.7, 0.0012, 0.512, -3.14] + [0] * 10

    init_qpos = np.array(init_qpos)
    left_init_qpos = init_qpos
    right_init_qpos = init_qpos

    bimanual_init_qpos = (left_init_qpos, right_init_qpos)

    client = TeleopClient(port=5500, cmd_dims=(16, 16), host="localhost")
    client.send_init_config(
        robot_base_pose=(
            np.array([0, 0.4, 0, 1, 0, 0, 0]),
            np.array([0, -0.4, 0, 1, 0, 0, 0]),
        ),
        init_qpos=bimanual_init_qpos,
        joint_names=joint_names,
        bimanual_alignment_mode=BimanualAlignmentMode.ALIGN_SEPARATELY,  # ALIGN_CENTER, ALIGN_LEFT, ALIGN_RIGHT, ALIGN_SEPARETELY
        align_gravity_dir=True,
    )

    print("============= Waiting for server to start...")
    client.wait_for_server_start()
    print("============= Server started.")

    try:
        while True:
            ee_pose = client.get_ee_pose()
            print("qpos_list:", ee_pose)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Keyboard interrupt, shutting down.")


if __name__ == "__main__":
    get_qpos_list()
