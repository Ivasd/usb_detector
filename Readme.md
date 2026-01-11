# 感知相机模块
## 基于君码和usb_cam的全向感知相机模块

- usb相机内参: src/rm_vision/rm_vision_bringup/config/usb_camera_info
- usb相机配置：src/rm_vision/rm_vision_bringup/config/usb_params.yaml

运行：
```
source install/setup.zsh
ros2 launch rm_vision_bringup no_hardware.launch.py
```
foxglove:
```
source install/setup.bash
ros2 launch foxglove_bridge foxglove_bridge_launch.xml port:=8765
```