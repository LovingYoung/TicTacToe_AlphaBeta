#include <iostream>
#include <Python.h>
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQml>
#include "MediaClass.h"
using namespace std;

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    qmlRegisterType<MediaClass>("liuyang.Media",1,0,"MediaClass");

    QQmlApplicationEngine engine;

    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
