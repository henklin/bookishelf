#include "mainwindow.h"
#include <QMessageBox>
#include <QApplication>
#include <QPluginLoader>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    return a.exec();
}
