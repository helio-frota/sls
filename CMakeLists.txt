cmake_minimum_required(VERSION 3.10)

project(sls VERSION 0.0.1 LANGUAGES C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED 11)

set(CMAKE_C_COMPILER gcc)
set(copts "-Wall -Wextra")
set(CMAKE_C_FLAGS_DEBUG_INIT ${copts})

add_executable(sls ${PROJECT_SOURCE_DIR}/src/sls.c)
