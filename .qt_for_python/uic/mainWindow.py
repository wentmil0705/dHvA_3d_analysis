# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/wentworth/Desktop/skeaf_demo_sw/skeaf_demo_2/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1415, 894)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.May_preFreq_ExtVal_OrbOut_splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.May_preFreq_ExtVal_OrbOut_splitter.sizePolicy().hasHeightForWidth())
        self.May_preFreq_ExtVal_OrbOut_splitter.setSizePolicy(sizePolicy)
        self.May_preFreq_ExtVal_OrbOut_splitter.setMinimumSize(QtCore.QSize(0, 500))
        self.May_preFreq_ExtVal_OrbOut_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.May_preFreq_ExtVal_OrbOut_splitter.setObjectName("May_preFreq_ExtVal_OrbOut_splitter")
        self.May_PreFre_splitter = QtWidgets.QSplitter(self.May_preFreq_ExtVal_OrbOut_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.May_PreFre_splitter.sizePolicy().hasHeightForWidth())
        self.May_PreFre_splitter.setSizePolicy(sizePolicy)
        self.May_PreFre_splitter.setMinimumSize(QtCore.QSize(700, 600))
        self.May_PreFre_splitter.setOrientation(QtCore.Qt.Vertical)
        self.May_PreFre_splitter.setObjectName("May_PreFre_splitter")
        self.mayavi_widget = MayaviQWidget(self.May_PreFre_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.mayavi_widget.sizePolicy().hasHeightForWidth())
        self.mayavi_widget.setSizePolicy(sizePolicy)
        self.mayavi_widget.setMinimumSize(QtCore.QSize(0, 600))
        self.mayavi_widget.setAutoFillBackground(False)
        self.mayavi_widget.setObjectName("mayavi_widget")
        self.predicted_frequencies_scroll_area = QtWidgets.QScrollArea(self.May_PreFre_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.predicted_frequencies_scroll_area.sizePolicy().hasHeightForWidth())
        self.predicted_frequencies_scroll_area.setSizePolicy(sizePolicy)
        self.predicted_frequencies_scroll_area.setMinimumSize(QtCore.QSize(0, 100))
        self.predicted_frequencies_scroll_area.setAutoFillBackground(True)
        self.predicted_frequencies_scroll_area.setWidgetResizable(True)
        self.predicted_frequencies_scroll_area.setObjectName("predicted_frequencies_scroll_area")
        self.predicted_frequencies_scroll_area_content = QtWidgets.QWidget()
        self.predicted_frequencies_scroll_area_content.setGeometry(QtCore.QRect(0, 0, 705, 96))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predicted_frequencies_scroll_area_content.sizePolicy().hasHeightForWidth())
        self.predicted_frequencies_scroll_area_content.setSizePolicy(sizePolicy)
        self.predicted_frequencies_scroll_area_content.setObjectName("predicted_frequencies_scroll_area_content")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.predicted_frequencies_scroll_area_content)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.predicted_frequencies_tabel_view = QtWidgets.QTableWidget(self.predicted_frequencies_scroll_area_content)
        self.predicted_frequencies_tabel_view.setObjectName("predicted_frequencies_tabel_view")
        self.predicted_frequencies_tabel_view.setColumnCount(0)
        self.predicted_frequencies_tabel_view.setRowCount(0)
        self.gridLayout_3.addWidget(self.predicted_frequencies_tabel_view, 0, 0, 1, 1)
        self.predicted_frequencies_scroll_area.setWidget(self.predicted_frequencies_scroll_area_content)
        self.ExtVal_OrbOut_splitter = QtWidgets.QSplitter(self.May_preFreq_ExtVal_OrbOut_splitter)
        self.ExtVal_OrbOut_splitter.setMinimumSize(QtCore.QSize(400, 600))
        self.ExtVal_OrbOut_splitter.setOrientation(QtCore.Qt.Vertical)
        self.ExtVal_OrbOut_splitter.setHandleWidth(4)
        self.ExtVal_OrbOut_splitter.setObjectName("ExtVal_OrbOut_splitter")
        self.extreme_value_widget = QtWidgets.QWidget(self.ExtVal_OrbOut_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.extreme_value_widget.sizePolicy().hasHeightForWidth())
        self.extreme_value_widget.setSizePolicy(sizePolicy)
        self.extreme_value_widget.setMinimumSize(QtCore.QSize(10, 10))
        self.extreme_value_widget.setAutoFillBackground(False)
        self.extreme_value_widget.setObjectName("extreme_value_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.extreme_value_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.extreme_value_layout = QtWidgets.QVBoxLayout()
        self.extreme_value_layout.setSpacing(2)
        self.extreme_value_layout.setObjectName("extreme_value_layout")
        self.ExtVal_SetPar_layout = QtWidgets.QHBoxLayout()
        self.ExtVal_SetPar_layout.setObjectName("ExtVal_SetPar_layout")
        self.extreme_value_label = QtWidgets.QLabel(self.extreme_value_widget)
        self.extreme_value_label.setObjectName("extreme_value_label")
        self.ExtVal_SetPar_layout.addWidget(self.extreme_value_label)
        self.extreme_value_set_parameters_button = QtWidgets.QPushButton(self.extreme_value_widget)
        self.extreme_value_set_parameters_button.setObjectName("extreme_value_set_parameters_button")
        self.ExtVal_SetPar_layout.addWidget(self.extreme_value_set_parameters_button)
        self.extreme_value_layout.addLayout(self.ExtVal_SetPar_layout)
        self.extreme_value_pic_widget = MyMatplotlibFigure(self.extreme_value_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extreme_value_pic_widget.sizePolicy().hasHeightForWidth())
        self.extreme_value_pic_widget.setSizePolicy(sizePolicy)
        self.extreme_value_pic_widget.setMinimumSize(QtCore.QSize(0, 270))
        self.extreme_value_pic_widget.setAutoFillBackground(False)
        self.extreme_value_pic_widget.setObjectName("extreme_value_pic_widget")
        self.extreme_value_layout.addWidget(self.extreme_value_pic_widget)
        self.gridLayout_4.addLayout(self.extreme_value_layout, 0, 0, 1, 1)
        self.orbit_outline_widget = QtWidgets.QWidget(self.ExtVal_OrbOut_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.orbit_outline_widget.sizePolicy().hasHeightForWidth())
        self.orbit_outline_widget.setSizePolicy(sizePolicy)
        self.orbit_outline_widget.setMinimumSize(QtCore.QSize(1, 1))
        self.orbit_outline_widget.setAutoFillBackground(False)
        self.orbit_outline_widget.setObjectName("orbit_outline_widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.orbit_outline_widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.orbit_outline_layout = QtWidgets.QVBoxLayout()
        self.orbit_outline_layout.setSpacing(2)
        self.orbit_outline_layout.setObjectName("orbit_outline_layout")
        self.OrbOut_SetPar_layout = QtWidgets.QHBoxLayout()
        self.OrbOut_SetPar_layout.setObjectName("OrbOut_SetPar_layout")
        self.orbit_outline_label = QtWidgets.QLabel(self.orbit_outline_widget)
        self.orbit_outline_label.setObjectName("orbit_outline_label")
        self.OrbOut_SetPar_layout.addWidget(self.orbit_outline_label)
        self.orbit_outline_set_parameters_button = QtWidgets.QPushButton(self.orbit_outline_widget)
        self.orbit_outline_set_parameters_button.setObjectName("orbit_outline_set_parameters_button")
        self.OrbOut_SetPar_layout.addWidget(self.orbit_outline_set_parameters_button)
        self.orbit_outline_layout.addLayout(self.OrbOut_SetPar_layout)
        self.orbit_outline_pic_widget = MyMatplotlibFigure(self.orbit_outline_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orbit_outline_pic_widget.sizePolicy().hasHeightForWidth())
        self.orbit_outline_pic_widget.setSizePolicy(sizePolicy)
        self.orbit_outline_pic_widget.setMinimumSize(QtCore.QSize(0, 270))
        self.orbit_outline_pic_widget.setObjectName("orbit_outline_pic_widget")
        self.orbit_outline_layout.addWidget(self.orbit_outline_pic_widget)
        self.gridLayout_5.addLayout(self.orbit_outline_layout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.May_preFreq_ExtVal_OrbOut_splitter, 0, 1, 1, 1)
        self.para_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.para_frame.sizePolicy().hasHeightForWidth())
        self.para_frame.setSizePolicy(sizePolicy)
        self.para_frame.setMinimumSize(QtCore.QSize(250, 800))
        self.para_frame.setAutoFillBackground(True)
        self.para_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.para_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.para_frame.setObjectName("para_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.para_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mode_layout = QtWidgets.QHBoxLayout()
        self.mode_layout.setObjectName("mode_layout")
        self.mode_label = QtWidgets.QLabel(self.para_frame)
        self.mode_label.setObjectName("mode_label")
        self.mode_layout.addWidget(self.mode_label)
        self.simple_button = QtWidgets.QRadioButton(self.para_frame)
        self.simple_button.setObjectName("simple_button")
        self.mode_button_group = QtWidgets.QButtonGroup(MainWindow)
        self.mode_button_group.setObjectName("mode_button_group")
        self.mode_button_group.addButton(self.simple_button)
        self.mode_layout.addWidget(self.simple_button)
        self.seperate_button = QtWidgets.QRadioButton(self.para_frame)
        self.seperate_button.setObjectName("seperate_button")
        self.mode_button_group.addButton(self.seperate_button)
        self.mode_layout.addWidget(self.seperate_button)
        self.gridLayout_2.addLayout(self.mode_layout, 0, 0, 1, 1)
        self.interpol_ratio_layout = QtWidgets.QHBoxLayout()
        self.interpol_ratio_layout.setObjectName("interpol_ratio_layout")
        self.interpol_ratio_label = QtWidgets.QLabel(self.para_frame)
        self.interpol_ratio_label.setObjectName("interpol_ratio_label")
        self.interpol_ratio_layout.addWidget(self.interpol_ratio_label)
        self.interpol_ratio_line = QtWidgets.QLineEdit(self.para_frame)
        self.interpol_ratio_line.setObjectName("interpol_ratio_line")
        self.interpol_ratio_layout.addWidget(self.interpol_ratio_line)
        self.gridLayout_2.addLayout(self.interpol_ratio_layout, 1, 0, 1, 1)
        self.fermi_energy_layout = QtWidgets.QHBoxLayout()
        self.fermi_energy_layout.setSpacing(11)
        self.fermi_energy_layout.setObjectName("fermi_energy_layout")
        self.fermi_energy = QtWidgets.QLabel(self.para_frame)
        self.fermi_energy.setObjectName("fermi_energy")
        self.fermi_energy_layout.addWidget(self.fermi_energy)
        self.fermi_energy_line = QtWidgets.QLineEdit(self.para_frame)
        self.fermi_energy_line.setObjectName("fermi_energy_line")
        self.fermi_energy_layout.addWidget(self.fermi_energy_line)
        self.gridLayout_2.addLayout(self.fermi_energy_layout, 2, 0, 1, 1)
        self.brilliou_zone_layout = QtWidgets.QVBoxLayout()
        self.brilliou_zone_layout.setObjectName("brilliou_zone_layout")
        self.brilliou_zone_label = QtWidgets.QLabel(self.para_frame)
        self.brilliou_zone_label.setObjectName("brilliou_zone_label")
        self.brilliou_zone_layout.addWidget(self.brilliou_zone_label)
        self.brilliou_zone_select_layout = QtWidgets.QHBoxLayout()
        self.brilliou_zone_select_layout.setObjectName("brilliou_zone_select_layout")
        self.first_bz_button = QtWidgets.QRadioButton(self.para_frame)
        self.first_bz_button.setObjectName("first_bz_button")
        self.bz_button_group = QtWidgets.QButtonGroup(MainWindow)
        self.bz_button_group.setObjectName("bz_button_group")
        self.bz_button_group.addButton(self.first_bz_button)
        self.brilliou_zone_select_layout.addWidget(self.first_bz_button)
        self.primitive_bz_button = QtWidgets.QRadioButton(self.para_frame)
        self.primitive_bz_button.setObjectName("primitive_bz_button")
        self.bz_button_group.addButton(self.primitive_bz_button)
        self.brilliou_zone_select_layout.addWidget(self.primitive_bz_button)
        self.brilliou_zone_layout.addLayout(self.brilliou_zone_select_layout)
        self.gridLayout_2.addLayout(self.brilliou_zone_layout, 3, 0, 1, 1)
        self.eps_show_slice_layout = QtWidgets.QHBoxLayout()
        self.eps_show_slice_layout.setSpacing(10)
        self.eps_show_slice_layout.setObjectName("eps_show_slice_layout")
        self.eps_layout = QtWidgets.QHBoxLayout()
        self.eps_layout.setObjectName("eps_layout")
        self.eps_label = QtWidgets.QLabel(self.para_frame)
        self.eps_label.setObjectName("eps_label")
        self.eps_layout.addWidget(self.eps_label)
        self.eps_line = QtWidgets.QLineEdit(self.para_frame)
        self.eps_line.setObjectName("eps_line")
        self.eps_layout.addWidget(self.eps_line)
        self.eps_show_slice_layout.addLayout(self.eps_layout)
        self.show_slice_checkbox = QtWidgets.QCheckBox(self.para_frame)
        self.show_slice_checkbox.setObjectName("show_slice_checkbox")
        self.eps_show_slice_layout.addWidget(self.show_slice_checkbox)
        self.gridLayout_2.addLayout(self.eps_show_slice_layout, 4, 0, 1, 1)
        self.section_v_layout = QtWidgets.QVBoxLayout()
        self.section_v_layout.setObjectName("section_v_layout")
        self.section_v_label = QtWidgets.QLabel(self.para_frame)
        self.section_v_label.setObjectName("section_v_label")
        self.section_v_layout.addWidget(self.section_v_label)
        self.section_v_line_layout = QtWidgets.QHBoxLayout()
        self.section_v_line_layout.setObjectName("section_v_line_layout")
        self.section_v_line1 = QtWidgets.QLineEdit(self.para_frame)
        self.section_v_line1.setObjectName("section_v_line1")
        self.section_v_line_layout.addWidget(self.section_v_line1)
        self.section_v_line2 = QtWidgets.QLineEdit(self.para_frame)
        self.section_v_line2.setObjectName("section_v_line2")
        self.section_v_line_layout.addWidget(self.section_v_line2)
        self.section_v_line3 = QtWidgets.QLineEdit(self.para_frame)
        self.section_v_line3.setObjectName("section_v_line3")
        self.section_v_line_layout.addWidget(self.section_v_line3)
        self.section_v_layout.addLayout(self.section_v_line_layout)
        self.gridLayout_2.addLayout(self.section_v_layout, 5, 0, 1, 1)
        self.bz_number_layout = QtWidgets.QVBoxLayout()
        self.bz_number_layout.setObjectName("bz_number_layout")
        self.bz_number_label = QtWidgets.QLabel(self.para_frame)
        self.bz_number_label.setObjectName("bz_number_label")
        self.bz_number_layout.addWidget(self.bz_number_label)
        self.bz_number_line_layout = QtWidgets.QHBoxLayout()
        self.bz_number_line_layout.setObjectName("bz_number_line_layout")
        self.bz_number_line1 = QtWidgets.QLineEdit(self.para_frame)
        self.bz_number_line1.setObjectName("bz_number_line1")
        self.bz_number_line_layout.addWidget(self.bz_number_line1)
        self.bz_number_line2 = QtWidgets.QLineEdit(self.para_frame)
        self.bz_number_line2.setObjectName("bz_number_line2")
        self.bz_number_line_layout.addWidget(self.bz_number_line2)
        self.bz_number_line3 = QtWidgets.QLineEdit(self.para_frame)
        self.bz_number_line3.setObjectName("bz_number_line3")
        self.bz_number_line_layout.addWidget(self.bz_number_line3)
        self.bz_number_layout.addLayout(self.bz_number_line_layout)
        self.gridLayout_2.addLayout(self.bz_number_layout, 6, 0, 1, 1)
        self.rotate_layout = QtWidgets.QVBoxLayout()
        self.rotate_layout.setObjectName("rotate_layout")
        self.rotate_label = QtWidgets.QLabel(self.para_frame)
        self.rotate_label.setObjectName("rotate_label")
        self.rotate_layout.addWidget(self.rotate_label)
        self.rotate_line_layout = QtWidgets.QHBoxLayout()
        self.rotate_line_layout.setObjectName("rotate_line_layout")
        self.rotate_line1 = QtWidgets.QLineEdit(self.para_frame)
        self.rotate_line1.setObjectName("rotate_line1")
        self.rotate_line_layout.addWidget(self.rotate_line1)
        self.rotate_line2 = QtWidgets.QLineEdit(self.para_frame)
        self.rotate_line2.setObjectName("rotate_line2")
        self.rotate_line_layout.addWidget(self.rotate_line2)
        self.rotate_line3 = QtWidgets.QLineEdit(self.para_frame)
        self.rotate_line3.setObjectName("rotate_line3")
        self.rotate_line_layout.addWidget(self.rotate_line3)
        self.rotate_layout.addLayout(self.rotate_line_layout)
        self.gridLayout_2.addLayout(self.rotate_layout, 7, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_checkbox = QtWidgets.QCheckBox(self.para_frame)
        self.line_checkbox.setObjectName("line_checkbox")
        self.verticalLayout.addWidget(self.line_checkbox)
        self.line_color_layout = QtWidgets.QHBoxLayout()
        self.line_color_layout.setSpacing(10)
        self.line_color_layout.setObjectName("line_color_layout")
        self.line_color_button = QtWidgets.QPushButton(self.para_frame)
        self.line_color_button.setObjectName("line_color_button")
        self.line_color_layout.addWidget(self.line_color_button)
        self.line_color_frame = QtWidgets.QFrame(self.para_frame)
        self.line_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.line_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_color_frame.setObjectName("line_color_frame")
        self.line_color_layout.addWidget(self.line_color_frame)
        self.verticalLayout.addLayout(self.line_color_layout)
        self.line_width_layout = QtWidgets.QHBoxLayout()
        self.line_width_layout.setSpacing(11)
        self.line_width_layout.setObjectName("line_width_layout")
        self.line_width_label = QtWidgets.QLabel(self.para_frame)
        self.line_width_label.setObjectName("line_width_label")
        self.line_width_layout.addWidget(self.line_width_label)
        self.line_width_line = QtWidgets.QLineEdit(self.para_frame)
        self.line_width_line.setText("")
        self.line_width_line.setObjectName("line_width_line")
        self.line_width_layout.addWidget(self.line_width_line)
        self.verticalLayout.addLayout(self.line_width_layout)
        self.gridLayout_2.addLayout(self.verticalLayout, 8, 0, 1, 1)
        self.inner_outer_layout = QtWidgets.QVBoxLayout()
        self.inner_outer_layout.setObjectName("inner_outer_layout")
        self.inner_outer_checkbox = QtWidgets.QCheckBox(self.para_frame)
        self.inner_outer_checkbox.setObjectName("inner_outer_checkbox")
        self.inner_outer_layout.addWidget(self.inner_outer_checkbox)
        self.inner_color_color_layout = QtWidgets.QHBoxLayout()
        self.inner_color_color_layout.setSpacing(14)
        self.inner_color_color_layout.setObjectName("inner_color_color_layout")
        self.inner_color_button = QtWidgets.QPushButton(self.para_frame)
        self.inner_color_button.setObjectName("inner_color_button")
        self.inner_color_color_layout.addWidget(self.inner_color_button)
        self.inner_color_frame = QtWidgets.QFrame(self.para_frame)
        self.inner_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inner_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inner_color_frame.setObjectName("inner_color_frame")
        self.inner_color_color_layout.addWidget(self.inner_color_frame)
        self.inner_outer_layout.addLayout(self.inner_color_color_layout)
        self.outer_color_layout = QtWidgets.QHBoxLayout()
        self.outer_color_layout.setSpacing(10)
        self.outer_color_layout.setObjectName("outer_color_layout")
        self.outer_color_button = QtWidgets.QPushButton(self.para_frame)
        self.outer_color_button.setObjectName("outer_color_button")
        self.outer_color_layout.addWidget(self.outer_color_button)
        self.outer_color_frame = QtWidgets.QFrame(self.para_frame)
        self.outer_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outer_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outer_color_frame.setObjectName("outer_color_frame")
        self.outer_color_layout.addWidget(self.outer_color_frame)
        self.inner_outer_layout.addLayout(self.outer_color_layout)
        self.gridLayout_2.addLayout(self.inner_outer_layout, 9, 0, 1, 1)
        self.trait_layout = QtWidgets.QHBoxLayout()
        self.trait_layout.setObjectName("trait_layout")
        self.trait_check_box = QtWidgets.QCheckBox(self.para_frame)
        self.trait_check_box.setObjectName("trait_check_box")
        self.trait_layout.addWidget(self.trait_check_box)
        self.trait_select_combobox = CheckableComboBox(self.para_frame)
        self.trait_select_combobox.setObjectName("trait_select_combobox")
        self.trait_layout.addWidget(self.trait_select_combobox)
        self.gridLayout_2.addLayout(self.trait_layout, 10, 0, 1, 1)
        self.trait_width_layout = QtWidgets.QHBoxLayout()
        self.trait_width_layout.setSpacing(11)
        self.trait_width_layout.setObjectName("trait_width_layout")
        self.trait_width_label = QtWidgets.QLabel(self.para_frame)
        self.trait_width_label.setObjectName("trait_width_label")
        self.trait_width_layout.addWidget(self.trait_width_label)
        self.trait_width_line = QtWidgets.QLineEdit(self.para_frame)
        self.trait_width_line.setObjectName("trait_width_line")
        self.trait_width_layout.addWidget(self.trait_width_line)
        self.gridLayout_2.addLayout(self.trait_width_layout, 11, 0, 1, 1)
        self.trait_color_layout = QtWidgets.QHBoxLayout()
        self.trait_color_layout.setSpacing(10)
        self.trait_color_layout.setObjectName("trait_color_layout")
        self.trait_color_button = QtWidgets.QPushButton(self.para_frame)
        self.trait_color_button.setObjectName("trait_color_button")
        self.trait_color_layout.addWidget(self.trait_color_button)
        self.trait_color_frame = QtWidgets.QFrame(self.para_frame)
        self.trait_color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trait_color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trait_color_frame.setObjectName("trait_color_frame")
        self.trait_color_layout.addWidget(self.trait_color_frame)
        self.gridLayout_2.addLayout(self.trait_color_layout, 12, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.full_trait_checkbox = QtWidgets.QCheckBox(self.para_frame)
        self.full_trait_checkbox.setObjectName("full_trait_checkbox")
        self.horizontalLayout.addWidget(self.full_trait_checkbox)
        self.axes_checkbox = QtWidgets.QCheckBox(self.para_frame)
        self.axes_checkbox.setObjectName("axes_checkbox")
        self.horizontalLayout.addWidget(self.axes_checkbox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 13, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.full_fs_full_trait_checkbox = QtWidgets.QCheckBox(self.para_frame)
        self.full_fs_full_trait_checkbox.setObjectName("full_fs_full_trait_checkbox")
        self.horizontalLayout_2.addWidget(self.full_fs_full_trait_checkbox)
        self.more_button = QtWidgets.QPushButton(self.para_frame)
        self.more_button.setObjectName("more_button")
        self.horizontalLayout_2.addWidget(self.more_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 14, 0, 1, 1)
        self.update_button = QtWidgets.QPushButton(self.para_frame)
        self.update_button.setObjectName("update_button")
        self.gridLayout_2.addWidget(self.update_button, 15, 0, 1, 1)
        self.gridLayout.addWidget(self.para_frame, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1415, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport_skeaf_file = QtWidgets.QMenu(self.menuFile)
        self.menuImport_skeaf_file.setObjectName("menuImport_skeaf_file")
        self.menuCalc = QtWidgets.QMenu(self.menubar)
        self.menuCalc.setObjectName("menuCalc")
        self.menuNormal_calculation = QtWidgets.QMenu(self.menuCalc)
        self.menuNormal_calculation.setObjectName("menuNormal_calculation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_bxsf_file = QtWidgets.QAction(MainWindow)
        self.actionImport_bxsf_file.setObjectName("actionImport_bxsf_file")
        self.actionExport_figure_data = QtWidgets.QAction(MainWindow)
        self.actionExport_figure_data.setObjectName("actionExport_figure_data")
        self.actionSave_figure = QtWidgets.QAction(MainWindow)
        self.actionSave_figure.setObjectName("actionSave_figure")
        self.actionImport_results_long_out = QtWidgets.QAction(MainWindow)
        self.actionImport_results_long_out.setObjectName("actionImport_results_long_out")
        self.actionImport_results_orbitoutlines_invAng_out = QtWidgets.QAction(MainWindow)
        self.actionImport_results_orbitoutlines_invAng_out.setObjectName("actionImport_results_orbitoutlines_invAng_out")
        self.actionImport_results_orbitoutlines_invau_out = QtWidgets.QAction(MainWindow)
        self.actionImport_results_orbitoutlines_invau_out.setObjectName("actionImport_results_orbitoutlines_invau_out")
        self.actionImport_all_results_file = QtWidgets.QAction(MainWindow)
        self.actionImport_all_results_file.setObjectName("actionImport_all_results_file")
        self.actionImport_config_in = QtWidgets.QAction(MainWindow)
        self.actionImport_config_in.setObjectName("actionImport_config_in")
        self.actionSettng_parameters = QtWidgets.QAction(MainWindow)
        self.actionSettng_parameters.setObjectName("actionSettng_parameters")
        self.actionRotating_angle_calculation = QtWidgets.QAction(MainWindow)
        self.actionRotating_angle_calculation.setObjectName("actionRotating_angle_calculation")
        self.menuImport_skeaf_file.addAction(self.actionImport_results_long_out)
        self.menuImport_skeaf_file.addAction(self.actionImport_results_orbitoutlines_invAng_out)
        self.menuImport_skeaf_file.addAction(self.actionImport_results_orbitoutlines_invau_out)
        self.menuImport_skeaf_file.addAction(self.actionImport_all_results_file)
        self.menuFile.addAction(self.actionImport_bxsf_file)
        self.menuFile.addAction(self.menuImport_skeaf_file.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_figure_data)
        self.menuFile.addAction(self.actionSave_figure)
        self.menuNormal_calculation.addAction(self.actionImport_config_in)
        self.menuNormal_calculation.addAction(self.actionSettng_parameters)
        self.menuCalc.addAction(self.menuNormal_calculation.menuAction())
        self.menuCalc.addAction(self.actionRotating_angle_calculation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCalc.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Skeaf_demo"))
        self.extreme_value_label.setText(_translate("MainWindow", "Extreme value"))
        self.extreme_value_set_parameters_button.setText(_translate("MainWindow", "Save Data"))
        self.orbit_outline_label.setText(_translate("MainWindow", "Orbit outline"))
        self.orbit_outline_set_parameters_button.setText(_translate("MainWindow", "Save Data"))
        self.mode_label.setText(_translate("MainWindow", "Mode"))
        self.simple_button.setText(_translate("MainWindow", "SImple"))
        self.seperate_button.setText(_translate("MainWindow", "Seperate"))
        self.interpol_ratio_label.setText(_translate("MainWindow", "Interpol  ratio"))
        self.fermi_energy.setText(_translate("MainWindow", "fermi energy"))
        self.brilliou_zone_label.setText(_translate("MainWindow", "Brilliou zone"))
        self.first_bz_button.setText(_translate("MainWindow", "First BZ"))
        self.primitive_bz_button.setText(_translate("MainWindow", "Primitive BZ"))
        self.eps_label.setText(_translate("MainWindow", "eps"))
        self.show_slice_checkbox.setText(_translate("MainWindow", "Show slice"))
        self.section_v_label.setText(_translate("MainWindow", "Section-v"))
        self.bz_number_label.setText(_translate("MainWindow", "BZ number"))
        self.rotate_label.setText(_translate("MainWindow", "Rotate"))
        self.line_checkbox.setText(_translate("MainWindow", "Line"))
        self.line_color_button.setText(_translate("MainWindow", "Line color"))
        self.line_width_label.setText(_translate("MainWindow", "Line width"))
        self.inner_outer_checkbox.setText(_translate("MainWindow", "Inner-outer"))
        self.inner_color_button.setText(_translate("MainWindow", "Inner color"))
        self.outer_color_button.setText(_translate("MainWindow", "Outer color"))
        self.trait_check_box.setText(_translate("MainWindow", "Trait"))
        self.trait_width_label.setText(_translate("MainWindow", "Trait width"))
        self.trait_color_button.setText(_translate("MainWindow", "Trait color"))
        self.full_trait_checkbox.setText(_translate("MainWindow", "Full trait"))
        self.axes_checkbox.setText(_translate("MainWindow", "Axes"))
        self.full_fs_full_trait_checkbox.setText(_translate("MainWindow", "Full fs full trait"))
        self.more_button.setText(_translate("MainWindow", "..."))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImport_skeaf_file.setTitle(_translate("MainWindow", "Import skeaf file"))
        self.menuCalc.setTitle(_translate("MainWindow", "Calc"))
        self.menuNormal_calculation.setTitle(_translate("MainWindow", "Normal calculation"))
        self.actionImport_bxsf_file.setText(_translate("MainWindow", "Import bxsf file"))
        self.actionExport_figure_data.setText(_translate("MainWindow", "Export figure data"))
        self.actionSave_figure.setText(_translate("MainWindow", "Save figure"))
        self.actionImport_results_long_out.setText(_translate("MainWindow", "Import results_long.out"))
        self.actionImport_results_orbitoutlines_invAng_out.setText(_translate("MainWindow", "Import results_orbitoutlines_invAng.out"))
        self.actionImport_results_orbitoutlines_invau_out.setText(_translate("MainWindow", "Import results_orbitoutlines_invau.out"))
        self.actionImport_all_results_file.setText(_translate("MainWindow", "Import all results file"))
        self.actionImport_config_in.setText(_translate("MainWindow", "Import config.in"))
        self.actionSettng_parameters.setText(_translate("MainWindow", "Settng parameters"))
        self.actionRotating_angle_calculation.setText(_translate("MainWindow", "Rotating angle calculation"))
from comboCheckbox import CheckableComboBox
from matplot_show import MyMatplotlibFigure
from mayavi_show import MayaviQWidget