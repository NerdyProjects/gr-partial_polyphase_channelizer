INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PARTIAL_POLYPHASE_CHANNELIZER partial_polyphase_channelizer)

FIND_PATH(
    PARTIAL_POLYPHASE_CHANNELIZER_INCLUDE_DIRS
    NAMES partial_polyphase_channelizer/api.h
    HINTS $ENV{PARTIAL_POLYPHASE_CHANNELIZER_DIR}/include
        ${PC_PARTIAL_POLYPHASE_CHANNELIZER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PARTIAL_POLYPHASE_CHANNELIZER_LIBRARIES
    NAMES gnuradio-partial_polyphase_channelizer
    HINTS $ENV{PARTIAL_POLYPHASE_CHANNELIZER_DIR}/lib
        ${PC_PARTIAL_POLYPHASE_CHANNELIZER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/partial_polyphase_channelizerTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PARTIAL_POLYPHASE_CHANNELIZER DEFAULT_MSG PARTIAL_POLYPHASE_CHANNELIZER_LIBRARIES PARTIAL_POLYPHASE_CHANNELIZER_INCLUDE_DIRS)
MARK_AS_ADVANCED(PARTIAL_POLYPHASE_CHANNELIZER_LIBRARIES PARTIAL_POLYPHASE_CHANNELIZER_INCLUDE_DIRS)
