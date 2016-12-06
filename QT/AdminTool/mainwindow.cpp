#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QStringListModel>


#include <iostream>
using namespace std;

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->tableWidget->setColumnCount(4);

    auto width = ui->tableWidget->width();
    for (int i = 0; i < 4; i++)
        ui->tableWidget->setColumnWidth(i,width/4.0);

    QStringList labels;
      labels << "Book ID" << "Book Title" << "Quantity" << "Price per Unit";
    ui->tableWidget->setHorizontalHeaderLabels(labels);
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
    QString id;
    QByteArray getRequest;
    QStringList list;

    id = ui->lineEdit_searchID->text();

    if (id == "") {

        QMessageBox::information(NULL, "Warning", "You need to enter an book ID");

    } else {


        manager = new QNetworkAccessManager(this);

        QString url = "http://localhost:8080/api/book?bookid=" + id;
        QNetworkRequest request= QNetworkRequest(QUrl(url));
        request.setHeader(QNetworkRequest::ContentTypeHeader, "application/x-www-form-urlencoded");

        QNetworkReply* reply = manager ->get(request);

        //Väntar en sekund för att hinna läsa data
        QTime dieTime= QTime::currentTime().addMSecs(100);
            while (QTime::currentTime() < dieTime)
                QCoreApplication::processEvents(QEventLoop::AllEvents, 100);

         connect(manager, SIGNAL(finished(QNetworkReply*)),
                    this, SLOT(replyFinished(QNetworkReply*)));


        //Omvandlar from QByteArray till QString
        getRequest = reply->readAll();
        QString getRequestStr(QString::fromLatin1(getRequest));
        getRequestStr.replace("(","");
        getRequestStr.replace(")","");
        getRequestStr.replace("'","");
        getRequestStr.replace(" ","");

        //Dela upp QString
        list = getRequestStr.split(",");
        QString id = list.at(0);
        QString title = list.at(1);
        QString qty = list.at(2);
        QString price = list.at(3);

        ui->tableWidget->setRowCount(1);
        ui->tableWidget->setItem(0, 0, new QTableWidgetItem(id));
        ui->tableWidget->setItem(0, 1, new QTableWidgetItem(title));
        ui->tableWidget->setItem(0, 2, new QTableWidgetItem(qty));
        ui->tableWidget->setItem(0, 3, new QTableWidgetItem(price));



    }

    ui->lineEdit_searchID->clear();
}


void MainWindow::on_pushButton_5_clicked()
{

    QByteArray getRequest;
    QStringList list;
    manager = new QNetworkAccessManager(this);

    QString url = "http://localhost:8080/api/allBooks";
    QNetworkRequest request= QNetworkRequest(QUrl(url));
    request.setHeader(QNetworkRequest::ContentTypeHeader, "application/x-www-form-urlencoded");

    QNetworkReply* reply = manager ->get(request);

    //Väntar en sekund för att hinna läsa data
    QTime dieTime= QTime::currentTime().addSecs(1);
        while (QTime::currentTime() < dieTime)
            QCoreApplication::processEvents(QEventLoop::AllEvents, 100);

     connect(manager, SIGNAL(finished(QNetworkReply*)),
                this, SLOT(replyFinished(QNetworkReply*)));

     //Omvandlar from QByteArray till QString
     getRequest = reply->readAll();
     QString getRequestStr(QString::fromLatin1(getRequest));
     getRequestStr.replace("(","");
     getRequestStr.replace(")","");
     getRequestStr.replace("'","");
     getRequestStr.replace(" ","");

     //Dela in allt i en lista
     list = getRequestStr.split(",");
     qDebug() << getRequest;

     //Hur många finns det
     int nrOfBooks = list.size()*0.25;
     int place = 0;
     int place1 = 1;
     int place2 = 2;
     int place3 = 3;

     for (int i = 0; i < nrOfBooks; i++) {

         QString id = list.at(place);
         QString title = list.at(place1);
         QString qty = list.at(place2);
         QString price = list.at(place3);

         place += 4;
         place1 += 4;
         place2 += 4;
         place3 += 4;

         ui->tableWidget->setRowCount(nrOfBooks);
         ui->tableWidget->setItem(i, 0, new QTableWidgetItem(id));
         ui->tableWidget->setItem(i, 1, new QTableWidgetItem(title));
         ui->tableWidget->setItem(i, 2, new QTableWidgetItem(qty));
         ui->tableWidget->setItem(i, 3, new QTableWidgetItem(price));

     }
}






