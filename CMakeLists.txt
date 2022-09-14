cmake_minimum_required(VERSION 3.10)
project(fmt)

find_package(Python COMPONENTS Interpreter)

# Use waf to resolve dependencies
if(NOT DEFINED STEINWURF_RESOLVE)
  message(STATUS "Resolving dependencies...")
  execute_process(
    COMMAND ${Python_EXECUTABLE} waf resolve ${STEINWURF_RESOLVE_OPTIONS}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    RESULT_VARIABLE STATUS)

  if(STATUS AND NOT STATUS EQUAL 0)
    message(FATAL_ERROR "Failed: ${STATUS}")
  endif()

  set(STEINWURF_RESOLVE "${CMAKE_CURRENT_SOURCE_DIR}/resolve_symlinks")
  set(STEINWURF_TOP_NAME fmt)
endif()

# Define library
add_library(fmt INTERFACE)
target_compile_features(fmt INTERFACE cxx_std_14)

target_compile_definitions(
  fmt INTERFACE FMT_HEADER_ONLY)

# GCC 6.3 breaks with constexpr
target_compile_definitions(
  fmt INTERFACE FMT_USE_CONSTEXPR=0)

target_include_directories(
  fmt INTERFACE "${STEINWURF_RESOLVE}/fmt-source/include")

add_library(steinwurf::fmt ALIAS fmt)

# Install headers
install(
  DIRECTORY "${STEINWURF_RESOLVE}/fmt-source/include"
  DESTINATION ${CMAKE_INSTALL_PREFIX}/include
  FILES_MATCHING
  PATTERN *.hpp)

# Is top level project?
if(${CMAKE_PROJECT_NAME} STREQUAL ${PROJECT_NAME})
  # Build executables
  add_executable(format example/main.cpp)
  target_link_libraries(format fmt)
endif()
