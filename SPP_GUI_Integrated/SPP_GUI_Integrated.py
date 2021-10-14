# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/eduardo/Desktop/SPP_deep_learning/SPP_GUI_Integrated/SPP_GUI_Integrated.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout

from Batch_Generator import WorkerThread_Batch_Gen
from SP_Predictor import WorkerThread_SP_Predictor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 513)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget_Predict_And_BatchGene = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_Predict_And_BatchGene.setGeometry(QtCore.QRect(10, 10, 601, 451))
        self.tabWidget_Predict_And_BatchGene.setObjectName("tabWidget_Predict_And_BatchGene")

        self.tab_Prection = QtWidgets.QWidget()
        self.tab_Prection.setObjectName("tab_Prection")

        self.CompaniesComboBox_SP = QtWidgets.QComboBox(self.tab_Prection)
        self.CompaniesComboBox_SP.setGeometry(QtCore.QRect(40, 60, 151, 25))
        self.CompaniesComboBox_SP.setObjectName("CompaniesComboBox_SP")
        self.CompaniesComboBox_SP.addItems(['none','TWTR']) #Add more items

        self.LBCompaniesComboBox_SP = QtWidgets.QLabel(self.tab_Prection)
        self.LBCompaniesComboBox_SP.setGeometry(QtCore.QRect(40, 40, 141, 17))
        self.LBCompaniesComboBox_SP.setObjectName("LBCompaniesComboBox_SP")

        self.PBtn_SelectBatch_SP = QtWidgets.QPushButton(self.tab_Prection)
        self.PBtn_SelectBatch_SP.setGeometry(QtCore.QRect(470, 60, 101, 25))
        self.PBtn_SelectBatch_SP.setObjectName("PBtn_SelectBatch_SP")

        self.LEdit_SelectBatch_SP = QtWidgets.QLineEdit(self.tab_Prection)
        self.LEdit_SelectBatch_SP.setGeometry(QtCore.QRect(250, 60, 211, 25))
        self.LEdit_SelectBatch_SP.setObjectName("LEdit_SelectBatch_SP")

        self.PbtnStart_SP = QtWidgets.QPushButton(self.tab_Prection)
        self.PbtnStart_SP.setGeometry(QtCore.QRect(428, 145, 111, 31))
        self.PbtnStart_SP.setObjectName("PbtnStart_SP")

        self.PbtnCleanall_SP = QtWidgets.QPushButton(self.tab_Prection)
        self.PbtnCleanall_SP.setGeometry(QtCore.QRect(270, 145, 111, 31))
        self.PbtnCleanall_SP.setObjectName("PbtnCleanall_SP")

        self.Ledit_NDaysPredict = QtWidgets.QLineEdit(self.tab_Prection)
        self.Ledit_NDaysPredict.setGeometry(QtCore.QRect(40, 150, 113, 25))
        self.Ledit_NDaysPredict.setObjectName("Ledit_NDaysPredict")

        self.progressBar = QtWidgets.QProgressBar(self.tab_Prection)
        self.progressBar.setGeometry(QtCore.QRect(50, 330, 501, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.LB_StateProcessBar_SP = QtWidgets.QLabel(self.tab_Prection)
        self.LB_StateProcessBar_SP.setGeometry(QtCore.QRect(50, 310, 241, 17))
        self.LB_StateProcessBar_SP.setObjectName("LB_StateProcessBar_SP")

        self.Lb_NdayPredict = QtWidgets.QLabel(self.tab_Prection)
        self.Lb_NdayPredict.setGeometry(QtCore.QRect(40, 130, 121, 17))
        self.Lb_NdayPredict.setObjectName("Lb_NdayPredict")

        self.Lb_BatchPath_SP = QtWidgets.QLabel(self.tab_Prection)
        self.Lb_BatchPath_SP.setGeometry(QtCore.QRect(250, 40, 131, 17))
        self.Lb_BatchPath_SP.setObjectName("Lb_BatchPath_SP")

        self.tabWidget_Predict_And_BatchGene.addTab(self.tab_Prection, "")

        self.Tab_BatchGene = QtWidgets.QWidget()
        self.Tab_BatchGene.setObjectName("Tab_BatchGene")

        self.DateEdit_From = QtWidgets.QDateEdit(self.Tab_BatchGene)
        self.DateEdit_From.setGeometry(QtCore.QRect(280, 70, 110, 26))
        self.DateEdit_From.setObjectName("DateEdit_From")

        self.DateEdit_To = QtWidgets.QDateEdit(self.Tab_BatchGene)
        self.DateEdit_To.setGeometry(QtCore.QRect(440, 70, 110, 26))
        self.DateEdit_To.setObjectName("DateEdit_To")

        self.progressBar_BatchGene = QtWidgets.QProgressBar(self.Tab_BatchGene)
        self.progressBar_BatchGene.setGeometry(QtCore.QRect(50, 330, 501, 41))
        self.progressBar_BatchGene.setProperty("value", 0)
        self.progressBar_BatchGene.setObjectName("progressBar_BatchGene")

        self.LB_From = QtWidgets.QLabel(self.Tab_BatchGene)
        self.LB_From.setGeometry(QtCore.QRect(280, 50, 81, 17))
        self.LB_From.setObjectName("LB_From")

        self.LB_To = QtWidgets.QLabel(self.Tab_BatchGene)
        self.LB_To.setGeometry(QtCore.QRect(440, 50, 67, 17))
        self.LB_To.setObjectName("LB_To")

        self.LEdit_BackDays = QtWidgets.QLineEdit(self.Tab_BatchGene)
        self.LEdit_BackDays.setGeometry(QtCore.QRect(20, 205, 101, 25))
        self.LEdit_BackDays.setObjectName("LEdit_BackDays")

        self.Pbtn_Start = QtWidgets.QPushButton(self.Tab_BatchGene)
        self.Pbtn_Start.setGeometry(QtCore.QRect(320, 260, 111, 25))
        self.Pbtn_Start.setObjectName("Pbtn_Start")

        self.Pbtn_CleanAll = QtWidgets.QPushButton(self.Tab_BatchGene)
        self.Pbtn_CleanAll.setGeometry(QtCore.QRect(120, 260, 111, 25))
        self.Pbtn_CleanAll.setObjectName("Pbtn_CleanAll")

        self.PBtn_SaveIn = QtWidgets.QPushButton(self.Tab_BatchGene)
        self.PBtn_SaveIn.setGeometry(QtCore.QRect(470, 130, 89, 25))
        self.PBtn_SaveIn.setObjectName("PBtn_SaveIn")

        self.LB_BackDays = QtWidgets.QLabel(self.Tab_BatchGene)
        self.LB_BackDays.setGeometry(QtCore.QRect(20, 180, 191, 17))
        self.LB_BackDays.setObjectName("LB_BackDays")

        self.LB_StateProcessBar = QtWidgets.QLabel(self.Tab_BatchGene)
        self.LB_StateProcessBar.setGeometry(QtCore.QRect(50, 310, 241, 17))
        self.LB_StateProcessBar.setObjectName("LB_StateProcessBar")

        self.LEdi_PathToSaveBatch = QtWidgets.QLineEdit(self.Tab_BatchGene)
        self.LEdi_PathToSaveBatch.setGeometry(QtCore.QRect(240, 130, 201, 25))
        self.LEdi_PathToSaveBatch.setObjectName("LEdi_PathToSaveBatch")
        self.LEdi_PathToSaveBatch.setText('/home/eduardo/Desktop/SPP_deep_learning/BatchDataGenerator_Qt_file/All_Batches_TWTR/')

        self.Lb_PathToSaveBatch = QtWidgets.QLabel(self.Tab_BatchGene)
        self.Lb_PathToSaveBatch.setGeometry(QtCore.QRect(240, 110, 191, 17))
        self.Lb_PathToSaveBatch.setObjectName("Lb_PathToSaveBatch")

        self.Lb_CompaniesComboBox = QtWidgets.QLabel(self.Tab_BatchGene)
        self.Lb_CompaniesComboBox.setGeometry(QtCore.QRect(20, 50, 91, 17))
        self.Lb_CompaniesComboBox.setObjectName("Lb_CompaniesComboBox")
        

        self.CompaniesComboBox_BG = QtWidgets.QComboBox(self.Tab_BatchGene)
        self.CompaniesComboBox_BG.setGeometry(QtCore.QRect(20, 70, 161, 25))
        self.CompaniesComboBox_BG.setInputMethodHints(QtCore.Qt.ImhNone)
        self.CompaniesComboBox_BG.setEditable(False)
        self.CompaniesComboBox_BG.setObjectName("CompaniesComboBox_BG")
        self.CompaniesComboBox_BG.addItems(['none','TWTR']) #Add more items

        self.LB_BackDaysKindBatchGen = QtWidgets.QLabel(self.Tab_BatchGene)
        self.LB_BackDaysKindBatchGen.setGeometry(QtCore.QRect(20, 110, 191, 17))
        self.LB_BackDaysKindBatchGen.setObjectName("LB_BackDaysKindBatchGen")

        self.KindBatchGenComboBox_BG = QtWidgets.QComboBox(self.Tab_BatchGene)
        self.KindBatchGenComboBox_BG.setGeometry(QtCore.QRect(20, 135, 161, 25))
        self.KindBatchGenComboBox_BG.setInputMethodHints(QtCore.Qt.ImhNone)
        self.KindBatchGenComboBox_BG.setEditable(False)
        self.KindBatchGenComboBox_BG.setObjectName("KindBatchGenComboBox_BG")
        self.KindBatchGenComboBox_BG.addItems(['none','Training','Predict']) #Add more items

        self.tabWidget_Predict_And_BatchGene.addTab(self.Tab_BatchGene, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)


        self.LB_Last_Data_Batch_Path = QtWidgets.QLabel(self.Tab_BatchGene)
        self.LB_Last_Data_Batch_Path.setGeometry(QtCore.QRect(240, 178, 191, 17))
        self.LB_Last_Data_Batch_Path.setObjectName("LB_Last_Data_Batch_Path")

        self.LEdi_Last_Data_Batch_Path = QtWidgets.QLineEdit(self.Tab_BatchGene)
        self.LEdi_Last_Data_Batch_Path.setGeometry(QtCore.QRect(240, 203, 280, 25))
        self.LEdi_Last_Data_Batch_Path.setObjectName("LEdi_Last_Data_Batch_Path")
        self.LEdi_Last_Data_Batch_Path.setText('')


        self.retranslateUi(MainWindow)
        self.tabWidget_Predict_And_BatchGene.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ------ Error messages in Batch Generator ------ 
        self.msg_Batch_Gen = QMessageBox()
        self.msg_Batch_Gen.setIcon(QMessageBox.Critical)
        self.msg_Batch_Gen.setText("Back Days to consider")
        self.msg_Batch_Gen.setInformativeText('Must write a int number bigger than 0')
        self.msg_Batch_Gen.setWindowTitle("Error")

        self.msg_DirectoryPathSaveBatch = QMessageBox()
        self.msg_DirectoryPathSaveBatch.setIcon(QMessageBox.Critical)
        self.msg_DirectoryPathSaveBatch.setText("folder directoy to save ")
        self.msg_DirectoryPathSaveBatch.setInformativeText('Most selecte a directory to save the batches')
        self.msg_DirectoryPathSaveBatch.setWindowTitle("Error")

        #---------------    Bottons call functions Batch Generator ----------------------

        self.Pbtn_Start.clicked.connect(self.Start_Batch_Gen)
        self.Pbtn_CleanAll.clicked.connect(self.Clean_all_Betch_Gen)
        self.PBtn_SaveIn.clicked.connect(self.getDirectory)

        #-------------- Thread instance and mited signals Batch Generator ----------------------
        self.Worker_Batch_Gen=WorkerThread_Batch_Gen()
        self.Worker_Batch_Gen.Update_Progress.connect(self.Event_UpdateProgress_Batch_Gen)
        self.Worker_Batch_Gen.Update_Progress_Description.connect(self.Event_UpdateProgress_Description_Batch_Gen)
        self.Worker_Batch_Gen.LastBatchPathPredict.connect(self.Event_LastBatchPathPredict)

        # ------ Error messages in Batch Stock predictor  ------
        self.msg_SP_NdayPredict= QMessageBox()
        self.msg_SP_NdayPredict.setIcon(QMessageBox.Critical)
        self.msg_SP_NdayPredict.setText("N futures Days to predict")
        self.msg_SP_NdayPredict.setInformativeText('Must write a int number bigger than 0')
        self.msg_SP_NdayPredict.setWindowTitle("Error")

        self.msg_SP_Missing_Data= QMessageBox()
        self.msg_SP_Missing_Data.setIcon(QMessageBox.Critical)
        self.msg_SP_Missing_Data.setText("N futures Days to predict")
        self.msg_SP_Missing_Data.setInformativeText('Must write a int number bigger than 0')
        self.msg_SP_Missing_Data.setWindowTitle("Error")

        #---------------    Bottons call functions Stock predictor  ----------------------
        self.PbtnStart_SP.clicked.connect(self.Start_SP)
        self.PbtnCleanall_SP.clicked.connect(self.Clean_all_SP)
        self.PBtn_SelectBatch_SP.clicked.connect(self.getPathBacth)

        #-------------- Thread instance and mited signals Stock predictor  ----------------------
        self.Worker_SP=WorkerThread_SP_Predictor()
        self.Worker_SP.Update_Progress.connect(self.Event_UpdateProgress_SP)
        self.Worker_SP.Update_Progress_Description.connect(self.Event_UpdateProgress_Description_SP)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPP deep learning GUI"))
        self.LBCompaniesComboBox_SP.setText(_translate("MainWindow", "Company  model"))
        self.PBtn_SelectBatch_SP.setText(_translate("MainWindow", "Select Batch"))
        self.PbtnStart_SP.setText(_translate("MainWindow", "Start process"))
        self.PbtnCleanall_SP.setText(_translate("MainWindow", "Clean all"))
        self.LB_StateProcessBar_SP.setText(_translate("MainWindow", "Ready "))
        self.Lb_NdayPredict.setText(_translate("MainWindow", "N days to predict"))
        self.Lb_BatchPath_SP.setText(_translate("MainWindow", "Batch Path"))
        self.tabWidget_Predict_And_BatchGene.setTabText(self.tabWidget_Predict_And_BatchGene.indexOf(self.tab_Prection), _translate("MainWindow", "Stock Prections"))
        self.LB_From.setText(_translate("MainWindow", "Date From"))
        self.LB_To.setText(_translate("MainWindow", "Date To"))
        self.Pbtn_Start.setText(_translate("MainWindow", "Start"))
        self.Pbtn_CleanAll.setText(_translate("MainWindow", "Clean all"))
        self.PBtn_SaveIn.setText(_translate("MainWindow", "Save in"))
        self.LB_BackDays.setText(_translate("MainWindow", "Back days to consider"))
        self.LB_BackDaysKindBatchGen.setText(_translate("MainWindow", "Kind of batch"))
        self.LB_StateProcessBar.setText(_translate("MainWindow", "Ready"))
        self.Lb_PathToSaveBatch.setText(_translate("MainWindow", "It\'s going to be save in..."))
        self.Lb_CompaniesComboBox.setText(_translate("MainWindow", "Company"))
        self.LB_Last_Data_Batch_Path.setText(_translate("MainWindow", "Last_Data_Batch_Path"))
        self.tabWidget_Predict_And_BatchGene.setTabText(self.tabWidget_Predict_And_BatchGene.indexOf(self.Tab_BatchGene), _translate("MainWindow", "Batch Generator"))

    #-------------  Funtions Batch_Generator ------------------------
    
    def Start_Batch_Gen(self):
        var_DateTo=self.getting_DateTo()

        var_DateFrom=self.getting_DateFrom()
        
        var_N_backDays= self.getting_BackDaysTo_Consider()

        SelectedCompany=self.getting_Company_Batch_Gene()


        KindBatch=self.getting_Kind_Batch()

        print("---------------------")
        print(SelectedCompany)

        DirectoryPath = self.getting_DirectoryPathSaveBatch()

        if  var_N_backDays>0:
            self.Worker_Batch_Gen.GettingParametersForBatches(var_DateFrom,var_DateTo,var_N_backDays,SelectedCompany, DirectoryPath,KindBatch)
            self.Worker_Batch_Gen.start()
        else:
            self.msg_Batch_Gen.exec_()
            #QMessageBox.about(self, "Title", "Message")
            #QMessageBox.information()

    def getting_DateFrom(self):
        #Get Dates and transforme them into a "yyyy-mm-dd"
        temp_var = self.DateEdit_From.date()
        var_DateFrom = str(temp_var.toPyDate())
        return var_DateFrom
    
    def getting_DateTo(self):
        temp_var = self.DateEdit_To.date()
        var_DateTo =str(temp_var.toPyDate())
        return var_DateTo

    def getting_Company_Batch_Gene(self):
        return str(self.CompaniesComboBox_BG.currentText())

    def getting_Kind_Batch(self):
        return str (self.KindBatchGenComboBox_BG.currentText())

    def getting_DirectoryPathSaveBatch(self):
        try:
            var_directoryPath=self.LEdi_PathToSaveBatch.text()
        except:
            self.msg_DirectoryPathSaveBatch.exec_()
        return  var_directoryPath

    def getting_BackDaysTo_Consider(self):
        try:
            var_N_backDays=int(self.LEdit_BackDays.text())
        except:
            self.msg_Batch_Gen.exec_()
        
        return var_N_backDays
                
    def Event_UpdateProgress_Batch_Gen(self,val):
        self.progressBar_BatchGene.setValue(val)
    
    def Event_UpdateProgress_Description_Batch_Gen(self,val):
        self.LB_StateProcessBar.setText(val)

    def Event_LastBatchPathPredict(self,val):
        self.LEdi_Last_Data_Batch_Path.setText(val)

    def Clean_all_Betch_Gen(self):
        self.LEdit_BackDays.setText("")
        self.progressBar_BatchGene.setValue(0)
        self.LB_StateProcessBar.setText('Ready')
    
    def getDirectory(self):
        pass
    #-------------  Funtions SP_Predictor ------------------------

    def Start_SP(self):
        Company =self.getting_Company_SP()
        PathNumpyPredictionBatch =self.gettingPathPredictionBatch()
        N_Days_to_predict =self.N_Days_to_predict()

        if Company !='none' and PathNumpyPredictionBatch !='' and  N_Days_to_predict>0:
            self.Worker_SP.GettingParametersToPredictions(Company,PathNumpyPredictionBatch,N_Days_to_predict)
            self.Worker_SP.start()
        else:
            self.msg_SP_Missing_Data.exec_()


    def getting_Company_SP(self):
        return str(self.CompaniesComboBox_SP.currentText())
    
    def gettingPathPredictionBatch(self):
        return str(self.LEdit_SelectBatch_SP.text())

    def N_Days_to_predict(self): 
        try:
            var_N_backDays=int(self.Ledit_NDaysPredict.text())
        except:
            self.msg_SP_NdayPredict.exec_()
        
        return var_N_backDays
    

    def Clean_all_SP(self):
        self.Lb_NdayPredict.setText("")
        self.progressBar.setValue(0)

    def getPathBacth(self):
        pass

    def Event_UpdateProgress_SP(self,val):
        self.progressBar.setValue(val)

    def Event_UpdateProgress_Description_SP(self,val):
        self.LB_StateProcessBar_SP.setText(val)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
