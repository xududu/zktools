# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from configparser import RawConfigParser
import ast
import ctypes
from service import zkapi

# 设置图标
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# 读取配置文件
zk_config_obj = RawConfigParser()
zk_config_obj.read('./config/config.cfg')
Connect_list_str = zk_config_obj.get('zkConfig', 'Connect_list')
# 转化为python列表
Connect_list = ast.literal_eval(Connect_list_str)
# 获取列表长度
row_num = len(Connect_list)


class Ui_ZKTools(object):
    def setupUi(self, ZKTools):
        # 设置图标
        ZKTools.setWindowIcon(QtGui.QIcon('./logo.jpg'))
        ZKTools.setObjectName("ZKTools")
        ZKTools.setEnabled(True)
        ZKTools.resize(1201, 631)
        self.save_but = QtWidgets.QPushButton(ZKTools)
        self.save_but.setGeometry(QtCore.QRect(10, 580, 271, 51))
        self.save_but.setObjectName("save_but")
        self.close_but = QtWidgets.QPushButton(ZKTools)
        self.close_but.setGeometry(QtCore.QRect(530, 580, 331, 51))
        self.close_but.setObjectName("close_but")
        self.zk_text_input = QtWidgets.QPlainTextEdit(ZKTools)
        self.zk_text_input.setGeometry(QtCore.QRect(10, 100, 851, 471))
        self.zk_text_input.setPlainText("")
        self.zk_text_input.setObjectName("zk_text_input")
        self.text_titile_lable = QtWidgets.QLabel(ZKTools)
        self.text_titile_lable.setGeometry(QtCore.QRect(420, 80, 71, 16))
        self.text_titile_lable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_titile_lable.setObjectName("text_titile_lable")
        # 右上角地址表格
        self.zk_addr_table = QtWidgets.QTableWidget(ZKTools)
        self.zk_addr_table.setGeometry(QtCore.QRect(870, 30, 321, 271))
        self.zk_addr_table.setObjectName("zk_addr_table")
        # 设置行数和列数
        self.zk_addr_table.setColumnCount(2)
        self.zk_addr_table.setRowCount(row_num)
        # 设置竖直方向个数
        for vertical_header_num in range(row_num):
            item = QtWidgets.QTableWidgetItem()
            self.zk_addr_table.setVerticalHeaderItem(vertical_header_num, item)

        # 设置横向个数
        for horizontal_num in range(2):
            item = QtWidgets.QTableWidgetItem()
            self.zk_addr_table.setHorizontalHeaderItem(horizontal_num, item)

        # 绘制表格
        for abscissa in range(2):
            for ordinate in range(row_num):
                item = QtWidgets.QTableWidgetItem()
                self.zk_addr_table.setItem(ordinate, abscissa, item)
        self.zk_addr_table.horizontalHeader().setVisible(True)
        self.zk_addr_table.horizontalHeader().setCascadingSectionResizes(False)
        self.zk_addr_table.horizontalHeader().setDefaultSectionSize(155)
        self.zk_addr_table.horizontalHeader().setHighlightSections(True)

        self.check_group_box = QtWidgets.QGroupBox(ZKTools)
        self.check_group_box.setGeometry(QtCore.QRect(870, 310, 321, 311))
        self.check_group_box.setObjectName("check_group_box")
        # 组内check_box定义
        self.checkBox_9 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_9.setGeometry(QtCore.QRect(0, 190, 91, 21))
        # self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_8 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_8.setGeometry(QtCore.QRect(0, 170, 91, 21))
        # self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_7 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_7.setGeometry(QtCore.QRect(0, 150, 91, 21))
        # self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_6 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_6.setGeometry(QtCore.QRect(0, 130, 91, 21))
        # self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_5 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_5.setGeometry(QtCore.QRect(0, 110, 91, 21))
        # self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 90, 91, 21))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 70, 91, 21))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 50, 91, 21))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.check_group_box)
        self.checkBox.setGeometry(QtCore.QRect(0, 30, 91, 19))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.zk_title_input = QtWidgets.QPlainTextEdit(ZKTools)
        self.zk_title_input.setGeometry(QtCore.QRect(10, 30, 851, 31))
        self.zk_title_input.setPlainText("")
        self.zk_title_input.setObjectName("zk_title_input")
        self.titile_lable = QtWidgets.QLabel(ZKTools)
        self.titile_lable.setGeometry(QtCore.QRect(410, 10, 91, 16))
        self.titile_lable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titile_lable.setObjectName("titile_lable")

        self.retranslateUi(ZKTools)
        QtCore.QMetaObject.connectSlotsByName(ZKTools)
        # 点击事件
        self.save_but.clicked.connect(self.save_clicked)
        self.close_but.clicked.connect(self.close)

    def retranslateUi(self, ZKTools):
        _translate = QtCore.QCoreApplication.translate
        ZKTools.setWindowTitle(_translate("ZKTools", "ZkTools"))
        self.save_but.setText(_translate("ZKTools", "确认发布"))
        self.close_but.setText(_translate("ZKTools", "退出"))
        self.text_titile_lable.setText(_translate("ZKTools", "文本"))
        # 右上角表格内容填充
        # 设置第一列标号
        for vertical_header_num in range(row_num):
            item = self.zk_addr_table.verticalHeaderItem(vertical_header_num)
            num_text = vertical_header_num + 1
            item.setText(_translate("ZKTools", "%s") % num_text)
        # 设置第一行标题
        item = self.zk_addr_table.horizontalHeaderItem(0)
        item.setText(_translate("ZKTools", "组名"))
        item = self.zk_addr_table.horizontalHeaderItem(1)
        item.setText(_translate("ZKTools", "zk地址"))
        __sortingEnabled = self.zk_addr_table.isSortingEnabled()
        self.zk_addr_table.setSortingEnabled(False)

        # 填充表格内容
        for abscissa in range(2):
            for ordinate in range(row_num):
                connect_dic = Connect_list[ordinate]
                # 取字典内容填充
                for group_name in connect_dic:
                    item = self.zk_addr_table.item(ordinate, abscissa)
                    item.setText(_translate("ZKTools", "%s") % group_name)
                    # 取地址
                    address = connect_dic[group_name]
                    address_column = 1
                    item = self.zk_addr_table.item(ordinate, address_column)
                    item.setText(_translate("ZKTools", "%s") % address)
        self.zk_addr_table.setSortingEnabled(__sortingEnabled)

        self.check_group_box.setTitle(_translate("ZKTools", "勾选需要同步到的组"))

        # 填充check_box内容
        self.checkBox_9.setText(_translate("ZKTools", "9"))
        self.checkBox_8.setText(_translate("ZKTools", "8"))
        self.checkBox_7.setText(_translate("ZKTools", "7"))
        self.checkBox_6.setText(_translate("ZKTools", "6"))
        self.checkBox_5.setText(_translate("ZKTools", "5"))
        self.checkBox_4.setText(_translate("ZKTools", "4"))
        self.checkBox_3.setText(_translate("ZKTools", "3"))
        self.checkBox_2.setText(_translate("ZKTools", "2"))
        self.checkBox.setText(_translate("ZKTools", "1"))

        self.titile_lable.setText(_translate("ZKTools", "节点名"))

    # 保存按钮触发
    def save_clicked(self, event):
        _translate = QtCore.QCoreApplication.translate
        node_name = self.zk_title_input.toPlainText().strip()
        if not node_name:
            self.zk_title_input.setPlainText(_translate("ZKTools", "在这写节点名！"))
            return False
        input_text = self.zk_text_input.toPlainText().strip()
        if not input_text:
            self.zk_text_input.setPlainText(_translate("ZKTools", "在这写zk文本！"))
            return False
        # 点击发布按钮后的确认框判断
        reply = QMessageBox.question(self,
                                     "Are you sure?",
                                     "确认发布?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('确定发布。')
        else:
            return False

        for children_box in self.check_group_box.children():
            # 获取每一个check_box的选中状态
            children_box_status = children_box.isChecked()
            if children_box_status:
                # 获取zk地址
                children_box_name = children_box.text()
                children_box_index = int(children_box_name) - 1
                try:
                    connect_dic = Connect_list[children_box_index]
                except IndexError:
                    self.check_group_box.setTitle(_translate("ZKTools", "勾选的组超出了范围！"))
                    return False
                else:
                    for zk_address in connect_dic.values():
                        # 实例化zk链接
                        zk_obj = zkapi.ZkApi(zk_hosts=zk_address)
                        zk_obj.upload_zk_text(node_name=node_name, input_text=input_text)
        self.check_group_box.setTitle(_translate("ZKTools", "发布成功！"))
        return True

