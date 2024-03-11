# mobi_ros2
Test:\
Kopiere den **mobi_ros2** Ordner in den **src** Ordner. (ros2_ws/src) \
Führe die folgenden Zeilen im Terminal in deinem **WORKSPAC**E Ordner aus:

```shell
cd ~/ros2_ws
colcon build --packages-select mobi_ros2
source install/setup.bash
ros2 launch mobi_ros2 gazebo.launch.py
```
