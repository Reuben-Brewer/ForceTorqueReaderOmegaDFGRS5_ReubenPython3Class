###########################

ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class

Control class (including ability to hook to Tkinter GUI) to control/read load-cell data from the Omega DFG-RS5 Force/Torque Reader.

https://www.omega.com/en-us/force-and-strain-measurement/force-gauges/p/DFG-RS5-Series

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision B, 11/20/2024

Verified working on:

Python 3.11.

Windows 10/11 64-bit

Note For test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class_MultipleSensors.py:

1. The specific sensors that will be used (and, hence, the number of sensors) is set by the variable "ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList".

2a. In Windows, you can get each sensor's USB-serial-device serial number by following the instructions in the USBserialDevice_GettingSerialNumberInWindows.png screenshot in this folder.

2b. IMPORTANT: Do NOT include the last "A" in the USB-serial-device serial number. For example, if the serial number from Device Manager is "AH02WWDYA", then only list "AH02WWDY" in "ForceTorqueReaderOmegaDFGRS5_DevicesToReadSerialNumbersList".

3. In Windows, you can manually set the latency timer for each sensor by following the instructions in the USBserialDevice_SettingLatencyTimerManuallyInWindows.png screenshot in this folder.

Note for ExcelPlot_CSVdataLogger_ReubenPython3Code__ForceTorqueReaderOmegaDFGRS5_MultipleSensors:

1. This file is currently configured for 1 sensor, plotting only their sum.

###########################

###########################

Reader settings (consult Omega_DFG-RS5_Manual_M5251.pdf for more information):

###########################

########################### Python module installation instructions, all OS's

############

test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class_MultipleSensors.py, ListOfModuleDependencies: ['CSVdataLogger_ReubenPython3Class', 'ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class', 'MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class']

test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class_MultipleSensors.py, ListOfModuleDependencies_TestProgram: []

test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class_MultipleSensors.py, ListOfModuleDependencies_NestedLayers: ['ftd2xx', 'future.builtins', 'LowPassFilter_ReubenPython2and3Class', 'LowPassFilterForDictsOfLists_ReubenPython2and3Class', 'numpy', 'pexpect', 'psutil', 'serial', 'serial.tools']

test_program_for_ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class_MultipleSensors.py, ListOfModuleDependencies_All:['CSVdataLogger_ReubenPython3Class', 'ForceTorqueReaderOmegaDFGRS5_ReubenPython3Class', 'ftd2xx', 'future.builtins', 'LowPassFilter_ReubenPython2and3Class', 'LowPassFilterForDictsOfLists_ReubenPython2and3Class', 'MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'numpy', 'pexpect', 'psutil', 'serial', 'serial.tools']

pip install psutil

pip install pyserial (NOT pip install serial).

pip install ftd2xx, ##https://pypi.org/project/ftd2xx/ #version 1.3.3 as of 11/08/23. For SetAllFTDIdevicesLatencyTimer function.

############

############

ExcelPlot_CSVdataLogger_ReubenPython3Code_ForceTorqueReaderOmegaDFGRS5.py, ListOfModuleDependencies: ['pandas', 'win32com.client', 'xlsxwriter', 'xlutils.copy', 'xlwt']

ExcelPlot_CSVdataLogger_ReubenPython3Code_ForceTorqueReaderOmegaDFGRS5.py, ListOfModuleDependencies_TestProgram: []

ExcelPlot_CSVdataLogger_ReubenPython3Code_ForceTorqueReaderOmegaDFGRS5.py, ListOfModuleDependencies_NestedLayers: []

ExcelPlot_CSVdataLogger_ReubenPython3Code_ForceTorqueReaderOmegaDFGRS5.py, ListOfModuleDependencies_All:['pandas', 'win32com.client', 'xlsxwriter', 'xlutils.copy', 'xlwt']

pip install pywin32         #version 305.1 as of 10/17/24

pip install xlsxwriter      #version 3.2.0 as of 10/17/24. Might have to manually delete older version from /lib/site-packages if it was distutils-managed. Works overall, but the function ".set_size" doesn't do anything.

pip install xlutils         #version 2.0.0 as of 10/17/24

pip install xlwt            #version 1.3.0 as of 10/17/24

############

###########################

########################### FTDI installation instructions, Windows

(more to come)

###########################
