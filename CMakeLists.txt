cmake_minimum_required(VERSION 3.5)

project(sls VERSION 0.0.1 LANGUAGES C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(CMAKE_C_COMPILER gcc)
string(APPEND CMAKE_C_FLAGS "-Wall -Wextra -Wno-unused-parameter -Wendif-labels")

add_executable(sls ${PROJECT_SOURCE_DIR}/src/sls.c)
