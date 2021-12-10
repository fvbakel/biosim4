cmake_minimum_required(VERSION 3.0.0)
project(BioSim4 VERSION 0.1.0)

include(CTest)
enable_testing()

add_subdirectory(src)


install(FILES ./biosim4.ini DESTINATION bin)
install(FILES ./tools/* DESTINATION tools)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
