#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QHttpMultiPart>
#include <QUrlQuery>
#include <QNetworkReply>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    void getbooks();

private slots:
    void on_pushButton_4_clicked();
    void replyFinished (QNetworkReply* reply);


    void on_pushButton_clicked();

private:
    QNetworkAccessManager *manager;
    Ui::MainWindow *ui;


private:

};

#endif // MAINWINDOW_H
