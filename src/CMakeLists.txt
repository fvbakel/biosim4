
FILE(GLOB MyCppSources ./*.cpp)
FILE(GLOB MyCppheaders ./*.h)

# TDO move to test
#list(REMOVE_ITEM MyCppSources "./unitTestBasicTypes.cpp")
#list(REMOVE_ITEM MyCppSources "./unitTestConnectNeuralNetWiringFromGenome.cpp")
#list(REMOVE_ITEM MyCppSources "./unitTestGridVisitNeighborhood.cpp")

find_package(OpenCV REQUIRED)

include_directories( ${OpenCV_INCLUDE_DIRS} )

SET(GCC_COVERAGE_LINK_FLAGS    "-o3 -s -lz -lX11 -lpthread")
SET(CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}")
set( CMAKE_VERBOSE_MAKEFILE on )

add_executable(biosim ${MyCppSources} ${MyCppheaders})
target_link_libraries( biosim PUBLIC ${OpenCV_LIBS} )


install(TARGETS biosim DESTINATION bin)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)


