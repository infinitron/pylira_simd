cmake_minimum_required(VERSION 3.15...3.19)

project(pylira_simd VERSION "0.2.0")


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

find_package(pybind11 CONFIG REQUIRED)
find_package(Python3)

include_directories(/usr/local/include /usr/share/R/include/)
include_directories(/usr/include /usr/include/R /usr/include/R/include)
include_directories(src/extern/pybind11/include)
include_directories(src/extern/lira_simd)
include_directories(src/extern/highway)

add_subdirectory(src/extern/highway)
link_directories(/usr/lib/R/lib)

# lira.cpp file needs its absolute location for dynamic dispatch
get_filename_component(_LIRA_SIMD_CPP_FILE_ src/extern/lira_simd/lira.cpp REALPATH)
add_compile_definitions(_LIRA_SIMD_CPP_FILE_="${_LIRA_SIMD_CPP_FILE_}")

pybind11_add_module(_pylira_simd MODULE src/main.cpp)

add_dependencies(_pylira_simd hwy)
add_compile_options(-fPIC -O2)      
target_link_libraries(_pylira_simd PUBLIC hwy R Rmath pthread tbb)


target_compile_definitions(_pylira_simd PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS _pylira_simd DESTINATION .)
