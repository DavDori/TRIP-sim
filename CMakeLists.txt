cmake_minimum_required(VERSION 3.5)
project(trip_description)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(urdf REQUIRED)
find_package(tf2 REQUIRED)


install(DIRECTORY 
  urdf 
  meshes 
  launch 
  rviz 
  config
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(
  geometry_msgs
  nav_msgs
  rclcpp
  sensor_msgs
  tf2
)

ament_package()
