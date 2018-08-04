cmake_minimum_required(VERSION 3.11.0)

set(CMAKE_VERBOSE_MAKEFILE ON)

project(cgal_mesher)

set(SOURCE_DIR "src/mesher")
include_directories(${SOURCE_DIR})
set(SOURCES "${SOURCE_DIR}/math.cpp")

add_subdirectory(lib/pybind11)
pybind11_add_module(cgal_mesher ${SOURCES} "${SOURCE_DIR}/bindings.cpp")

