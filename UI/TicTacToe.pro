TEMPLATE = app

QT += qml quick
CONFIG += c++11

SOURCES += main.cpp

RESOURCES += qml.qrc

QMAKE_CXXFLAGS +=

QMAKE_INCDIR += /usr/include/python2.7

QMAKE_LIBS += -lpython2.7

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
include(deployment.pri)

DISTFILES += \
    mytest.py \
    main.py \
    status.py

HEADERS += \
    MediaClass.h

