#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

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

//Denna startar en connection

void MainWindow::getbooks()
{

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
    manager = new QNetworkAccessManager(this);
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


void MainWindow::on_pushButton_clicked()
{
    QString id, str1;
    QStringList list;

    id = ui->lineEdit_searchID->text();

    if (id == "") {

        QMessageBox::information(NULL, "Warning", "You need to enter an book ID");

    } else {

        manager = new QNetworkAccessManager(this);

        connect(manager, SIGNAL(finished(QNetworkReply*)),
                this, SLOT(replyFinished(QNetworkReply*)));

        QString url = "http://localhost:8080/api/book?bookid=" + id;

        QNetworkReply* reply = manager->get(QNetworkRequest(QUrl(url)));
        reply->finished();
        int statusCode = reply->attribute(QNetworkRequest::HttpStatusCodeAttribute).toInt();
        qDebug() << reply->readAll();


    }

    ui->lineEdit_searchID->clear();
}





