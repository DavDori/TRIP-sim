# TRIP Robot Description (ROS 2 + Gazebo Classic)

This package contains the URDF/Xacro description of the **TRIP** robot and supports
spawning the robot in **Gazebo Classic** using ROS 2 and RViz display.

---

## Package Structure

```text
trip_description/
├── CMakeLists.txt
├── package.xml
├── meshes/
│   ├── base_link.dae
│   └── base_link.stl
├── urdf/
│   └── trip.urdf.xacro
├── launch/
│   └── gazebo.launch.py
└── rviz/

## Required

Install the necessary ROS 2 packages:

```bash
sudo apt install ros-humble-gz-ros2-control \
                 ros-humble-ros2-controllers \
                 ros-humble-ros2-control
```

## Setup

Set the environment variable TRIP_PATH to your project path to ensure proper operation:

```bash
source setup_env.sh
```

## Run

### Simulation

Launch the simulation with:

```bash
ros2 launch trip_description gazebo.launch.py 
```

To enable RViz visualization, set the use_rviz variable:

```bash
ros2 launch trip_description gazebo.launch.py use_rviz:=true
```

### Display robot data

To display real robot data and state:

```bash
ros2 launch trip_description gazebo.launch.py 
```
