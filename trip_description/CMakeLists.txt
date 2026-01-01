cmake_minimum_required(VERSION 3.5)
project(trip_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY urdf meshes launch rviz config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
