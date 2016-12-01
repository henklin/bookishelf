#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    manager = new QNetworkAccessManager(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

//Denna startar en connection

void MainWindow::getbooks()
{
    manager = new QNetworkAccessManager(this);

    connect(manager, SIGNAL(finished(QNetworkReply*)),
            this, SLOT(replyFinished(QNetworkReply*)));

    manager->get(QNetworkRequest(QUrl("http://localhost:8080/api/checkout?userid=1&bookid=1")));

}

void MainWindow::replyFinished (QNetworkReply *reply)
{
    qDebug() << reply->readAll();
}


void MainWindow::on_pushButton_4_clicked()
{

    QString title, id, qty, price;

    id = ui->lineEdit_3->text();
    title = ui->lineEdit_2->text();
    qty = ui->lineEdit_4->text();
    price = ui->lineEdit_5->text();

    //Koppla mig till servern

    connect(manager, SIGNAL(finished(QNetworkReply*)),
            this, SLOT(replyFinished(QNetworkReply*)));


    QByteArray data;
    QUrlQuery params;
    params.addQueryItem("id",id );
    params.addQueryItem("title", title);
    params.addQueryItem("qty", qty);
    params.addQueryItem("price",price);
    data.append(params.toString());

    QUrl resource("http://localhost:8080/api/book");
    QNetworkRequest request(resource);
    //Force Content-Type header
    request.setHeader(QNetworkRequest::ContentTypeHeader, "application/x-www-form-urlencoded");

    manager->post(request, data);



}

