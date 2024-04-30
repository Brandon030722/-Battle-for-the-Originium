#include "Widget.h"
#include "ui_widget.h"
#include <QPixmap>
#include <QPalette>
#include <QBrush>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    QPixmap backgroundPixmap("D:\\qt_p\\1024");
    backgroundPixmap = backgroundPixmap.scaled(this->size(), Qt::IgnoreAspectRatio, Qt::SmoothTransformation);

    QBrush brush(backgroundPixmap);


    QPalette palette;
    palette.setBrush(QPalette::Window, brush);
    this->setPalette(palette);



}

Widget::~Widget()
{
    delete ui;
}


