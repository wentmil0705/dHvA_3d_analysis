# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/wentworth/Desktop/skeaf_demo_sw/skeaf_demo_2/more.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_More(object):
    def setupUi(self, More):
        More.setObjectName("More")
        More.resize(411, 239)
        More.setMinimumSize(QtCore.QSize(320, 230))
        More.setSizeGripEnabled(False)
        self.layoutWidget = QtWidgets.QWidget(More)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 391, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.opacity_layout = QtWidgets.QHBoxLayout()
        self.opacity_layout.setObjectName("opacity_layout")
        self.opacity_label_layout = QtWidgets.QVBoxLayout()
        self.opacity_label_layout.setSpacing(20)
        self.opacity_label_layout.setObjectName("opacity_label_layout")
        self.fs_opacity_label = QtWidgets.QLabel(self.layoutWidget)
        self.fs_opacity_label.setObjectName("fs_opacity_label")
        self.opacity_label_layout.addWidget(self.fs_opacity_label)
        self.line_opacity_label = QtWidgets.QLabel(self.layoutWidget)
        self.line_opacity_label.setObjectName("line_opacity_label")
        self.opacity_label_layout.addWidget(self.line_opacity_label)
        self.trait_opacity_label = QtWidgets.QLabel(self.layoutWidget)
        self.trait_opacity_label.setObjectName("trait_opacity_label")
        self.opacity_label_layout.addWidget(self.trait_opacity_label)
        self.slice_opacity_label = QtWidgets.QLabel(self.layoutWidget)
        self.slice_opacity_label.setObjectName("slice_opacity_label")
        self.opacity_label_layout.addWidget(self.slice_opacity_label)
        self.opacity_layout.addLayout(self.opacity_label_layout)
        self.opacity_slider_layout = QtWidgets.QVBoxLayout()
        self.opacity_slider_layout.setSpacing(20)
        self.opacity_slider_layout.setObjectName("opacity_slider_layout")
        self.fs_opacity_slider = QtWidgets.QSlider(self.layoutWidget)
        self.fs_opacity_slider.setMinimumSize(QtCore.QSize(230, 0))
        self.fs_opacity_slider.setMaximum(10)
        self.fs_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fs_opacity_slider.setObjectName("fs_opacity_slider")
        self.opacity_slider_layout.addWidget(self.fs_opacity_slider)
        self.line_opacity_slider = QtWidgets.QSlider(self.layoutWidget)
        self.line_opacity_slider.setMinimumSize(QtCore.QSize(170, 0))
        self.line_opacity_slider.setMaximum(10)
        self.line_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.line_opacity_slider.setObjectName("line_opacity_slider")
        self.opacity_slider_layout.addWidget(self.line_opacity_slider)
        self.trait_opacity_slider = QtWidgets.QSlider(self.layoutWidget)
        self.trait_opacity_slider.setMaximum(10)
        self.trait_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.trait_opacity_slider.setObjectName("trait_opacity_slider")
        self.opacity_slider_layout.addWidget(self.trait_opacity_slider)
        self.slice_opacity_slider = QtWidgets.QSlider(self.layoutWidget)
        self.slice_opacity_slider.setMaximum(10)
        self.slice_opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.slice_opacity_slider.setObjectName("slice_opacity_slider")
        self.opacity_slider_layout.addWidget(self.slice_opacity_slider)
        self.opacity_layout.addLayout(self.opacity_slider_layout)
        self.opacity_line_layout = QtWidgets.QVBoxLayout()
        self.opacity_line_layout.setSpacing(20)
        self.opacity_line_layout.setObjectName("opacity_line_layout")
        self.fs_opacity_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.fs_opacity_line.setObjectName("fs_opacity_line")
        self.opacity_line_layout.addWidget(self.fs_opacity_line)
        self.line_opacity_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_opacity_line.setObjectName("line_opacity_line")
        self.opacity_line_layout.addWidget(self.line_opacity_line)
        self.trait_opacity_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.trait_opacity_line.setObjectName("trait_opacity_line")
        self.opacity_line_layout.addWidget(self.trait_opacity_line)
        self.slice_opacity_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.slice_opacity_line.setObjectName("slice_opacity_line")
        self.opacity_line_layout.addWidget(self.slice_opacity_line)
        self.opacity_layout.addLayout(self.opacity_line_layout)
        self.gridLayout.addLayout(self.opacity_layout, 0, 0, 1, 1)
        self.color_layout = QtWidgets.QHBoxLayout()
        self.color_layout.setObjectName("color_layout")
        self.backgroud_color_layout = QtWidgets.QHBoxLayout()
        self.backgroud_color_layout.setObjectName("backgroud_color_layout")
        self.background_button = QtWidgets.QPushButton(self.layoutWidget)
        self.background_button.setObjectName("background_button")
        self.backgroud_color_layout.addWidget(self.background_button)
        self.background_color_frame = QtWidgets.QFrame(self.layoutWidget)
        self.background_color_frame.setMinimumSize(QtCore.QSize(50, 0))
        self.background_color_frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.background_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_color_frame.setObjectName("background_color_frame")
        self.backgroud_color_layout.addWidget(self.background_color_frame)
        self.color_layout.addLayout(self.backgroud_color_layout)
        self.slice_color_layout = QtWidgets.QHBoxLayout()
        self.slice_color_layout.setSpacing(6)
        self.slice_color_layout.setObjectName("slice_color_layout")
        self.slice_color_button = QtWidgets.QPushButton(self.layoutWidget)
        self.slice_color_button.setObjectName("slice_color_button")
        self.slice_color_layout.addWidget(self.slice_color_button)
        self.slice_color_frame = QtWidgets.QFrame(self.layoutWidget)
        self.slice_color_frame.setMinimumSize(QtCore.QSize(50, 0))
        self.slice_color_frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.slice_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slice_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slice_color_frame.setObjectName("slice_color_frame")
        self.slice_color_layout.addWidget(self.slice_color_frame)
        self.color_layout.addLayout(self.slice_color_layout)
        self.gridLayout.addLayout(self.color_layout, 1, 0, 1, 1)
        self.magnetic_field_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.magnetic_field_checkbox.setObjectName("magnetic_field_checkbox")
        self.gridLayout.addWidget(self.magnetic_field_checkbox, 2, 0, 1, 1)

        self.retranslateUi(More)
        QtCore.QMetaObject.connectSlotsByName(More)

    def retranslateUi(self, More):
        _translate = QtCore.QCoreApplication.translate
        More.setWindowTitle(_translate("More", "More"))
        self.fs_opacity_label.setText(_translate("More", "FS Opacity"))
        self.line_opacity_label.setText(_translate("More", "Line Opacity"))
        self.trait_opacity_label.setText(_translate("More", "Trait Opacity"))
        self.slice_opacity_label.setText(_translate("More", "Slice Opacity"))
        self.background_button.setText(_translate("More", "Backgroud Color"))
        self.slice_color_button.setText(_translate("More", "Slice Color"))
        self.magnetic_field_checkbox.setText(_translate("More", "Magnetic Field"))
