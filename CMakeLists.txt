cmake_minimum_required(VERSION 3.15...3.19)

project(pylira_simd VERSION "0.0.1")


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c
            "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()



# Now we can find pybind11
find_package(pybind11 CONFIG REQUIRED)
find_package(Python COMPONENTS Interpreter Development)
find_package(Python3)


include_directories(src/extern/pybind11/include)

#add_subdirectory(src/extern/pybind11)
add_subdirectory(src/extern/highway)

# Python method:
Python_add_library(_pylira_simd MODULE src/main.cpp)

add_dependencies(_pylira_simd hwy)
target_link_libraries(_pylira_simd INTERFACE pybind11::headers hwy)

cmake_policy(SET CMP0069 NEW)
# target_link_libraries(_pylira_simd hwy)
set_target_properties(_pylira_simd PROPERTIES
                                INTERPROCEDURAL_OPTIMIZATION TRUE
                                CXX_VISIBILITY_PRESET internal
                                VISIBLITY_INLINES_HIDDEN ON)
# pybind11_add_module(_pylira_simd MODULE src/main.cpp)
# add_dependencies(_pylira_simd hwy)


# target_link_libraries(_pylira_simd hwy)

target_compile_definitions(_pylira_simd PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS _pylira_simd DESTINATION .)
