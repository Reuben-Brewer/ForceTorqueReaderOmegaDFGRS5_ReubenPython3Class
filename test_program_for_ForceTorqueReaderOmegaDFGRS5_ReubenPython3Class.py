# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision D, 01/09/2026

Verified working on: Python 3.11/12/13 for Windows 10/11 64-bit and Raspberry Pi Bookworm.
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

##########################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
##########################################

##########################################
from CSVdataLogger_ReubenPython3Class import *
from ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class import *
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
##########################################

##########################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import math
import traceback
import keyboard
##########################################

##########################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
##########################################

##########################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
##########################################

##########################################################################################################
##########################################################################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global ForceTorqueReaderOmegaDFGRS5_Object
    global ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG
    global SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global CSVdataLogger_Object
    global CSVdataLogger_OPEN_FLAG
    global SHOW_IN_GUI_CSVdataLogger_FLAG

    if USE_GUI_FLAG == 1:

        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1 and SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG == 1:
                ForceTorqueReaderOmegaDFGRS5_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if CSVdataLogger_OPEN_FLAG == 1 and SHOW_IN_GUI_CSVdataLogger_FLAG == 1:
                CSVdataLogger_Object.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG
    global CSVdataLogger_MostRecentDict_IsSavingFlag

    print("ExitProgram_Callback event fired!")

    if CSVdataLogger_MostRecentDict_IsSavingFlag == 0:
        EXIT_PROGRAM_FLAG = 1
    else:
        print("ExitProgram_Callback, ERROR! Still saving data.")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    global ForceTorqueReaderOmegaDFGRS5_Object
    global ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG

    global CSVdataLogger_Object
    global CSVdataLogger_OPEN_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()

    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_ForceTorqueReaderOmegaDFGRS5
    global Tab_MyPrint
    global Tab_CSVdataLogger

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_ForceTorqueReaderOmegaDFGRS5 = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_ForceTorqueReaderOmegaDFGRS5, text='   FT Omega   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        #Tab_CSVdataLogger = ttk.Frame(TabControlObject)
        #TabControlObject.add(Tab_CSVdataLogger, text='   CSVdataLogger   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############

        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_ForceTorqueReaderOmegaDFGRS5 = root
        Tab_MyPrint = root
        Tab_CSVdataLogger = root
        #################################################

    ##########################################################################################################

    #################################################
    #################################################
    ButtonsFrame = Frame(Tab_MainControls)
    ButtonsFrame.grid(row = 0, column = 0, padx = 10, pady = 10, rowspan = 1, columnspan = 1)
    #################################################
    #################################################

    #################################################
    #################################################
    ResetPeak_Button = Button(ButtonsFrame, text="Reset Peak", state="normal", width=15, command=lambda: ResetPeak_Button_Response())
    ResetPeak_Button.grid(row=0, column=0, padx=10, pady=10, columnspan=1, rowspan=1)
    #################################################
    #################################################

    #################################################
    #################################################
    ResetTare_Button = Button(ButtonsFrame, text="Reset Tare", state="normal", width=20, command=lambda: ResetTare_Button_Response())
    ResetTare_Button.grid(row=0, column=1, padx=10, pady=10, columnspan=1, rowspan=1)
    #################################################
    #################################################

    #################################################
    #################################################
    if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG:
        ForceTorqueReaderOmegaDFGRS5_Object.CreateGUIobjects(TkinterParent=Tab_ForceTorqueReaderOmegaDFGRS5)
    #################################################
    #################################################

    #################################################
    #################################################
    if CSVdataLogger_OPEN_FLAG == 1:
        CSVdataLogger_Object.CreateGUIobjects(TkinterParent=Tab_MainControls)
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.CreateGUIobjects(TkinterParent=Tab_MyPrint)
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ResetPeak_Button_Response():
    global ResetPeak_EventNeedsToBeFiredFlag

    ResetPeak_EventNeedsToBeFiredFlag = 1

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ResetTare_Button_Response():
    global ResetTare_EventNeedsToBeFiredFlag

    ResetTare_EventNeedsToBeFiredFlag = 1

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_ForceTorqueReaderOmegaDFGRS5_FLAG
    USE_ForceTorqueReaderOmegaDFGRS5_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    USE_MyPlotterPureTkinterStandAloneProcess_FLAG = 1

    global USE_CSVdataLogger_FLAG
    USE_CSVdataLogger_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1

    global TorqueInsteadOfForceFlag
    TorqueInsteadOfForceFlag = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG
    SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1

    global SHOW_IN_GUI_CSVdataLogger_FLAG
    SHOW_IN_GUI_CSVdataLogger_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_ForceTorqueReaderOmegaDFGRS5
    global GUI_COLUMN_ForceTorqueReaderOmegaDFGRS5
    global GUI_PADX_ForceTorqueReaderOmegaDFGRS5
    global GUI_PADY_ForceTorqueReaderOmegaDFGRS5
    global GUI_ROWSPAN_ForceTorqueReaderOmegaDFGRS5
    global GUI_COLUMNSPAN_ForceTorqueReaderOmegaDFGRS5
    GUI_ROW_ForceTorqueReaderOmegaDFGRS5 = 0

    GUI_COLUMN_ForceTorqueReaderOmegaDFGRS5 = 0
    GUI_PADX_ForceTorqueReaderOmegaDFGRS5 = 1
    GUI_PADY_ForceTorqueReaderOmegaDFGRS5 = 1
    GUI_ROWSPAN_ForceTorqueReaderOmegaDFGRS5 = 1
    GUI_COLUMNSPAN_ForceTorqueReaderOmegaDFGRS5 = 1

    global GUI_ROW_CSVdataLogger
    global GUI_COLUMN_CSVdataLogger
    global GUI_PADX_CSVdataLogger
    global GUI_PADY_CSVdataLogger
    global GUI_ROWSPAN_CSVdataLogger
    global GUI_COLUMNSPAN_CSVdataLogger
    GUI_ROW_CSVdataLogger = 2

    GUI_COLUMN_CSVdataLogger = 0
    GUI_PADX_CSVdataLogger = 1
    GUI_PADY_CSVdataLogger = 1
    GUI_ROWSPAN_CSVdataLogger = 1
    GUI_COLUMNSPAN_CSVdataLogger = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 3

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_ForceTorqueReaderOmegaDFGRS5
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global ResetPeak_EventNeedsToBeFiredFlag
    ResetPeak_EventNeedsToBeFiredFlag = 0

    global ResetTare_EventNeedsToBeFiredFlag
    ResetTare_EventNeedsToBeFiredFlag = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global ForceTorqueReaderOmegaDFGRS5_Object

    global ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG
    ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG = 0

    global ForceTorqueReaderOmegaDFGRS5_DeviceToReadSerialNumber
    ForceTorqueReaderOmegaDFGRS5_DeviceToReadSerialNumber = "AV0K59E0A"

    global ForceTorqueReaderOmegaDFGRS5_MostRecentDict
    ForceTorqueReaderOmegaDFGRS5_MostRecentDict = dict()

    global ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_N
    ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_N = -11111.0

    global ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_N
    ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_N = -11111.0

    global ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_Nm
    ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_Nm = -11111.0

    global ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_Nm
    ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_Nm = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_Object

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global CSVdataLogger_Object

    global CSVdataLogger_OPEN_FLAG
    CSVdataLogger_OPEN_FLAG = -1

    global CSVdataLogger_MostRecentDict
    CSVdataLogger_MostRecentDict = dict()

    global CSVdataLogger_MostRecentDict_Time
    CSVdataLogger_MostRecentDict_Time = -11111.0

    global CSVdataLogger_MostRecentDict_IsSavingFlag
    CSVdataLogger_MostRecentDict_IsSavingFlag = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_Object

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = -1

    global LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = -11111.0
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global ForceTorqueReaderOmegaDFGRS5_GUIparametersDict
    ForceTorqueReaderOmegaDFGRS5_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG),
                                                            ("EnableInternal_MyPrint_Flag", 0),
                                                            ("NumberOfPrintLines", 10),
                                                            ("UseBorderAroundThisGuiObjectFlag", 0),
                                                            ("GUI_ROW", GUI_ROW_ForceTorqueReaderOmegaDFGRS5),
                                                            ("GUI_COLUMN", GUI_COLUMN_ForceTorqueReaderOmegaDFGRS5),
                                                            ("GUI_PADX", GUI_PADX_ForceTorqueReaderOmegaDFGRS5),
                                                            ("GUI_PADY", GUI_PADY_ForceTorqueReaderOmegaDFGRS5),
                                                            ("GUI_ROWSPAN", GUI_ROWSPAN_ForceTorqueReaderOmegaDFGRS5),
                                                            ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_ForceTorqueReaderOmegaDFGRS5)])

    global ForceTorqueReaderOmegaDFGRS5_SetupDict
    ForceTorqueReaderOmegaDFGRS5_SetupDict = dict([("GUIparametersDict", ForceTorqueReaderOmegaDFGRS5_GUIparametersDict),
                                                    ("DesiredSerialNumber_USBtoSerialConverter", ForceTorqueReaderOmegaDFGRS5_DeviceToReadSerialNumber),
                                                    ("NameToDisplay_UserSet", "ForceTorqueReaderOmegaDFGRS5: Sensor " + ForceTorqueReaderOmegaDFGRS5_DeviceToReadSerialNumber),
                                                    ("ReadingModeString", "RealTime_CUR"), #["RealTime_CUR",  "PeakTension_PT", "PeakCompression_PC",  "PeakClockwise_PCW", "PeakCounterClockwise_PCCW"]
                                                    ("SamplesPerSecond", 250), #[0, 2, 5, 10, 25, 50, 125, 250]
                                                    ("FilterExponent0to10ForNumberOfSamplesToBeAveraged", 2),
                                                    ("AutoShutoffTimeIntegerMinutes0to30", 10),
                                                    ("DedicatedRxThread_TimeToSleepEachLoop", 0.001),
                                                    ("DedicatedTxThread_TimeToSleepEachLoop", 0.010),
                                                    ("DedicatedTxThread_TxMessageToSend_Queue_MaxSize", 1),
                                                    ("MeasurementDerivative_ExponentialSmoothingFilterLambda", 0.95)])

    if USE_ForceTorqueReaderOmegaDFGRS5_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            ForceTorqueReaderOmegaDFGRS5_Object = ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class(ForceTorqueReaderOmegaDFGRS5_SetupDict)
            ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG = ForceTorqueReaderOmegaDFGRS5_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("ForceTorqueReaderOmegaDFGRS5_ReubenPython3ClassObject __init__ on SerialNumber" + ForceTorqueReaderOmegaDFGRS5_DeviceToReadSerialNumber + ", exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_ForceTorqueReaderOmegaDFGRS5_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG != 1:
                print("Failed to open ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global CSVdataLogger_Object_GUIparametersDict
    CSVdataLogger_Object_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_CSVdataLogger_FLAG),
                                                ("EnableInternal_MyPrint_Flag", 1),
                                                ("NumberOfPrintLines", 10),
                                                ("UseBorderAroundThisGuiObjectFlag", 0),
                                                ("GUI_ROW", GUI_ROW_CSVdataLogger),
                                                ("GUI_COLUMN", GUI_COLUMN_CSVdataLogger),
                                                ("GUI_PADX", GUI_PADX_CSVdataLogger),
                                                ("GUI_PADY", GUI_PADY_CSVdataLogger),
                                                ("GUI_ROWSPAN", GUI_ROWSPAN_CSVdataLogger),
                                                ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_CSVdataLogger)])

    CSVdataLogger_Object_SetupDict_VariableNamesForHeaderList = ["Time (S)",
                                                                 "Force (N)",
                                                                 "ForceDerivative (N/s)",
                                                                 "Torque (Nm)",
                                                                 "TorqueDerivative (Nm/s)"]
                                                                 
    print("CSVdataLogger_Object_SetupDict_VariableNamesForHeaderList: " + str(CSVdataLogger_Object_SetupDict_VariableNamesForHeaderList))

    global CSVdataLogger_Object_SetupDict
    CSVdataLogger_Object_SetupDict = dict([("GUIparametersDict", CSVdataLogger_Object_GUIparametersDict),
                                            ("NameToDisplay_UserSet", "CSVdataLogger"),
                                            ("CSVfile_DirectoryPath", "C:\\CSVfiles"), #os.getcwd() + "\\CSVfiles"
                                            ("FileNamePrefix", "CSV_file_"),
                                            ("VariableNamesForHeaderList", CSVdataLogger_Object_SetupDict_VariableNamesForHeaderList),
                                            ("MainThread_TimeToSleepEachLoop", 0.002),
                                            ("SaveOnStartupFlag", 0)])

    if USE_CSVdataLogger_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            CSVdataLogger_Object = CSVdataLogger_ReubenPython3Class(CSVdataLogger_Object_SetupDict)
            CSVdataLogger_OPEN_FLAG = CSVdataLogger_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("CSVdataLogger_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_CSVdataLogger_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if CSVdataLogger_OPEN_FLAG != 1:
                print("Failed to open CSVdataLogger_ReubenPython3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPrint_GUIparametersDict
    MyPrint_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

    global MyPrint_SetupDict
    MyPrint_SetupDict = dict([("NumberOfPrintLines", 10),
                            ("WidthOfPrintingLabel", 200),
                            ("PrintToConsoleFlag", 1),
                            ("LogFileNameFullPath", os.path.join(os.getcwd(), "TestLog.txt")),
                            ("GUIparametersDict", MyPrint_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPrint_Object = MyPrint_ReubenPython2and3Class(MyPrint_SetupDict)
            MyPrint_OPEN_FLAG = MyPrint_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPrint_OPEN_FLAG != 1:
                print("Failed to open MyPrint_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_NameList
    MyPlotterPureTkinterStandAloneProcess_NameList = ["Torque (Nm)", "TorqueDerivative (Nm/s)"]

    global MyPlotterPureTkinterStandAloneProcess_ColorList
    MyPlotterPureTkinterStandAloneProcess_ColorList = ["Green", "Red"]
    
    global MyPlotterPureTkinterStandAloneProcess_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("GraphCanvasWidth", 900),
                                                                    ("GraphCanvasHeight", 700),
                                                                    ("GraphCanvasWindowStartingX", 0),
                                                                    ("GraphCanvasWindowStartingY", 0),
                                                                    ("GraphCanvasWindowTitle", "My plotting example!"),
                                                                    ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 30)])


    global MyPlotterPureTkinterStandAloneProcess_SetupDict
    MyPlotterPureTkinterStandAloneProcess_SetupDict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_GUIparametersDict),
                                                            ("ParentPID", os.getpid()),
                                                            ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 5.0),
                                                            ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", MyPlotterPureTkinterStandAloneProcess_NameList),
                                                                                                        ("MarkerSizeList", [2]*2),
                                                                                                        ("LineWidthList", [2]*2),
                                                                                                        ("IncludeInXaxisAutoscaleCalculationList", [1, 0]),
                                                                                                        ("IncludeInYaxisAutoscaleCalculationList", [1, 0]),
                                                                                                        ("ColorList", MyPlotterPureTkinterStandAloneProcess_ColorList)])),
                                                            ("SmallTextSize", 7),
                                                            ("LargeTextSize", 12),
                                                            ("NumberOfDataPointToPlot", 100),
                                                            ("XaxisNumberOfTickMarks", 10),
                                                            ("YaxisNumberOfTickMarks", 10),
                                                            ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("XaxisAutoscaleFlag", 1),
                                                            ("YaxisAutoscaleFlag", 1),
                                                            ("X_min", 0.0),
                                                            ("X_max", 5.0),
                                                            ("Y_min", -5.0),
                                                            ("Y_max", 5.0),
                                                            ("XaxisDrawnAtBottomOfGraph", 0),
                                                            ("XaxisLabelString", "Time (sec)"),
                                                            ("YaxisLabelString", "Y-units (units)"),
                                                            ("ShowLegendFlag", 1),
                                                            ("GraphNumberOfLeadingZeros", 0),
                                                            ("GraphNumberOfDecimalPlaces", 3),
                                                            ("SavePlot_DirectoryPath", os.path.join(os.getcwd(), "SavedImagesFolder")),
                                                            ("KeepPlotterWindowAlwaysOnTopFlag", 0),
                                                            ("RemoveTitleBorderCloseButtonAndDisallowWindowMoveFlag", 0),
                                                            ("AllowResizingOfWindowFlag", 1)])

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_Object = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_SetupDict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_Object, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
                print("Failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_ForceTorqueReaderOmegaDFGRS5 = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    print("Starting main loop 'test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if CSVdataLogger_OPEN_FLAG == 1:

            CSVdataLogger_MostRecentDict = CSVdataLogger_Object.GetMostRecentDataDict()

            if "Time" in CSVdataLogger_MostRecentDict:
                CSVdataLogger_MostRecentDict_Time = CSVdataLogger_MostRecentDict["Time"]
                CSVdataLogger_MostRecentDict_IsSavingFlag = CSVdataLogger_MostRecentDict["IsSavingFlag"]

        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1:

            ForceTorqueReaderOmegaDFGRS5_MostRecentDict = ForceTorqueReaderOmegaDFGRS5_Object.GetMostRecentDataDict()

            if "Time" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict and "Measurement_DictOfConvertedValues" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict:
                ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_N = ForceTorqueReaderOmegaDFGRS5_MostRecentDict["Measurement_DictOfConvertedValues"]["N"]
                ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_N = ForceTorqueReaderOmegaDFGRS5_MostRecentDict["MeasurementDerivative_DictOfConvertedValues"]["N"]
                
                ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_Nm = ForceTorqueReaderOmegaDFGRS5_MostRecentDict["Measurement_DictOfConvertedValues"]["Nm"]
                ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_Nm = ForceTorqueReaderOmegaDFGRS5_MostRecentDict["MeasurementDerivative_DictOfConvertedValues"]["Nm"]

                ###################################################
                if ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_N == -11111.0:
                    TorqueInsteadOfForceFlag = 1

                elif ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_Nm == -11111.0:
                    TorqueInsteadOfForceFlag = 0

                else:
                    TorqueInsteadOfForceFlag = -1
                ###################################################

        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1:

            ##########################################################################################################
            if ResetPeak_EventNeedsToBeFiredFlag == 1:
                ForceTorqueReaderOmegaDFGRS5_Object.ResetPeak()
                ResetPeak_EventNeedsToBeFiredFlag = 0
            ##########################################################################################################

            ##########################################################################################################
            if ResetTare_EventNeedsToBeFiredFlag == 1:
                ForceTorqueReaderOmegaDFGRS5_Object.ResetTare()
                ResetTare_EventNeedsToBeFiredFlag = 0
            ##########################################################################################################

        ###################################################
        ###################################################

        #################################################### SET's
        ####################################################
        ####################################################
        if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1 and CSVdataLogger_OPEN_FLAG == 1:

            ####################################################
            ####################################################
            ListToWrite = [CurrentTime_MainLoopThread,
                            ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_N,
                            ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_N,
                            ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_Nm,
                            ForceTorqueReaderOmegaDFGRS5_MostRecentDictMeasurementDerivative_DictOfConvertedValues_Nm]
            ####################################################
            ####################################################

            CSVdataLogger_Object.AddDataToCSVfile_ExternalFunctionCall(ListToWrite)
        ####################################################
        ####################################################
        ####################################################

        #################################################### SET's
        ####################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_Object.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_MostRecentDict_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess >= MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents"]/1000.0 + 0.001:

                        if TorqueInsteadOfForceFlag == 0:

                            MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot(["Torque (Nm)"],
                                                                                                            [CurrentTime_MainLoopThread]*1,
                                                                                                            [ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_N])

                        else:
                            MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot(["Torque (Nm)"],
                                                                                                            [CurrentTime_MainLoopThread]*1,
                                                                                                            [ForceTorqueReaderOmegaDFGRS5_MostRecentDict_Measurement_DictOfConvertedValues_Nm])

                        LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_MainLoopThread
            ####################################################

        ####################################################
        ####################################################

        time.sleep(0.005)
        
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################
    print("Exiting main program 'test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class.")

    #################################################
    if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1:
        ForceTorqueReaderOmegaDFGRS5_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if CSVdataLogger_OPEN_FLAG == 1:
        CSVdataLogger_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_Object.ExitProgram_Callback()
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################