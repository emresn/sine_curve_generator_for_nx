
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
    
    expression2 = workPart.Expressions.CreateWithUnits("xt=25*(30*t)", unit1)
    
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
    
    expression3 = workPart.Expressions.CreateWithUnits("yt=0 +(10*sin(25*360*t))", unit1)
    
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
                
                
                