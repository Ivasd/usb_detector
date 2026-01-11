import os
import sys
from ament_index_python.packages import get_package_share_directory
sys.path.append(os.path.join(get_package_share_directory('rm_vision_bringup'), 'launch'))


def generate_launch_description():

    from common import launch_params, node_params
    from launch_ros.actions import Node
    from launch import LaunchDescription
    
    usb_cam_config_path = os.path.join(
        get_package_share_directory('rm_vision_bringup'),
        'config',
        'usb_params.yaml'
    )

    usb_cam_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        name='usb_cam',
        namespace='usb_cam_1',
        parameters=[usb_cam_config_path],
        emulate_tty=True,
        output='both',
    )
    detector_node = Node(
        package='usb_detector',
        executable='usb_detector_node',
        emulate_tty=True,
        output='both',
        parameters=[node_params],
        arguments=['--ros-args', '--log-level',
                   'armor_detector:='+launch_params['detector_log_level']],
    )

    return LaunchDescription([
        usb_cam_node,
        detector_node,
    ])
