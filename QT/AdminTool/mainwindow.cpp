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

   /*
   Setup the post data somehow
   I want to transmit:
   param1=string,
   param2=string
   */

    // Call the webservice
    QNetworkAccessManager *networkManager = new QNetworkAccessManager(this);
    connect(networkManager, SIGNAL(finished(QNetworkReply*)), this, SLOT(serviceRequestFinished(QNetworkReply*)));
    networkManager->post(QNetworkRequest(serviceUrl),ContentType { MixedType, RelatedType, FormDataType, AlternativeType });

    /*
       QNetworkRequest request(QUrl("http://localhost/laptop/trylogin.php"));

       QByteArray data;
       QUrl params;

       QString userString("root");
       QString passString("admin");

       params.addQueryItem("user", userString );
       params.addQueryItem("pass", passString );
       data.append(params.toString());
       data.remove(0,1);

       QNetworkReply *reply = nwam->post(request,data);

       */

    //Connection test
    if(db.open()) {
        ui->label_2->setText("Connection succeded");
    }
    else {
        ui->label_2->setText("Connection failed");
    }

}
