# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision A, 12/27/2023

Verified working on: Python 3.8 for Windows 10/11 64-bit and Raspberry Pi Buster (may work on Mac in non-GUI mode, but haven't tested yet).
'''

__author__ = 'reuben.brewer'

##########################################
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from CSVdataLogger_ReubenPython3Class import *
from MyPrint_ReubenPython2and3Class import *
from ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class import *
##########################################

##########################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
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

    global ForceTorqueReaderOmegaDFGRS5_ListOfObjects
    global ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG
    global SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global CSVdataLogger_ReubenPython3ClassObject
    global CSVdataLogger_OPEN_FLAG
    global SHOW_IN_GUI_CSVdataLogger_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1 and SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG == 1:
                for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                    ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if CSVdataLogger_OPEN_FLAG == 1 and SHOW_IN_GUI_CSVdataLogger_FLAG == 1:
                CSVdataLogger_ReubenPython3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
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

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
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

        Tab_CSVdataLogger = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_CSVdataLogger, text='   CSVdataLogger   ')

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

    '''
    #################################################
    #################################################
    ResetLatchedAlarms_Button = Button(ButtonsFrame, text="Reset Alarms", state="normal", width=20, command=lambda: ResetLatchedAlarms_Button_Response())
    ResetLatchedAlarms_Button.grid(row=0, column=2, padx=10, pady=10, columnspan=1, rowspan=1)
    #################################################
    #################################################
    '''

    ##########################################################################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
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

'''
##########################################################################################################
##########################################################################################################
def ResetLatchedAlarms_Button_Response():
    global ResetLatchedAlarms_EventNeedsToBeFiredFlag

    ResetLatchedAlarms_EventNeedsToBeFiredFlag = 1

##########################################################################################################
##########################################################################################################
'''

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

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

    #global ResetLatchedAlarms_EventNeedsToBeFiredFlag
    #ResetLatchedAlarms_EventNeedsToBeFiredFlag = 0

    global SumOfForcesFromAllSensors_lb
    SumOfForcesFromAllSensors_lb = 0

    global SumOfForceDerivativesFromAllSensors_lb
    SumOfForceDerivativesFromAllSensors_lb = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global ForceTorqueReaderOmegaDFGRS5_ListOfObjects
    ForceTorqueReaderOmegaDFGRS5_ListOfObjects = list()

    global ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG
    ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG = 0

    global ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList
    ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList = ["AV0K59E0A"]

    global ForceTorqueReaderOmegaDFGRS5_NumberOfSensors
    ForceTorqueReaderOmegaDFGRS5_NumberOfSensors = len(ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList)

    global ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG_ListOfFlags
    ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG_ListOfFlags = [0]*ForceTorqueReaderOmegaDFGRS5_NumberOfSensors

    #################################################
    global ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts
    ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts = list()

    for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
        ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts.append(dict())
    #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global CSVdataLogger_ReubenPython3ClassObject

    global CSVdataLogger_OPEN_FLAG
    CSVdataLogger_OPEN_FLAG = -1

    global CSVdataLogger_MostRecentDict
    CSVdataLogger_MostRecentDict = dict()

    global CSVdataLogger_MostRecentDict_Time
    CSVdataLogger_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1

    global LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = -11111.0
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_ForceTorqueReaderOmegaDFGRS5 = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    #################################################

    #################################################
    #################################################
    for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):

        #################################################
        global ForceTorqueReaderOmegaDFGRS5_GUIparametersDict
        ForceTorqueReaderOmegaDFGRS5_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_ForceTorqueReaderOmegaDFGRS5_FLAG),
                                        ("root", Tab_ForceTorqueReaderOmegaDFGRS5),
                                        ("EnableInternal_MyPrint_Flag", 0),
                                        ("NumberOfPrintLines", 10),
                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                        ("GUI_ROW", GUI_ROW_ForceTorqueReaderOmegaDFGRS5 + Index),
                                        ("GUI_COLUMN", GUI_COLUMN_ForceTorqueReaderOmegaDFGRS5),
                                        ("GUI_PADX", GUI_PADX_ForceTorqueReaderOmegaDFGRS5),
                                        ("GUI_PADY", GUI_PADY_ForceTorqueReaderOmegaDFGRS5),
                                        ("GUI_ROWSPAN", GUI_ROWSPAN_ForceTorqueReaderOmegaDFGRS5),
                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_ForceTorqueReaderOmegaDFGRS5)])
        #################################################

        #################################################
        global ForceTorqueReaderOmegaDFGRS5_setup_dict
        ForceTorqueReaderOmegaDFGRS5_setup_dict = dict([("GUIparametersDict", ForceTorqueReaderOmegaDFGRS5_GUIparametersDict),
                                                                                    ("DesiredSerialNumber_USBtoSerialConverter", ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList[Index]),
                                                                                    ("NameToDisplay_UserSet", "ForceTorqueReaderOmegaDFGRS5: Sensor " + ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList[Index]),
                                                                                    ("ReadingModeString", "RealTime_CUR"), #["RealTime_CUR",  "PeakTension_PT", "PeakCompression_PC",  "PeakClockwise_PCW", "PeakCounterClockwise_PCCW"]
                                                                                    ("SamplesPerSecond", 250), #[0, 2, 5, 10, 25, 50, 125, 250]
                                                                                    ("FilterExponent0to10ForNumberOfSamplesToBeAveraged", 2),
                                                                                    ("AutoShutoffTimeIntegerMinutes0to30", 10),
                                                                                    ("DedicatedRxThread_TimeToSleepEachLoop", 0.001),
                                                                                    ("DedicatedTxThread_TimeToSleepEachLoop", 0.010),
                                                                                    ("DedicatedTxThread_TxMessageToSend_Queue_MaxSize", 1),
                                                                                    ("ForceDerivative_ExponentialSmoothingFilterLambda", 0.95)])
        #################################################

        #################################################
        if USE_ForceTorqueReaderOmegaDFGRS5_FLAG == 1:
            try:
                ForceTorqueReaderOmegaDFGRS5_ListOfObjects.append(ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class(ForceTorqueReaderOmegaDFGRS5_setup_dict))
                ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG_ListOfFlags[Index] = ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].OBJECT_CREATED_SUCCESSFULLY_FLAG

            except:
                exceptions = sys.exc_info()[0]
                print("ForceTorqueReaderOmegaDFGRS5_ReubenPython3ClassObject __init__ on SerialNumber" +
                      ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList[Index] +
                      ", exceptions: %s" % exceptions)

                traceback.print_exc()
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG = 1
    for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
        for IndividualFlag in ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG_ListOfFlags:
            if IndividualFlag != 1:
                ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG = 0
    #################################################
    #################################################

    #################################################
    #################################################
    #################################################

    #################################################
    #################################################
    #################################################
    global CSVdataLogger_ReubenPython3ClassObject_GUIparametersDict
    CSVdataLogger_ReubenPython3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_CSVdataLogger_FLAG),
                                    ("root", Tab_CSVdataLogger),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_CSVdataLogger),
                                    ("GUI_COLUMN", GUI_COLUMN_CSVdataLogger),
                                    ("GUI_PADX", GUI_PADX_CSVdataLogger),
                                    ("GUI_PADY", GUI_PADY_CSVdataLogger),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_CSVdataLogger),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_CSVdataLogger)])
    #################################################
    #################################################

    #################################################
    CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList = ["Time (S)",
                                                                                    "SumOfForcesFromAllSensors (lb)"]
    #################################################

    #################################################
    for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
        CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList.append("Force " + str(Index) + " (lb)")
    #################################################

    #################################################
    CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList.append("SumOfForceDerivativesFromAllSensors (lb/s)")
    #################################################

    #################################################
    for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
        CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList.append("ForceDerivative " + str(Index) + " (lb/s)")
    #################################################

    #################################################
    print("CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList: " + str(CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList))
    #################################################

    #################################################
    #################################################
    global CSVdataLogger_ReubenPython3ClassObject_setup_dict
    CSVdataLogger_ReubenPython3ClassObject_setup_dict = dict([("GUIparametersDict", CSVdataLogger_ReubenPython3ClassObject_GUIparametersDict),
                                                                                ("NameToDisplay_UserSet", "CSVdataLogger"),
                                                                                ("CSVfile_DirectoryPath", os.getcwd() + "\\CSVfiles"),
                                                                                ("FileNamePrefix", "CSV_file_"),
                                                                                ("VariableNamesForHeaderList", CSVdataLogger_ReubenPython3ClassObject_setup_dict_VariableNamesForHeaderList),
                                                                                ("MainThread_TimeToSleepEachLoop", 0.002),
                                                                                ("SaveOnStartupFlag", 0)])

    if USE_CSVdataLogger_FLAG == 1:
        try:
            CSVdataLogger_ReubenPython3ClassObject = CSVdataLogger_ReubenPython3Class(CSVdataLogger_ReubenPython3ClassObject_setup_dict)
            CSVdataLogger_OPEN_FLAG = CSVdataLogger_ReubenPython3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("CSVdataLogger_ReubenPython3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_NameList
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_NameList = ["SumOfForcesFromAllSensors_lb", "SumOfForceDerivativesFromAllSensors_lb", "Channel2", "Channel3", "Channel4", "Channel5"]

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_ColorList
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_ColorList = ["Red", "Green", "Blue", "Black", "Purple", "Orange"]

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                                                ("GraphCanvasWidth", 890),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 0.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists",
                                                                                            dict([("NameList", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_NameList),
                                                                                                  ("ColorList", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_ColorList)])),
                                                                                        ("NumberOfDataPointToPlot", 50),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 1),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", -0.0015),
                                                                                        ("Y_max", 0.0015),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    if USE_ForceTorqueReaderOmegaDFGRS5_FLAG == 1 and ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG != 1:
        print("Failed to open ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MyPrint_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_CSVdataLogger_FLAG == 1 and CSVdataLogger_OPEN_FLAG != 1:
        print("Failed to open CSVdataLogger_ReubenPython3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0 or CSVdataLogger_ReubenPython3ClassObject.IsSaving() == 1):

        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1:

            SumOfForcesFromAllSensors_lb = 0
            SumOfForceDerivativesFromAllSensors_lbPerSec = 0
            for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index] = ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].GetMostRecentDataDict()

                if "Time" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index] and "MeasurementForce_DictOfConvertedValues" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]:
                    SumOfForcesFromAllSensors_lb = SumOfForcesFromAllSensors_lb + ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]["MeasurementForce_DictOfConvertedValues"]["lbF"]
                    SumOfForceDerivativesFromAllSensors_lbPerSec = SumOfForceDerivativesFromAllSensors_lbPerSec + ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]["MeasurementForceDerivative_DictOfConvertedValues"]["lbF"]

            #print("SumOfForcesFromAllSensors_lb: " + str(SumOfForcesFromAllSensors_lb) + ", SumOfForceDerivativesFromAllSensors_lbPerSec: " + str(SumOfForceDerivativesFromAllSensors_lbPerSec))
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1:

            ##########################################################################################################
            if ResetPeak_EventNeedsToBeFiredFlag == 1:

                for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                    ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].ResetPeak()

                ResetPeak_EventNeedsToBeFiredFlag = 0
            ##########################################################################################################

            ##########################################################################################################
            if ResetTare_EventNeedsToBeFiredFlag == 1:

                for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                    ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].ResetTare()

                ResetTare_EventNeedsToBeFiredFlag = 0
            ##########################################################################################################

            '''
            ##########################################################################################################
            if ResetLatchedAlarms_EventNeedsToBeFiredFlag == 1:

                for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                    ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].ResetLatchedAlarms()

                ResetLatchedAlarms_EventNeedsToBeFiredFlag = 0
            ##########################################################################################################
            '''

        ###################################################
        ###################################################

        #################################################### SET's
        ####################################################
        ####################################################
        if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1 and CSVdataLogger_OPEN_FLAG == 1:

            ####################################################
            ####################################################
            ListToWrite = []
            ListToWrite.append(CurrentTime_MainLoopThread)
            ListToWrite.append(SumOfForcesFromAllSensors_lb)

            ####################################################
            for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                if "Time" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index] and "MeasurementForce_DictOfConvertedValues" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]:
                    ListToWrite.append(ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]["MeasurementForce_DictOfConvertedValues"]["lbF"])
            ####################################################

            ListToWrite.append(SumOfForceDerivativesFromAllSensors_lbPerSec)

            ####################################################
            for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
                if "Time" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index] and "MeasurementForce_DictOfConvertedValues" in ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]:
                    ListToWrite.append(ForceTorqueReaderOmegaDFGRS5_MostRecentDict_ListOfDicts[Index]["MeasurementForceDerivative_DictOfConvertedValues"]["lbF"])
            ####################################################

            ####################################################
            ####################################################

            CSVdataLogger_ReubenPython3ClassObject.AddDataToCSVfile_ExternalFunctionCall(ListToWrite)
        ####################################################
        ####################################################
        ####################################################

        #################################################### SET's
        ####################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess >= 0.030:
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_NameList[0:ForceTorqueReaderOmegaDFGRS5_NumberOfSensors],
                        #                                                                                                        [CurrentTime_MainLoopThread]*ForceTorqueReaderOmegaDFGRS5_NumberOfSensors,
                        #                                                                                                        [CurrentTime_MainLoopThread]*ForceTorqueReaderOmegaDFGRS5_NumberOfSensors)

                        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_NameList[0:2],
                                                                                                        [CurrentTime_MainLoopThread]*2,
                                                                                                        [SumOfForcesFromAllSensors_lb, SumOfForceDerivativesFromAllSensors_lbPerSec])


                        LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_MainLoopThread
            ####################################################

        ####################################################
        ####################################################

        time.sleep(0.010)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class.")

    #################################################
    if ForceTorqueReaderOmegaDFGRS5_OPEN_FLAG == 1:
        for Index in range(0, ForceTorqueReaderOmegaDFGRS5_NumberOfSensors):
            ForceTorqueReaderOmegaDFGRS5_ListOfObjects[Index].ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if CSVdataLogger_OPEN_FLAG == 1:
        CSVdataLogger_ReubenPython3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################