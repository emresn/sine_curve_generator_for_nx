# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curve_tool.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 310)
        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(10, 10, 590, 290))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("curve.png"))
        self.pic.setObjectName("pic")
        self.wavelength = QtWidgets.QLineEdit(Form)
        self.wavelength.setGeometry(QtCore.QRect(160, 130, 61, 21))
        self.wavelength.setObjectName("wavelength")
        self.amplitude = QtWidgets.QLineEdit(Form)
        self.amplitude.setGeometry(QtCore.QRect(110, 111, 41, 20))
        self.amplitude.setObjectName("amplitude")
        self.total_length = QtWidgets.QLineEdit(Form)
        self.total_length.setEnabled(False)
        self.total_length.setGeometry(QtCore.QRect(280, 210, 71, 31))
        self.total_length.setInputMask("")
        self.total_length.setClearButtonEnabled(False)
        self.total_length.setObjectName("total_length")
        self.orijin = QtWidgets.QLineEdit(Form)
        self.orijin.setGeometry(QtCore.QRect(40, 180, 31, 20))
        self.orijin.setObjectName("orijin")
        self.orijin_text = QtWidgets.QLabel(Form)
        self.orijin_text.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.orijin_text.setObjectName("orijin_text")
        self.create = QtWidgets.QPushButton(Form)
        self.create.setGeometry(QtCore.QRect(500, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create.setFont(font)
        self.create.setObjectName("create")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 500, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 25, 500, 31))
        self.label_4.setObjectName("label_4")
        self.cycle = QtWidgets.QLineEdit(Form)
        self.cycle.setGeometry(QtCore.QRect(330, 80, 65, 22))
        self.cycle.setObjectName("cycle")
        self.cycle_check = QtWidgets.QCheckBox(Form)
        self.cycle_check.setGeometry(QtCore.QRect(350, 100, 21, 17))
        self.cycle_check.setText("")
        self.cycle_check.setChecked(True)
        self.cycle_check.setObjectName("cycle_check")
        self.total_length_check = QtWidgets.QCheckBox(Form)
        self.total_length_check.setGeometry(QtCore.QRect(265, 220, 21, 16))
        self.total_length_check.setText("")
        self.total_length_check.setObjectName("total_length_check")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(450, 30, 61, 31))
        self.clear.setObjectName("clear")
        self.create.clicked.connect(self.makro_create)
        self.clear.clicked.connect(self.clear_fields)
        self.cycle_check.clicked.connect(self.active_selection)
        self.total_length_check.clicked.connect(self.active_selection)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.wavelength.setText(_translate("Form", "lambda"))
        self.amplitude.setText(_translate("Form", "a"))
        self.total_length.setText(_translate("Form", "Length"))
        self.orijin.setText(_translate("Form", "0"))
        self.orijin_text.setText(_translate("Form", "Y0"))
        self.create.setText(_translate("Form", "Create"))
        self.label_3.setText(_translate("Form", "Sine Curve Generator for NX 11"))
        self.label_4.setText(_translate("Form", "https://github.com/emresn/sine_curve_generator_for_nx"))
        self.cycle.setText(_translate("Form", "Cycle"))
        self.clear.setText(_translate("Form", "Clear"))


    def makro_create(self):
        try:
            self.amplitude_int = int(self.amplitude.text())
            self.wavelength_int = int(self.wavelength.text())
            self.orijin_int = int(self.orijin.text())
            if self.cycle_check.isChecked():
                self.cycle_int = int(self.cycle.text())
                self.total_length_int = self.cycle_int * self.wavelength_int
            elif self.total_length_check.isChecked():
                self.total_length_int = int(self.total_length.text())
                self.cycle_int = self.total_length_int/self.wavelength_int


            with open("journal_file.py", "w") as file:
                file.write("""
# NX 11.0.0.33
# Journal created by SinCurve Journal Generator for NX 
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Tools->Expressions...
    # ----------------------------------------------
    theSession.Preferences.Modeling.UpdatePending = False
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Expressions Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Expression")
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateWithUnits("t=1", unit1)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
    
    objects1 = [NXOpen.NXObject.Null] * 1 
    objects1[0] = expression1
    theSession.UpdateManager.MakeUpToDate(objects1, markId5)
    
    expression1.EditComment("")
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Expression")
    
    expression2 = workPart.Expressions.CreateWithUnits("xt={}*({}*t)", unit1)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
    
    objects2 = [NXOpen.NXObject.Null] * 1 
    objects2[0] = expression2
    theSession.UpdateManager.MakeUpToDate(objects2, markId7)
    
    expression2.EditComment("")
    
    objects3 = [NXOpen.NXObject.Null] * 2 
    objects3[0] = expression1
    objects3[1] = expression2
    theSession.UpdateManager.MakeUpToDate(objects3, markId3)
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId8)
    
    theSession.DeleteUndoMark(markId8, "NX update")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.DeleteUndoMark(markId2, None)
    
    theSession.SetUndoMarkName(markId1, "Expressions")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId9, "Expressions Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Expressions
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Expression")
    
    expression3 = workPart.Expressions.CreateWithUnits("yt={} +({}*sin({}*360*t))", unit1)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
    
    objects4 = [NXOpen.NXObject.Null] * 1 
    objects4[0] = expression3
    theSession.UpdateManager.MakeUpToDate(objects4, markId13)
    
    expression3.EditComment("")
    
    objects5 = [NXOpen.NXObject.Null] * 1 
    objects5[0] = expression3
    theSession.UpdateManager.MakeUpToDate(objects5, markId11)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId14)
    
    theSession.DeleteUndoMark(markId14, "NX update")
    
    theSession.DeleteUndoMark(markId11, None)
    
    theSession.DeleteUndoMark(markId10, None)
    
    theSession.SetUndoMarkName(markId9, "Expressions")
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId15, "Expressions Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Expressions
    # ----------------------------------------------
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Expression")
    
    expression4 = workPart.Expressions.CreateWithUnits("zt=0", unit1)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Check Circular")
    
    objects6 = [NXOpen.NXObject.Null] * 1 
    objects6[0] = expression4
    theSession.UpdateManager.MakeUpToDate(objects6, markId19)
    
    expression4.EditComment("")
    
    objects7 = [NXOpen.NXObject.Null] * 1 
    objects7[0] = expression4
    theSession.UpdateManager.MakeUpToDate(objects7, markId17)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId20)
    
    theSession.DeleteUndoMark(markId20, "NX update")
    
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    theSession.SetUndoMarkName(markId15, "Expressions")
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theSession.SetUndoMarkName(markId21, "Expressions Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Expressions
    # ----------------------------------------------
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
    
    theSession.DeleteUndoMark(markId22, None)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId25)
    
    theSession.DeleteUndoMark(markId25, "NX update")
    
    theSession.DeleteUndoMark(markId24, None)
    
    theSession.DeleteUndoMark(markId23, None)
    
    theSession.SetUndoMarkName(markId21, "Expressions")
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Law Curve...
    # ----------------------------------------------
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    lawCurveBuilder1 = workPart.Features.CreateLawCurveBuilder(NXOpen.Features.LawCurve.Null)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    lawCurveBuilder1.XLaw.LawType = NXOpen.GeometricUtilities.LawBuilder.Type.ByEquation
    
    lawCurveBuilder1.XLaw.Value.RightHandSide = "0"
    
    lawCurveBuilder1.XLaw.StartValue.RightHandSide = "0"
    
    lawCurveBuilder1.XLaw.EndValue.RightHandSide = "0"
    
    lawCurveBuilder1.YLaw.LawType = NXOpen.GeometricUtilities.LawBuilder.Type.ByEquation
    
    lawCurveBuilder1.YLaw.Value.RightHandSide = "0"
    
    lawCurveBuilder1.YLaw.StartValue.RightHandSide = "0"
    
    lawCurveBuilder1.YLaw.EndValue.RightHandSide = "0"
    
    lawCurveBuilder1.ZLaw.LawType = NXOpen.GeometricUtilities.LawBuilder.Type.ByEquation
    
    lawCurveBuilder1.ZLaw.Value.RightHandSide = "0"
    
    lawCurveBuilder1.ZLaw.StartValue.RightHandSide = "0"
    
    lawCurveBuilder1.ZLaw.EndValue.RightHandSide = "0"
    
    theSession.SetUndoMarkName(markId26, "Law Curve Dialog")
    
    lawCurveBuilder1.XLaw.AlongSpineData.Spine.DistanceTolerance = 0.01
    
    lawCurveBuilder1.XLaw.AlongSpineData.Spine.ChainingTolerance = 0.0094999999999999998
    
    lawCurveBuilder1.XLaw.LawCurve.DistanceTolerance = 0.01
    
    lawCurveBuilder1.XLaw.LawCurve.ChainingTolerance = 0.0094999999999999998
    
    lawCurveBuilder1.YLaw.AlongSpineData.Spine.DistanceTolerance = 0.01
    
    lawCurveBuilder1.YLaw.AlongSpineData.Spine.ChainingTolerance = 0.0094999999999999998
    
    lawCurveBuilder1.YLaw.LawCurve.DistanceTolerance = 0.01
    
    lawCurveBuilder1.YLaw.LawCurve.ChainingTolerance = 0.0094999999999999998
    
    lawCurveBuilder1.ZLaw.AlongSpineData.Spine.DistanceTolerance = 0.01
    
    lawCurveBuilder1.ZLaw.AlongSpineData.Spine.ChainingTolerance = 0.0094999999999999998
    
    lawCurveBuilder1.ZLaw.LawCurve.DistanceTolerance = 0.01
    
    lawCurveBuilder1.ZLaw.LawCurve.ChainingTolerance = 0.0094999999999999998
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Law Curve")
    
    theSession.DeleteUndoMark(markId27, None)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Law Curve")
    
    nXObject1 = lawCurveBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId28, None)
    
    theSession.SetUndoMarkName(markId26, "Law Curve")
    
    lawCurveBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression5)
    
    workPart.Expressions.Delete(expression6)
    
    workPart.Expressions.Delete(expression7)
    
    # ----------------------------------------------
    #   Menu: Orient View->Top
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
    
    scaleAboutPoint1 = NXOpen.Point3d(-2.1283952823445289, 5.9748927805575391, 0.0)
    viewCenter1 = NXOpen.Point3d(2.1283952823445289, -5.9748927805575391, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(-2.6604941029306612, 7.4686159756969248, 0.0)
    viewCenter2 = NXOpen.Point3d(2.6604941029306612, -7.4686159756969248, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint2, viewCenter2)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()
                
                
                """.format(self.cycle_int,self.wavelength_int,self.orijin_int,self.amplitude_int,self.cycle_int))

                with open("log.txt", "w") as logfile:
                    logfile.write("""
Cycle: {}
Wavelength: {}
Origin: {}
Amplitude: {}
Total Length: {}
                """.format(self.cycle_int,self.wavelength_int,self.orijin_int,self.amplitude_int,self.total_length_int))
                message = QtWidgets.QMessageBox.about(self, "Successfull", "journal_file.py file have been generated.\nPlease run journal_file.py with NX Play Journal (Alt + F8) command.")
                message2 = QtWidgets.QMessageBox.about(self, "Informations", "log.txt file have been generated. \nCycle: {}\nwave Length: {}\nOrigin: {}\nAmplitude: {}\nTotal Length: {}".format(self.cycle_int,self.wavelength_int,self.orijin_int,self.amplitude_int,self.total_length_int))

        except:
            message = QtWidgets.QMessageBox.about(self, "Errror", "Please enter integer value in all fields.")

    def clear_fields(self):
        self.amplitude.setText("a")
        self.cycle.setText("Cycle")
        self.wavelength.setText("Lambda")
        self.orijin.setText("0")
        self.total_length.setText("Length")
    
    def active_selection(self):
        sender = self.sender()
        if self.total_length_check.isChecked() and sender == self.total_length_check:
            self.total_length.setEnabled(True)
            self.cycle.setEnabled(False)
            self.cycle_check.setChecked(False)
        elif self.cycle_check.isChecked()and sender == self.cycle_check:
            self.total_length.setEnabled(False)
            self.cycle.setEnabled(True)
            self.total_length_check.setChecked(False)



