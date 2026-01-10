cmake_minimum_required(VERSION 3.5)
project(trip_description)

find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rclcpp REQUIRED)

install(DIRECTORY 
  urdf 
  meshes 
  launch 
  rviz 
  models 
  config
  DESTINATION share/${PROJECT_NAME}
)

# add_executable(trip_ctrl src/trip_ctrl.cpp)
# ament_target_dependencies(trip_ctrl
#   rclcpp
#   geometry_msgs
# )

# install(TARGETS
#   trip_ctrl
#   DESTINATION lib/${PROJECT_NAME}
# )

ament_package()
