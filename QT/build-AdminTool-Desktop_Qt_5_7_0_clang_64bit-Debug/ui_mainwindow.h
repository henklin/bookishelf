/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QTabWidget *tabWidget;
    QWidget *tab_2;
    QLabel *label_6;
    QPushButton *pushButton_4;
    QSplitter *splitter_3;
    QSplitter *splitter_2;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_5;
    QLabel *label_4;
    QWidget *widget;
    QVBoxLayout *verticalLayout_2;
    QLineEdit *lineEdit_2;
    QLineEdit *lineEdit_3;
    QLineEdit *lineEdit_4;
    QLineEdit *lineEdit_5;
    QWidget *tab;
    QSplitter *splitter;
    QLabel *label;
    QLineEdit *lineEdit;
    QPushButton *pushButton;
    QTableWidget *tableWidget;
    QSplitter *splitter_7;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(559, 444);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tab_2 = new QWidget();
        tab_2->setObjectName(QStringLiteral("tab_2"));
        label_6 = new QLabel(tab_2);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(20, 12, 207, 22));
        QFont font;
        font.setPointSize(18);
        label_6->setFont(font);
        pushButton_4 = new QPushButton(tab_2);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setGeometry(QRect(110, 250, 101, 32));
        splitter_3 = new QSplitter(tab_2);
        splitter_3->setObjectName(QStringLiteral("splitter_3"));
        splitter_3->setGeometry(QRect(20, 60, 191, 171));
        splitter_3->setOrientation(Qt::Horizontal);
        splitter_2 = new QSplitter(splitter_3);
        splitter_2->setObjectName(QStringLiteral("splitter_2"));
        splitter_2->setOrientation(Qt::Vertical);
        label_2 = new QLabel(splitter_2);
        label_2->setObjectName(QStringLiteral("label_2"));
        splitter_2->addWidget(label_2);
        label_3 = new QLabel(splitter_2);
        label_3->setObjectName(QStringLiteral("label_3"));
        splitter_2->addWidget(label_3);
        label_5 = new QLabel(splitter_2);
        label_5->setObjectName(QStringLiteral("label_5"));
        splitter_2->addWidget(label_5);
        label_4 = new QLabel(splitter_2);
        label_4->setObjectName(QStringLiteral("label_4"));
        splitter_2->addWidget(label_4);
        splitter_3->addWidget(splitter_2);
        widget = new QWidget(splitter_3);
        widget->setObjectName(QStringLiteral("widget"));
        verticalLayout_2 = new QVBoxLayout(widget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        lineEdit_2 = new QLineEdit(widget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));

        verticalLayout_2->addWidget(lineEdit_2);

        lineEdit_3 = new QLineEdit(widget);
        lineEdit_3->setObjectName(QStringLiteral("lineEdit_3"));

        verticalLayout_2->addWidget(lineEdit_3);

        lineEdit_4 = new QLineEdit(widget);
        lineEdit_4->setObjectName(QStringLiteral("lineEdit_4"));

        verticalLayout_2->addWidget(lineEdit_4);

        lineEdit_5 = new QLineEdit(widget);
        lineEdit_5->setObjectName(QStringLiteral("lineEdit_5"));

        verticalLayout_2->addWidget(lineEdit_5);

        splitter_3->addWidget(widget);
        tabWidget->addTab(tab_2, QString());
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        splitter = new QSplitter(tab);
        splitter->setObjectName(QStringLiteral("splitter"));
        splitter->setGeometry(QRect(250, 10, 251, 69));
        splitter->setOrientation(Qt::Vertical);
        label = new QLabel(splitter);
        label->setObjectName(QStringLiteral("label"));
        splitter->addWidget(label);
        lineEdit = new QLineEdit(splitter);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        splitter->addWidget(lineEdit);
        pushButton = new QPushButton(splitter);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        splitter->addWidget(pushButton);
        tableWidget = new QTableWidget(tab);
        tableWidget->setObjectName(QStringLiteral("tableWidget"));
        tableWidget->setGeometry(QRect(30, 100, 471, 161));
        splitter_7 = new QSplitter(tab);
        splitter_7->setObjectName(QStringLiteral("splitter_7"));
        splitter_7->setGeometry(QRect(390, 270, 111, 51));
        splitter_7->setOrientation(Qt::Vertical);
        pushButton_2 = new QPushButton(splitter_7);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        splitter_7->addWidget(pushButton_2);
        pushButton_3 = new QPushButton(splitter_7);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        splitter_7->addWidget(pushButton_3);
        tabWidget->addTab(tab, QString());

        verticalLayout->addWidget(tabWidget);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 559, 22));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        label_6->setText(QApplication::translate("MainWindow", "Add a book to the system", 0));
        pushButton_4->setText(QApplication::translate("MainWindow", "Add book", 0));
        label_2->setText(QApplication::translate("MainWindow", "Book Name", 0));
        label_3->setText(QApplication::translate("MainWindow", "ID", 0));
        label_5->setText(QApplication::translate("MainWindow", "number", 0));
        label_4->setText(QApplication::translate("MainWindow", "Price", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("MainWindow", "Add book", 0));
        label->setText(QApplication::translate("MainWindow", "Search for products", 0));
        pushButton->setText(QApplication::translate("MainWindow", "Search", 0));
        pushButton_2->setText(QApplication::translate("MainWindow", "Make Changes", 0));
        pushButton_3->setText(QApplication::translate("MainWindow", "Remove", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("MainWindow", "Handle Inventory", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
