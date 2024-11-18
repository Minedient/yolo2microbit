# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextBrowser,
    QWidget)

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        if not MainDialog.objectName():
            MainDialog.setObjectName(u"MainDialog")
        MainDialog.resize(444, 331)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainDialog.sizePolicy().hasHeightForWidth())
        MainDialog.setSizePolicy(sizePolicy)
        MainDialog.setLocale(QLocale(QLocale.Cantonese, QLocale.HongKong))
        self.gridLayoutWidget = QWidget(MainDialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 441, 321))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lineEdit, 5, 1, 1, 2)

        self.labelSubTitle = QLabel(self.gridLayoutWidget)
        self.labelSubTitle.setObjectName(u"labelSubTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelSubTitle.sizePolicy().hasHeightForWidth())
        self.labelSubTitle.setSizePolicy(sizePolicy2)
        self.labelSubTitle.setFrameShape(QFrame.Shape.NoFrame)
        self.labelSubTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelSubTitle, 2, 0, 1, 5)

        self.relationComboBox = QComboBox(self.gridLayoutWidget)
        self.relationComboBox.addItem("")
        self.relationComboBox.addItem("")
        self.relationComboBox.addItem("")
        self.relationComboBox.addItem("")
        self.relationComboBox.addItem("")
        self.relationComboBox.addItem("")
        self.relationComboBox.setObjectName(u"relationComboBox")
        sizePolicy1.setHeightForWidth(self.relationComboBox.sizePolicy().hasHeightForWidth())
        self.relationComboBox.setSizePolicy(sizePolicy1)
        self.relationComboBox.setLocale(QLocale(QLocale.Cantonese, QLocale.HongKong))

        self.gridLayout.addWidget(self.relationComboBox, 3, 3, 1, 1)

        self.manualButton = QPushButton(self.gridLayoutWidget)
        self.manualButton.setObjectName(u"manualButton")

        self.gridLayout.addWidget(self.manualButton, 5, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 4, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.logicComboBox = QComboBox(self.gridLayoutWidget)
        self.logicComboBox.addItem("")
        self.logicComboBox.addItem("")
        self.logicComboBox.addItem("")
        self.logicComboBox.setObjectName(u"logicComboBox")

        self.gridLayout.addWidget(self.logicComboBox, 4, 0, 1, 1)

        self.numberSpinBox = QSpinBox(self.gridLayoutWidget)
        self.numberSpinBox.setObjectName(u"numberSpinBox")
        self.numberSpinBox.setMaximum(9)

        self.gridLayout.addWidget(self.numberSpinBox, 3, 4, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 5)

        self.typeComboBox_2 = QComboBox(self.gridLayoutWidget)
        self.typeComboBox_2.setObjectName(u"typeComboBox_2")
        self.typeComboBox_2.setLocale(QLocale(QLocale.Cantonese, QLocale.HongKong))

        self.gridLayout.addWidget(self.typeComboBox_2, 4, 1, 1, 1)

        self.typeComboBox = QComboBox(self.gridLayoutWidget)
        self.typeComboBox.setObjectName(u"typeComboBox")
        self.typeComboBox.setLocale(QLocale(QLocale.Cantonese, QLocale.HongKong))

        self.gridLayout.addWidget(self.typeComboBox, 3, 1, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 7, 0, 1, 5)

        self.numberSpinBox_2 = QSpinBox(self.gridLayoutWidget)
        self.numberSpinBox_2.setObjectName(u"numberSpinBox_2")
        self.numberSpinBox_2.setMaximum(9)

        self.gridLayout.addWidget(self.numberSpinBox_2, 4, 4, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.modelFormLayout = QFormLayout()
        self.modelFormLayout.setObjectName(u"modelFormLayout")
        self.loadModelButton = QPushButton(self.gridLayoutWidget)
        self.loadModelButton.setObjectName(u"loadModelButton")

        self.modelFormLayout.setWidget(0, QFormLayout.LabelRole, self.loadModelButton)

        self.startButton = QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName(u"startButton")

        self.modelFormLayout.setWidget(2, QFormLayout.LabelRole, self.startButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stopButton = QPushButton(self.gridLayoutWidget)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout.addWidget(self.stopButton)

        self.connectButton = QPushButton(self.gridLayoutWidget)
        self.connectButton.setObjectName(u"connectButton")

        self.horizontalLayout.addWidget(self.connectButton)


        self.modelFormLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout)

        self.modelLabel = QLabel(self.gridLayoutWidget)
        self.modelLabel.setObjectName(u"modelLabel")

        self.modelFormLayout.setWidget(0, QFormLayout.FieldRole, self.modelLabel)


        self.gridLayout.addLayout(self.modelFormLayout, 0, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)

        self.relationComboBox_2 = QComboBox(self.gridLayoutWidget)
        self.relationComboBox_2.addItem("")
        self.relationComboBox_2.addItem("")
        self.relationComboBox_2.addItem("")
        self.relationComboBox_2.addItem("")
        self.relationComboBox_2.addItem("")
        self.relationComboBox_2.addItem("")
        self.relationComboBox_2.setObjectName(u"relationComboBox_2")
        sizePolicy1.setHeightForWidth(self.relationComboBox_2.sizePolicy().hasHeightForWidth())
        self.relationComboBox_2.setSizePolicy(sizePolicy1)
        self.relationComboBox_2.setLocale(QLocale(QLocale.Cantonese, QLocale.HongKong))

        self.gridLayout.addWidget(self.relationComboBox_2, 4, 3, 1, 1)

        self.runtimeLogger = QTextBrowser(self.gridLayoutWidget)
        self.runtimeLogger.setObjectName(u"runtimeLogger")

        self.gridLayout.addWidget(self.runtimeLogger, 8, 0, 1, 5)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lineEdit_2, 6, 1, 1, 2)

        self.hasNegate = QCheckBox(self.gridLayoutWidget)
        self.hasNegate.setObjectName(u"hasNegate")

        self.gridLayout.addWidget(self.hasNegate, 6, 4, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_7, 6, 3, 1, 1)

        self.gridLayout.setColumnStretch(1, 10)

        self.retranslateUi(MainDialog)

        QMetaObject.connectSlotsByName(MainDialog)
    # setupUi

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QCoreApplication.translate("MainDialog", u"Object Detection Model To Micro:bit Linker", None))
#if QT_CONFIG(tooltip)
        MainDialog.setToolTip(QCoreApplication.translate("MainDialog", u"This program load a yolo-based model and send signal to micro:bit according to the user setup", None))
#endif // QT_CONFIG(tooltip)
        self.labelSubTitle.setText(QCoreApplication.translate("MainDialog", u"\u8f38\u51fa\u908f\u8f2f", None))
        self.relationComboBox.setItemText(0, QCoreApplication.translate("MainDialog", u"\u5927\u65bc", None))
        self.relationComboBox.setItemText(1, QCoreApplication.translate("MainDialog", u"\u5927\u65bc\u6216\u7b49\u65bc", None))
        self.relationComboBox.setItemText(2, QCoreApplication.translate("MainDialog", u"\u7b49\u65bc", None))
        self.relationComboBox.setItemText(3, QCoreApplication.translate("MainDialog", u"\u4e0d\u7b49\u65bc", None))
        self.relationComboBox.setItemText(4, QCoreApplication.translate("MainDialog", u"\u5c0f\u65bc", None))
        self.relationComboBox.setItemText(5, QCoreApplication.translate("MainDialog", u"\u5c0f\u65bc\u6216\u7b49\u65bc", None))

#if QT_CONFIG(tooltip)
        self.manualButton.setToolTip(QCoreApplication.translate("MainDialog", u"\u624b\u52d5\u50b3\u9001\u6307\u4ee4\u5230micro:bit\u4ee5\u4fbf\u9032\u884c\u6e2c\u8a66", None))
#endif // QT_CONFIG(tooltip)
        self.manualButton.setText(QCoreApplication.translate("MainDialog", u"\u624b\u52d5\u50b3\u9001", None))
        self.label_3.setText(QCoreApplication.translate("MainDialog", u"\u7684\u6578\u91cf", None))
        self.label_4.setText(QCoreApplication.translate("MainDialog", u"\u5247\u8f38\u51fa", None))
        self.logicComboBox.setItemText(0, QCoreApplication.translate("MainDialog", u"\u6c92\u6709\u7b2c\u4e8c\u689d\u4ef6", None))
        self.logicComboBox.setItemText(1, QCoreApplication.translate("MainDialog", u"\u6216", None))
        self.logicComboBox.setItemText(2, QCoreApplication.translate("MainDialog", u"\u548c", None))

        self.label.setText(QCoreApplication.translate("MainDialog", u"\u7576\u6a21\u578b\u8b58\u5225\u5230", None))
        self.loadModelButton.setText(QCoreApplication.translate("MainDialog", u"\u9078\u64c7\u6a21\u578b", None))
        self.startButton.setText(QCoreApplication.translate("MainDialog", u"\u958b\u59cb", None))
        self.stopButton.setText(QCoreApplication.translate("MainDialog", u"\u66ab\u505c", None))
        self.connectButton.setText(QCoreApplication.translate("MainDialog", u"\u9023\u63a5\u5230micro:bit", None))
        self.modelLabel.setText(QCoreApplication.translate("MainDialog", u"\u672a\u9078\u64c7\u6a21\u578b", None))
        self.label_2.setText(QCoreApplication.translate("MainDialog", u"\u7684\u6578\u91cf", None))
        self.relationComboBox_2.setItemText(0, QCoreApplication.translate("MainDialog", u"\u5927\u65bc", None))
        self.relationComboBox_2.setItemText(1, QCoreApplication.translate("MainDialog", u"\u5927\u65bc\u6216\u7b49\u65bc", None))
        self.relationComboBox_2.setItemText(2, QCoreApplication.translate("MainDialog", u"\u7b49\u65bc", None))
        self.relationComboBox_2.setItemText(3, QCoreApplication.translate("MainDialog", u"\u4e0d\u7b49\u65bc", None))
        self.relationComboBox_2.setItemText(4, QCoreApplication.translate("MainDialog", u"\u5c0f\u65bc", None))
        self.relationComboBox_2.setItemText(5, QCoreApplication.translate("MainDialog", u"\u5c0f\u65bc\u6216\u7b49\u65bc", None))

        self.label_6.setText(QCoreApplication.translate("MainDialog", u"\u5426\u5247\u8f38\u51fa", None))
        self.hasNegate.setText(QCoreApplication.translate("MainDialog", u"\u4f7f\u7528", None))
        self.label_5.setText(QCoreApplication.translate("MainDialog", u"\u5230Micro:bit", None))
        self.label_7.setText(QCoreApplication.translate("MainDialog", u"\u5230Micro:bit", None))
    # retranslateUi

