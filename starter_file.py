import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from home import Ui_MainWindow
from daily_inspection import UIDailyInspection
from ppm import Ui_PPM
from preinstallation import Ui_Preinstallation


class Window1(QtWidgets.QMainWindow, Ui_Preinstallation):

    def __init__(self, report):
        super(Window1, self).__init__()
        self.ui = self.setupUi(self)
        self.hospital.setText(report['hospital'])
        self.department.setText(report['department'])
        self.equipment.setText(report['equipment_name'])
        self.floor.setText(str(report['floor']))
        self.room.setText(report['room'])
        index = 0
        data = report['data']
        for i in range(1, 5):
            self.table.setItem(i, 1, QTableWidgetItem(str(data[index])))
            index += 1
            self.table.setItem(i, 2, QTableWidgetItem(str(data[index])))
            index += 1
            self.table.setItem(i, 3, QTableWidgetItem(str(data[index])))
            index += 1
        self.name.setText(data[index])
        self.signature.setText(data[index])
        index += 1
        if isinstance(type(data[index]), str):
            self.date.setText(data[index])
        else:
            self.date.setText(data[index].strftime("%m/%d/%Y"))


class Window2(QtWidgets.QMainWindow, UIDailyInspection):

    def __init__(self, report):
        super(Window2, self).__init__()
        self.ui = self.setupUi(self)
        self.hospital.setText(report['hospital'])
        self.department.setText(report['department'])
        self.equipment.setText(report['equipment_name'])
        self.floor.setText(str(report['floor']))
        self.room.setText(report['room'])
        self.serial.setText(report['serial'])
        # Date Table
        for i in range(1, 8):
            self.data_table.setItem(0, i, QTableWidgetItem(report['date'][i-1].strftime("%m/%d/%Y")))

        index = 0
        data = report['data']
        
        # Foreign substances.
        for i in range(7):
            self.tab1.setItem(0, i, QTableWidgetItem(data[index]))
            index += 1
        # Damage or cracks.
        for i in range(7):
            self.tab1.setItem(1, i, QTableWidgetItem(data[index]))
            index += 1
        #  Broken, loose, or worn battery pins.
        for i in range(7):
            self.tab2.setItem(0, i, QTableWidgetItem(data[index]))
            index += 1
        # Damaged or leaking battery.
        for i in range(7):
            self.tab2.setItem(1, i, QTableWidgetItem(data[index]))
            index += 1
        # Spare battery available.
        for i in range(7):
            self.tab2.setItem(2, i, QTableWidgetItem(data[index]))
            index += 1
        # Cracking,damage, broken, or bent parts or pins.
        for i in range(7):
            self.tab3.setItem(0, i, QTableWidgetItem(data[index]))
            index += 1
        # Use By date.
        for i in range(7):
            self.tab4.setItem(0, i, QTableWidgetItem(data[index]))
            index += 1
        # Spare electrodes available.
        for i in range(7):
            self.tab4.setItem(1, i, QTableWidgetItem(data[index]))
            index += 1
        # Damaged, opened package.
        for i in range(7):
            self.tab4.setItem(2, i, QTableWidgetItem(data[index]))
            index += 1
        # Momentary illumination of self-test messages and LEDs.
        for i in range(7):
            self.tab5.setItem(0, i, QTableWidgetItem(data[index]))
            index += 1
        # Speaker beep.
        for i in range(7):
            self.tab5.setItem(1, i, QTableWidgetItem(data[index]))
            index += 1
        # Two Fully charged batteries.
        for i in range(7):
            self.tab5.setItem(2, i, QTableWidgetItem(data[index]))
            index += 1
        # Service indicator.
        for i in range(7):
            self.tab5.setItem(3, i, QTableWidgetItem(data[index]))
            index += 1


class Window3(QtWidgets.QMainWindow, Ui_PPM):

    def __init__(self, report):
        super(Window3, self).__init__()
        self.setupUi(self)
        self.hospital.setText(report['hospital'])
        self.department.setText(report['department'])
        self.equipment.setText(report['equipment_name'])
        self.floor.setText(str(report['floor']))
        self.room.setText(report['room'])
        index = 0
        data = report['data']
        # LIGHTING: row index 2:4
        for i in range(2, 5):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[index].strftime("%m/%d/%Y")))
            index += 1
            self.tableWidget.setItem(i, 4, QTableWidgetItem(data[index]))
            index += 1

        # ELECTRICAL row index 7:8
        for i in range(7, 9):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[index].strftime("%m/%d/%Y")))
            index += 1
            self.tableWidget.setItem(i, 4, QTableWidgetItem(data[index]))
            index += 1
        # SAFETY row index 11:13
        for i in range(11, 14):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[index].strftime("%m/%d/%Y")))
            index += 1
            self.tableWidget.setItem(i, 4, QTableWidgetItem(data[index]))
            index += 1
        # HVAC/R and PNEUMATICS 16:19
        for i in range(16, 20):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[index]))
            index += 1
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[index].strftime("%m/%d/%Y")))
            index += 1
            self.tableWidget.setItem(i, 4, QTableWidgetItem(data[index]))
            index += 1


def pop_win1(report):
    global app1
    app1 = Window1(report)
    app1.show()


def pop_win2(report):
    global app2
    app2 = Window2(report)
    app2.show()


def pop_win3(report):
    global app3
    app3 = Window3(report)
    app3.show()


class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.CCU = pd.read_excel('data/CCU_Equipment_List.xlsx')
        self.OR = pd.read_excel('data/OR_Equipment_List.xlsx')
        self.out_patient = pd.read_excel('data/Out_Patient_Equipment_List.xlsx')

        # Connections
        self.ui.dep.currentIndexChanged.connect(lambda index: self.get_equipment(index))
        self.ui.equipment.currentTextChanged.connect(lambda equip: self.set_serial_num_menu(equip))
        self.ui.report.currentIndexChanged.connect(lambda index: self.show_report(index))

    def get_equipment(self, index):
        if index == 1:
            equipments = set(self.CCU.iloc[:, 0].tolist())
        elif index == 2:
            equipments = set(self.OR.iloc[:, 0].tolist())
        elif index == 3:
            equipments = set(self.out_patient.iloc[:, 0].tolist())
        else:
            equipments = []
        self.set_equipment_menu(equipments)

    def set_equipment_menu(self, equipments):
        self.ui.equipment.clear()
        self.ui.equipment.addItem('Equipment')
        self.ui.equipment.addItems(equipments)

    def set_serial_num_menu(self, equip):
        department_index = self.ui.dep.currentIndex()
        indices = []
        serial_nums = []
        if department_index == 1:
            for i in range(len(self.CCU)):
                if equip == self.CCU.iloc[i, 0]:
                    indices.append(i)
                    serial_nums.append(self.CCU.iloc[i]['Serial Number'])
        elif department_index == 2:
            for i in range(len(self.OR)):
                if equip == self.OR.iloc[i, 0]:
                    indices.append(i)
                    serial_nums.append(self.OR.iloc[i]['Serial Number'])
        elif department_index == 3:
            for i in range(len(self.out_patient)):
                if equip == self.out_patient.iloc[i, 0]:
                    indices.append(i)
                    serial_nums.append(self.out_patient.iloc[i]['Serial Number'])

        self.ui.serial_num.clear()
        self.ui.serial_num.addItem('Serial Number')
        self.ui.serial_num.addItems(serial_nums)

    def show_report(self, index):
        if index == 1:
            report = self.get_preinstallation()
            pop_win1(report)
        elif index == 2:
            report = self.get_daily_inspection()
            pop_win2(report)
        elif index == 3:
            report = self.get_ppm()
            pop_win3(report)

    def get_daily_inspection(self):
        report = {}
        equipment_name, serial_num, dep, df = self.get_data()
        if df is not None:
            report['hospital'] = 'X'
            report['department'] = dep
            report['equipment_name'] = equipment_name
            report['floor'] = df['Floor Number']
            report['room'] = str(df['Room'])
            report['serial'] = serial_num
            df_daily = pd.read_excel('data/Dialy_inspection.xlsx')
            report['date'] = df_daily.iloc[1][1:].tolist()
            for i in range(len(df_daily)):
                if serial_num == df_daily.iloc[i][0]:
                    data = df_daily.iloc[i]
                    break

            report['data'] = data[1:].tolist()
        return report

    def get_preinstallation(self):
        report = {}
        equipment_name, serial_num, dep, df = self.get_data()
        if df is not None:
            report['hospital'] = 'X'
            report['department'] = dep
            report['equipment_name'] = equipment_name
            report['floor'] = df['Floor Number']
            report['room'] = str(df['Room'])
            df_preinst = pd.read_excel('data/Pre_installation.xlsx')
            for i in range(len(df_preinst)):
                if serial_num == df_preinst.iloc[i][0]:
                    data = df_preinst.iloc[i]
                    break
            report['data'] = data[1:].tolist()
            return report

    def get_ppm(self):
        report = {}
        equipment_name, serial_num, dep, df = self.get_data()
        if df is not None:
            report['hospital'] = 'X'
            report['department'] = dep
            report['equipment_name'] = equipment_name
            report['floor'] = df['Floor Number']
            report['room'] = str(df['Room'])
            df_ppm = pd.read_excel('data/PPM.xlsx')
            for i in range(len(df_ppm)):
                if serial_num == df_ppm.iloc[i][0]:
                    data = df_ppm.iloc[i]
                    break
            report['data'] = data[1:].tolist()
        return report

    def get_data(self):
        department_index = self.ui.dep.currentIndex()
        equipment_name = self.ui.equipment.currentText()
        serial_num = self.ui.serial_num.currentText()

        if department_index == 1:
            department = 'CCU'
            for i in range(len(self.CCU)):
                if equipment_name == self.CCU.iloc[i, 0] and serial_num == self.CCU.iloc[i]['Serial Number']:
                    df = self.CCU.iloc[i]
        elif department_index == 2:
            department = 'OR'
            for i in range(len(self.OR)):
                if equipment_name == self.OR.iloc[i, 0] and serial_num == self.OR.iloc[i]['Serial Number']:
                    df = self.OR.iloc[i]
        elif department_index == 3:
            department = 'OUT_Patient'
            for i in range(len(self.out_patient)):
                if equipment_name == self.out_patient.iloc[i, 0] and serial_num == self.out_patient.iloc[i][
                    'Serial Number']:
                    df = self.out_patient.iloc[i]
        else:
            df = None

        return equipment_name, serial_num, department, df


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
