#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QHttpMultiPart>

#include <iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_tableWidget_activated(const QModelIndex &index)
{

}

void MainWindow::on_pushButton_clicked()
{

}

void MainWindow::on_pushButton_4_clicked()
{
    QString name, id, nrOfBooks, price;

    name = ui->lineEdit_2->text();
    id = ui->lineEdit_3->text();
    nrOfBooks = ui->label_4->text();
    price = ui->label_5->text();

    //Creates connection
    //QNetworkAccessManager *nwam = new QNetworkAccessManager;

    QUrl serviceUrl = QUrl("http://myserver/myservice.asmx");
    QByteArray postData;

    QHttpMultiPart *multiPart = new QHttpMultiPart(QHttpMultiPart::FormDataType);

    QHttpPart textPart;
    textPart.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"text\""));
    textPart.setBody(name);

    // Call the webservice
    QNetworkAccessManager *networkManager = new QNetworkAccessManager(this);
    connect(networkManager, SIGNAL(finished(QNetworkReply*)), this, SLOT(serviceRequestFinished(QNetworkReply*)));
    networkManager->post(QNetworkRequest(serviceUrl), *multiPart);

}
