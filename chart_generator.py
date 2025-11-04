import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox,
    QPushButton, QLabel, QLineEdit, QTextEdit, QTabWidget, QFormLayout,
    QSpinBox, QDoubleSpinBox, QCheckBox, QFileDialog, QMessageBox, QScrollArea,
    QGroupBox, QRadioButton, QButtonGroup, QFrame, QSpacerItem, QSizePolicy,
    QGridLayout, QProgressBar, QSlider, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractItemView, QInputDialog, QDialog, QDialogButtonBox,
    QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt, QTranslator, QLocale, QLibraryInfo, pyqtSignal, QThread, QItemSelectionModel
from PyQt6.QtGui import QIcon, QPalette, QColor, QLinearGradient, QBrush, QPixmap, QFont, QImage
import matplotlib
matplotlib.use('QtAgg')
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple, Optional
import json
import tempfile
import base64
from io import BytesIO

# ====================== Translation System ======================
class Translator:
    def __init__(self):
        self.translators = {}
        self.current_lang = "en"
        self.load_translations()

    def load_translations(self):
        translations = {
            "en": {
                "app_title": "Advanced Dynamic Chart Generator",
                "select_language": "Select Language:",
                "theme": "Theme:",
                "chart_type": "Chart Type:",
                "bar_chart": "Bar Chart",
                "line_chart": "Line Chart",
                "pie_chart": "Pie Chart",
                "scatter_chart": "Scatter Plot",
                "area_chart": "Area Chart",
                "histogram": "Histogram",
                "box_plot": "Box Plot",
                "heatmap": "Heatmap",
                "radar_chart": "Radar Chart",
                "polar_chart": "Polar Chart",
                "title": "Title:",
                "xlabel": "X Label:",
                "ylabel": "Y Label:",
                "data_table": "Data Table (Dynamic):",
                "add_row": "Add Row",
                "remove_row": "Remove Row",
                "add_column": "Add Column",
                "remove_column": "Remove Column",
                "column_name": "Column Name",
                "enter_column_name": "Enter new column name:",
                "grid": "Show Grid",
                "legend": "Show Legend",
                "3d": "3D View",
                "generate": "Generate Chart",
                "save_image": "Save as Image",
                "export_data": "Export Data",
                "import_data": "Import CSV",
                "settings": "Settings",
                "advanced": "Advanced Options",
                "colors": "Color Scheme:",
                "font_size": "Font Size:",
                "line_width": "Line Width:",
                "marker_size": "Marker Size:",
                "opacity": "Opacity:",
                "rotation": "Label Rotation:",
                "language_changed": "Language changed. Restart required for full effect.",
                "chart_generated": "Chart generated successfully!",
                "error": "Error",
                "invalid_data": "Invalid data format. Please check inputs.",
                "file_saved": "Image saved successfully!",
                "file_exported": "Data exported successfully!",
                "windows_default": "Windows Default",
                "light": "Light",
                "dark": "Dark",
                "red": "Red Theme",
                "blue": "Blue Theme",
                "direction": "ltr",
                "x_column": "X Column:",
                "y_column": "Y Column:",
                "categories_column": "Categories Column:",
                "values_column": "Values Column:",
                "multi_series": "Multiple Series",
                "select_series": "Select Series Columns:",
                "heatmap_x": "Heatmap X Column:",
                "heatmap_y": "Heatmap Y Column:",
                "heatmap_z": "Heatmap Z Column:",
                "box_datasets": "Box Plot Datasets:",
                "radar_categories": "Radar Categories Column:",
                "radar_values": "Radar Values Columns:",
                "data_tab": "Data",
                "settings_tab": "Chart Settings",
                "display": "Display",
                "general": "General",
                "table_type": "Table Type:",
                "empty_table": "Empty Table",
                "sample_sales": "Sample: Sales Data",
                "sample_weather": "Sample: Weather Data",
                "sample_students": "Sample: Student Grades",
                "sample_survey": "Sample: Survey Results"
            },
            "fa": {
                "app_title": "تولیدکننده پیشرفته نمودار پویا",
                "select_language": "انتخاب زبان:",
                "theme": "تم:",
                "chart_type": "نوع نمودار:",
                "bar_chart": "نمودار میله‌ای",
                "line_chart": "نمودار خطی",
                "pie_chart": "نمودار دایره‌ای",
                "scatter_chart": "نمودار پراکندگی",
                "area_chart": "نمودار ناحیه‌ای",
                "histogram": "هیستوگرام",
                "box_plot": "نمودار جعبه‌ای",
                "heatmap": "نقشه حرارتی",
                "radar_chart": "نمودار راداری",
                "polar_chart": "نمودار قطبی",
                "title": "عنوان:",
                "xlabel": "برچسب محور X:",
                "ylabel": "برچسب محور Y:",
                "data_table": "جدول داده (پویا):",
                "add_row": "افزودن ردیف",
                "remove_row": "حذف ردیف",
                "add_column": "افزودن ستون",
                "remove_column": "حذف ستون",
                "column_name": "نام ستون",
                "enter_column_name": "نام ستون جدید را وارد کنید:",
                "grid": "نمایش شبکه",
                "legend": "نمایش راهنما",
                "3d": "نمای سه‌بعدی",
                "generate": "تولید نمودار",
                "save_image": "ذخیره به عنوان تصویر",
                "export_data": "خروجی داده",
                "import_data": "وارد کردن CSV",
                "settings": "تنظیمات",
                "advanced": "گزینه‌های پیشرفته",
                "colors": "طرح رنگی:",
                "font_size": "اندازه فونت:",
                "line_width": "ضخامت خط:",
                "marker_size": "اندازه نشانگر:",
                "opacity": "شفافیت:",
                "rotation": "چرخش برچسب:",
                "language_changed": "زبان تغییر کرد. برای اعمال کامل نیاز به راه‌اندازی مجدد است.",
                "chart_generated": "نمودار با موفقیت تولید شد!",
                "error": "خطا",
                "invalid_data": "فرمت داده نامعتبر است. لطفاً ورودی‌ها را بررسی کنید.",
                "file_saved": "تصویر با موفقیت ذخیره شد!",
                "file_exported": "داده با موفقیت خروجی شد!",
                "windows_default": "پیش‌فرض ویندوز",
                "light": "روشن",
                "dark": "تیره",
                "red": "تم قرمز",
                "blue": "تم آبی",
                "direction": "rtl",
                "x_column": "ستون X:",
                "y_column": "ستون Y:",
                "categories_column": "ستون دسته‌بندی:",
                "values_column": "ستون مقادیر:",
                "multi_series": "سری‌های چندگانه",
                "select_series": "انتخاب ستون‌های سری:",
                "heatmap_x": "ستون X نقشه حرارتی:",
                "heatmap_y": "ستون Y نقشه حرارتی:",
                "heatmap_z": "ستون Z نقشه حرارتی:",
                "box_datasets": "مجموعه داده‌های جعبه‌ای:",
                "radar_categories": "ستون دسته‌بندی رادار:",
                "radar_values": "ستون‌های مقادیر رادار:",
                "data_tab": "داده",
                "settings_tab": "تنظیمات نمودار",
                "display": "نمایش",
                "general": "عمومی",
                "table_type": "نوع جدول:",
                "empty_table": "جدول خالی",
                "sample_sales": "نمونه: داده‌های فروش",
                "sample_weather": "نمونه: داده‌های آب‌وهوا",
                "sample_students": "نمونه: نمرات دانش‌آموزان",
                "sample_survey": "نمونه: نتایج نظرسنجی"
            },
            "zh": {
                "app_title": "高级动态图表生成器",
                "select_language": "选择语言:",
                "theme": "主题:",
                "chart_type": "图表类型:",
                "bar_chart": "柱状图",
                "line_chart": "折线图",
                "pie_chart": "饼图",
                "scatter_chart": "散点图",
                "area_chart": "面积图",
                "histogram": "直方图",
                "box_plot": "箱线图",
                "heatmap": "热力图",
                "radar_chart": "雷达图",
                "polar_chart": "极坐标图",
                "title": "标题:",
                "xlabel": "X轴标签:",
                "ylabel": "Y轴标签:",
                "data_table": "数据表 (动态):",
                "add_row": "添加行",
                "remove_row": "删除行",
                "add_column": "添加列",
                "remove_column": "删除列",
                "column_name": "列名",
                "enter_column_name": "输入新列名:",
                "grid": "显示网格",
                "legend": "显示图例",
                "3d": "三维视图",
                "generate": "生成图表",
                "save_image": "另存为图片",
                "export_data": "导出数据",
                "import_data": "导入CSV",
                "settings": "设置",
                "advanced": "高级选项",
                "colors": "配色方案:",
                "font_size": "字体大小:",
                "line_width": "线宽:",
                "marker_size": "标记大小:",
                "opacity": "透明度:",
                "rotation": "标签旋转:",
                "language_changed": "语言已更改。需重启以完全生效。",
                "chart_generated": "图表生成成功！",
                "error": "错误",
                "invalid_data": "数据格式无效。请检查输入。",
                "file_saved": "图片保存成功！",
                "file_exported": "数据导出成功！",
                "windows_default": "Windows 默认",
                "light": "亮色",
                "dark": "暗色",
                "red": "红色主题",
                "blue": "蓝色主题",
                "direction": "ltr",
                "x_column": "X列:",
                "y_column": "Y列:",
                "categories_column": "类别列:",
                "values_column": "值列:",
                "multi_series": "多系列",
                "select_series": "选择系列列:",
                "heatmap_x": "热图X列:",
                "heatmap_y": "热图Y列:",
                "heatmap_z": "热图Z列:",
                "box_datasets": "箱线图数据集:",
                "radar_categories": "雷达类别列:",
                "radar_values": "雷达值列:",
                "data_tab": "数据",
                "settings_tab": "图表设置",
                "display": "显示",
                "general": "常规",
                "table_type": "表格类型:",
                "empty_table": "空表格",
                "sample_sales": "示例：销售数据",
                "sample_weather": "示例：天气数据",
                "sample_students": "示例：学生成绩",
                "sample_survey": "示例：调查结果"
            },
            "ru": {
                "app_title": "Продвинутый Генератор Динамических Диаграмм",
                "select_language": "Выбрать язык:",
                "theme": "Тема:",
                "chart_type": "Тип диаграммы:",
                "bar_chart": "Столбчатая диаграмма",
                "line_chart": "Линейный график",
                "pie_chart": "Круговая диаграмма",
                "scatter_chart": "Точечная диаграмма",
                "area_chart": "Площадная диаграмма",
                "histogram": "Гистограмма",
                "box_plot": "Ящик с усами",
                "heatmap": "Тепловая карта",
                "radar_chart": "Радарная диаграмма",
                "polar_chart": "Полярная диаграмма",
                "title": "Заголовок:",
                "xlabel": "Подпись оси X:",
                "ylabel": "Подпись оси Y:",
                "data_table": "Таблица данных (динамическая):",
                "add_row": "Добавить строку",
                "remove_row": "Удалить строку",
                "add_column": "Добавить столбец",
                "remove_column": "Удалить столбец",
                "column_name": "Имя столбца",
                "enter_column_name": "Введите имя нового столбца:",
                "grid": "Показать сетку",
                "legend": "Показать легенду",
                "3d": "3D вид",
                "generate": "Создать диаграмму",
                "save_image": "Сохранить как изображение",
                "export_data": "Экспорт данных",
                "import_data": "Импорт CSV",
                "settings": "Настройки",
                "advanced": "Расширенные опции",
                "colors": "Цветовая схема:",
                "font_size": "Размер шрифта:",
                "line_width": "Толщина линии:",
                "marker_size": "Размер маркера:",
                "opacity": "Прозрачность:",
                "rotation": "Поворот меток:",
                "language_changed": "Язык изменён. Перезапуск для полного эффекта.",
                "chart_generated": "Диаграмма успешно создана!",
                "error": "Ошибка",
                "invalid_data": "Неверный формат данных. Проверьте ввод.",
                "file_saved": "Изображение сохранено!",
                "file_exported": "Данные экспортированы!",
                "windows_default": "По умолчанию Windows",
                "light": "Светлая",
                "dark": "Тёмная",
                "red": "Красная",
                "blue": "Синяя",
                "direction": "ltr",
                "x_column": "Столбец X:",
                "y_column": "Столбец Y:",
                "categories_column": "Столбец категорий:",
                "values_column": "Столбец значений:",
                "multi_series": "Множественные серии",
                "select_series": "Выбрать столбцы серий:",
                "heatmap_x": "Столбец X тепловой карты:",
                "heatmap_y": "Столбец Y тепловой карты:",
                "heatmap_z": "Столбец Z тепловой карты:",
                "box_datasets": "Наборы данных для ящика с усами:",
                "radar_categories": "Столбец категорий радара:",
                "radar_values": "Столбцы значений радара:",
                "data_tab": "Данные",
                "settings_tab": "Настройки диаграммы",
                "display": "Отображение",
                "general": "Общие",
                "table_type": "Тип таблицы:",
                "empty_table": "Пустая таблица",
                "sample_sales": "Пример: Данные продаж",
                "sample_weather": "Пример: Погодные данные",
                "sample_students": "Пример: Оценки студентов",
                "sample_survey": "Пример: Результаты опроса"
            }
        }
        self.translators = translations

    def tr(self, key: str) -> str:
        return self.translators.get(self.current_lang, self.translators["en"]).get(key, key)

    def set_language(self, lang: str):
        self.current_lang = lang

    def direction(self) -> str:
        return self.translators.get(self.current_lang, self.translators["en"]).get("direction", "ltr")

# ====================== Theme Engine ======================
class ThemeEngine:
    @staticmethod
    def apply_theme(app: QApplication, theme_name: str):
        palette = QPalette()
        if theme_name == "dark":
            app.setStyleSheet("""
                QMainWindow, QWidget { background-color: #1e1e1e; color: #e0e0e0; font-family: Segoe UI; }
                QLabel { color: #e0e0e0; font-weight: 500; }
                QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QTableWidget, QListWidget { 
                    background-color: #2d2d2d; color: #ffffff; border: 1px solid #444444; border-radius: 6px; padding: 6px;
                    selection-background-color: #007acc;
                }
                QTableWidget::item { padding: 5px; }
                QPushButton { 
                    background-color: #007acc; color: white; border: none; padding: 10px 18px; border-radius: 6px; 
                    font-weight: bold; min-height: 20px;
                }
                QPushButton:hover { background-color: #005a99; }
                QPushButton:pressed { background-color: #003f70; }
                QTabWidget::pane { border: 1px solid #444444; background-color: #1e1e1e; border-radius: 8px; }
                QTabBar::tab { background-color: #2d2d2d; color: #cccccc; padding: 10px 16px; border-top-left-radius: 6px; border-top-right-radius: 6px; margin-right: 2px; }
                QTabBar::tab:selected { background-color: #007acc; color: white; }
                QGroupBox { color: #cccccc; border: 1px solid #444444; border-radius: 8px; margin-top: 12px; padding-top: 10px; }
                QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 8px; background-color: #1e1e1e; }
                QHeaderView::section { background-color: #2d2d2d; color: #e0e0e0; padding: 8px; border: 1px solid #444; }
                QScrollBar:vertical { background: #2d2d2d; width: 12px; margin: 0; }
                QScrollBar::handle:vertical { background: #555; border-radius: 6px; min-height: 20px; }
            """)
            palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.Base, QColor(45, 45, 45))
            palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 122, 204))
        elif theme_name == "light":
            app.setStyleSheet("""
                QMainWindow, QWidget { background-color: #f8f9fa; color: #212529; font-family: Segoe UI; }
                QLabel { color: #212529; font-weight: 500; }
                QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox, QTableWidget, QListWidget { 
                    background-color: white; color: #212529; border: 1px solid #ced4da; border-radius: 6px; padding: 6px;
                }
                QPushButton { 
                    background-color: #007bff; color: white; border: none; padding: 10px 18px; border-radius: 6px; 
                    font-weight: bold;
                }
                QPushButton:hover { background-color: #0056b3; }
            """)
            palette.setColor(QPalette.ColorRole.Window, QColor(248, 249, 250))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(33, 37, 41))
            palette.setColor(QPalette.ColorRole.Base, QColor(255, 255, 255))
            palette.setColor(QPalette.ColorRole.Text, QColor(33, 37, 41))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 123, 255))
        elif theme_name == "red":
            app.setStyleSheet("""
                QMainWindow, QWidget { background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #440000, stop:1 #880000); color: #ffffff; }
                QLabel { color: #ffcccc; font-weight: bold; }
                QLineEdit, QTextEdit, QComboBox, QTableWidget, QListWidget { background-color: #550000; color: #ffcccc; border: 1px solid #880000; border-radius: 6px; }
                QPushButton { background-color: #cc0000; color: white; border-radius: 6px; padding: 10px; font-weight: bold; }
                QPushButton:hover { background-color: #ff1111; }
                QTabBar::tab { background-color: #660000; color: #ffcccc; }
                QTabBar::tab:selected { background-color: #cc0000; }
            """)
        elif theme_name == "blue":
            app.setStyleSheet("""
                QMainWindow, QWidget { background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #001133, stop:1 #003366); color: #ffffff; }
                QLabel { color: #ccddff; font-weight: bold; }
                QLineEdit, QTextEdit, QComboBox, QTableWidget, QListWidget { background-color: #002244; color: #ccddff; border: 1px solid #004488; border-radius: 6px; }
                QPushButton { background-color: #007acc; color: white; border-radius: 6px; padding: 10px; font-weight: bold; }
                QPushButton:hover { background-color: #0099ff; }
                QTabBar::tab { background-color: #002244; color: #ccddff; }
                QTabBar::tab:selected { background-color: #007acc; }
            """)
        else:
            app.setStyleSheet("")
            app.setPalette(app.style().standardPalette())
        app.setPalette(palette)

# ====================== Dynamic Table Widget ======================
class DynamicTable(QWidget):
    data_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.translator = parent.translator if parent else Translator()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Buttons
        btn_layout = QHBoxLayout()
        self.add_row_btn = QPushButton(self.tr("add_row"))
        self.remove_row_btn = QPushButton(self.tr("remove_row"))
        self.add_col_btn = QPushButton(self.tr("add_column"))
        self.remove_col_btn = QPushButton(self.tr("remove_column"))

        for btn in [self.add_row_btn, self.remove_row_btn, self.add_col_btn, self.remove_col_btn]:
            btn.setMinimumHeight(36)
            btn_layout.addWidget(btn)

        layout.addLayout(btn_layout)

        # Table
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Category", "Value1", "Value2"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.itemChanged.connect(self.on_item_changed)
        layout.addWidget(self.table)

        # Connections
        self.add_row_btn.clicked.connect(self.add_row)
        self.remove_row_btn.clicked.connect(self.remove_row)
        self.add_col_btn.clicked.connect(self.add_column)
        self.remove_col_btn.clicked.connect(self.remove_column)

    def tr(self, key):
        return self.translator.tr(key)

    def add_row(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.data_changed.emit()

    def remove_row(self):
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            self.table.removeRow(row)
            self.data_changed.emit()

    def add_column(self):
        name, ok = QInputDialog.getText(self, self.tr("column_name"), self.tr("enter_column_name"))
        if ok and name:
            col = self.table.columnCount()
            self.table.insertColumn(col)
            self.table.setHorizontalHeaderItem(col, QTableWidgetItem(name))
            self.data_changed.emit()

    def remove_column(self):
        col = self.table.currentColumn()
        if col >= 0:
            self.table.removeColumn(col)
            self.data_changed.emit()

    def get_data(self) -> pd.DataFrame:
        rows = self.table.rowCount()
        cols = self.table.columnCount()
        data = []
        headers = [self.table.horizontalHeaderItem(i).text() if self.table.horizontalHeaderItem(i) else f"Col{i}" for i in range(cols)]
        for r in range(rows):
            row = []
            for c in range(cols):
                item = self.table.item(r, c)
                row.append(item.text() if item else "")
            data.append(row)
        return pd.DataFrame(data, columns=headers)

    def set_data(self, df: pd.DataFrame):
        self.table.blockSignals(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        if df.empty:
            self.table.setRowCount(5)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(["X", "Y"])
        else:
            self.table.setRowCount(df.shape[0])
            self.table.setColumnCount(df.shape[1])
            self.table.setHorizontalHeaderLabels(df.columns.tolist())
            for r in range(df.shape[0]):
                for c in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iat[r, c]))
                    self.table.setItem(r, c, item)
        self.table.blockSignals(False)
        self.data_changed.emit()

    def on_item_changed(self, item):
        self.data_changed.emit()

# ====================== Chart Generator Worker ======================
class ChartWorker(QThread):
    finished = pyqtSignal(Figure)
    error = pyqtSignal(str)

    def __init__(self, chart_type: str, df: pd.DataFrame, params: Dict[str, Any]):
        super().__init__()
        self.chart_type = chart_type
        self.df = df
        self.params = params

    def run(self):
        try:
            if self.df.empty:
                raise ValueError("DataFrame is empty")

            fig = Figure(figsize=(14, 9), dpi=120)
            ax = fig.add_subplot(111, projection='3d' if self.params.get('3d', False) and self.chart_type in ['bar', 'line'] else None)

            title = self.params.get('title', 'Chart')
            xlabel = self.params.get('xlabel', 'X')
            ylabel = self.params.get('ylabel', 'Y')
            grid = self.params.get('grid', True)
            legend = self.params.get('legend', True)
            font_size = self.params.get('font_size', 12)
            colors = self.params.get('colors', 'tab10')
            rotation = self.params.get('rotation', 0)

            plt.rcParams.update({'font.size': font_size})

            cmap = plt.get_cmap(colors)

            if self.chart_type == "bar_chart":
                cats_col = self.params.get('categories_column')
                vals_col = self.params.get('values_column')
                if not cats_col or not vals_col:
                    raise ValueError("Select categories and values columns")
                cats = self.df[cats_col].astype(str)
                vals = pd.to_numeric(self.df[vals_col], errors='coerce').fillna(0)
                bars = ax.bar(cats, vals, color=cmap(np.linspace(0, 1, len(vals))))
                if rotation:
                    ax.set_xticklabels(cats, rotation=rotation)
                if not self.params.get('3d', False):
                    for bar in bars:
                        h = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2., h + vals.max()*0.01, f'{h:.1f}', ha='center', va='bottom', fontsize=font_size-2)

            elif self.chart_type == "line_chart":
                x_col = self.params.get('x_column')
                y_cols = self.params.get('y_columns', [])
                if not x_col or not y_cols:
                    raise ValueError("Select X and Y columns")
                x = pd.to_numeric(self.df[x_col], errors='coerce').fillna(0)
                for i, y_col in enumerate(y_cols):
                    y = pd.to_numeric(self.df[y_col], errors='coerce').fillna(0)
                    ax.plot(x, y, marker='o', linewidth=self.params.get('line_width', 2), 
                            markersize=self.params.get('marker_size', 6), label=y_col, color=cmap(i/len(y_cols)))
                if legend:
                    ax.legend()

            elif self.chart_type == "pie_chart":
                labels_col = self.params.get('categories_column')
                values_col = self.params.get('values_column')
                if not labels_col or not values_col:
                    raise ValueError("Select labels and values")
                labels = self.df[labels_col].astype(str)
                sizes = pd.to_numeric(self.df[values_col], errors='coerce').fillna(0)
                ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=cmap(np.linspace(0, 1, len(sizes))))

            elif self.chart_type == "scatter_chart":
                x_col = self.params.get('x_column')
                y_cols = self.params.get('y_columns', [])
                if not x_col or not y_cols:
                    raise ValueError("Select X and Y columns")
                x = pd.to_numeric(self.df[x_col], errors='coerce').fillna(0)
                for i, y_col in enumerate(y_cols):
                    y = pd.to_numeric(self.df[y_col], errors='coerce').fillna(0)
                    ax.scatter(x, y, s=(self.params.get('marker_size', 6)**2), alpha=self.params.get('opacity', 0.8), 
                               label=y_col, color=cmap(i/len(y_cols)))
                if legend:
                    ax.legend()

            elif self.chart_type == "area_chart":
                x_col = self.params.get('x_column')
                y_cols = self.params.get('y_columns', [])
                if not x_col or not y_cols:
                    raise ValueError("Select X and Y columns")
                x = pd.to_numeric(self.df[x_col], errors='coerce').fillna(0)
                bottom = np.zeros(len(x))
                for i, y_col in enumerate(y_cols):
                    y = pd.to_numeric(self.df[y_col], errors='coerce').fillna(0)
                    ax.fill_between(x, bottom, bottom + y, alpha=0.5, label=y_col, color=cmap(i/len(y_cols)))
                    bottom += y
                if legend:
                    ax.legend()

            elif self.chart_type == "histogram":
                cols = self.params.get('y_columns', [])
                if not cols:
                    raise ValueError("Select columns for histogram")
                for i, col in enumerate(cols):
                    data = pd.to_numeric(self.df[col], errors='coerce').dropna()
                    ax.hist(data, bins=self.params.get('bins', 10), alpha=0.7, label=col, color=cmap(i/len(cols)))
                if legend:
                    ax.legend()

            elif self.chart_type == "box_plot":
                cols = self.params.get('box_columns', [])
                if not cols:
                    raise ValueError("Select dataset columns")
                data = [pd.to_numeric(self.df[c], errors='coerce').dropna() for c in cols]
                ax.boxplot(data, labels=cols)

            elif self.chart_type == "heatmap":
                x_col = self.params.get('heatmap_x')
                y_col = self.params.get('heatmap_y')
                z_col = self.params.get('heatmap_z')
                if not all([x_col, y_col, z_col]):
                    raise ValueError("Select X, Y, Z columns")
                pivot = self.df.pivot_table(index=y_col, columns=x_col, values=z_col, aggfunc='mean')
                im = ax.imshow(pivot.values, cmap=colors, aspect='auto')
                ax.set_xticks(np.arange(len(pivot.columns)))
                ax.set_yticks(np.arange(len(pivot.index)))
                ax.set_xticklabels(pivot.columns)
                ax.set_yticklabels(pivot.index)
                plt.setp(ax.get_xticklabels(), rotation=rotation)
                fig.colorbar(im)

            elif self.chart_type == "radar_chart":
                cat_col = self.params.get('radar_categories')
                val_cols = self.params.get('radar_values', [])
                if not cat_col or not val_cols:
                    raise ValueError("Select categories and values")
                categories = self.df[cat_col].unique()
                angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
                angles += angles[:1]
                ax = fig.add_subplot(111, polar=True)
                for i, col in enumerate(val_cols):
                    values = self.df.pivot_table(index=cat_col, values=col, aggfunc='mean').reindex(categories).values.flatten()
                    values = np.concatenate((values, [values[0]]))
                    ax.plot(angles, values, 'o-', linewidth=2, label=col, color=cmap(i/len(val_cols)))
                    ax.fill(angles, values, alpha=0.25, color=cmap(i/len(val_cols)))
                ax.set_thetagrids(np.degrees(angles[:-1]), categories)
                if legend:
                    ax.legend()

            elif self.chart_type == "polar_chart":
                theta_col = self.params.get('x_column')
                r_col = self.params.get('y_columns', [None])[0]
                if not theta_col or not r_col:
                    raise ValueError("Select theta and r columns")
                theta = pd.to_numeric(self.df[theta_col], errors='coerce').fillna(0) * np.pi / 180
                r = pd.to_numeric(self.df[r_col], errors='coerce').fillna(0)
                ax = fig.add_subplot(111, polar=True)
                ax.plot(theta, r, color=cmap(0.3))

            ax.set_title(title, pad=20, fontsize=font_size + 4, fontweight='bold')
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if grid and not isinstance(ax, plt.PolarAxes):
                ax.grid(True)

            fig.tight_layout(pad=3.0)
            self.finished.emit(fig)
        except Exception as e:
            self.error.emit(str(e))

# ====================== Sample Data Templates ======================
SAMPLE_DATA = {
    "empty_table": pd.DataFrame(),
    "sample_sales": pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales": [1200, 1500, 1800, 1700, 2000, 2200],
        "Profit": [300, 400, 500, 450, 600, 700]
    }),
    "sample_weather": pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Temp": [22, 24, 21, 25, 27, 28, 26],
        "Humidity": [60, 65, 70, 55, 50, 48, 52]
    }),
    "sample_students": pd.DataFrame({
        "Student": ["Ali", "Sara", "Reza", "Maryam", "Hossein"],
        "Math": [85, 92, 78, 96, 88],
        "Science": [90, 88, 82, 94, 86]
    }),
    "sample_survey": pd.DataFrame({
        "Age Group": ["18-25", "26-35", "36-45", "46+"],
        "Satisfied": [45, 60, 55, 40],
        "Neutral": [30, 25, 30, 35],
        "Dissatisfied": [25, 15, 15, 25]
    })
}

# ====================== Main Application ======================
class ChartGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.translator = Translator()
        self.current_theme = "windows_default"
        self.chart_worker = None
        self.last_figure = None
        self.init_ui()
        self.apply_language()
        self.apply_theme()

    def tr(self, key):
        return self.translator.tr(key)

    def init_ui(self):
        self.setWindowTitle(self.tr("app_title"))
        self.setGeometry(100, 100, 1600, 1000)
        self.setMinimumSize(1200, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(25)

        # Left Panel
        left_panel = QScrollArea()
        left_panel.setWidgetResizable(True)
        left_panel.setMaximumWidth(550)
        left_content = QWidget()
        left_layout = QVBoxLayout(left_content)
        left_layout.setSpacing(15)

        # Top Bar
        top_bar = QHBoxLayout()
        lang_combo = QComboBox()
        lang_combo.addItems(["English", "فارسی", "中文", "Русский"])
        lang_combo.currentIndexChanged.connect(self.change_language)
        top_bar.addWidget(QLabel(self.tr("select_language")))
        top_bar.addWidget(lang_combo)

        theme_combo = QComboBox()
        theme_combo.addItems([self.tr("windows_default"), self.tr("light"), self.tr("dark"), self.tr("red"), self.tr("blue")])
        theme_combo.currentIndexChanged.connect(self.change_theme)
        top_bar.addWidget(QLabel(self.tr("theme")))
        top_bar.addWidget(theme_combo)
        top_bar.addStretch()
        left_layout.addLayout(top_bar)

        # Table Type Selector
        table_type_layout = QHBoxLayout()
        self.table_type_combo = QComboBox()
        self.table_type_combo.addItems([
            self.tr("empty_table"),
            self.tr("sample_sales"),
            self.tr("sample_weather"),
            self.tr("sample_students"),
            self.tr("sample_survey")
        ])
        self.table_type_combo.currentIndexChanged.connect(self.load_sample_table)
        table_type_layout.addWidget(QLabel(self.tr("table_type")))
        table_type_layout.addWidget(self.table_type_combo)
        left_layout.addLayout(table_type_layout)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)

        # Data Tab
        data_tab = QWidget()
        data_layout = QVBoxLayout(data_tab)
        self.table_widget = DynamicTable(self)
        self.table_widget.data_changed.connect(self.update_column_combos)
        data_layout.addWidget(QLabel(self.tr("data_table")))
        data_layout.addWidget(self.table_widget)
        self.tabs.addTab(data_tab, self.tr("data_tab"))

        # Chart Settings Tab
        settings_tab = QWidget()
        settings_layout = QVBoxLayout(settings_tab)

        # Chart Type
        type_group = QGroupBox(self.tr("chart_type"))
        type_layout = QHBoxLayout(type_group)
        self.chart_type_combo = QComboBox()
        chart_types = ["bar_chart", "line_chart", "pie_chart", "scatter_chart", "area_chart",
                       "histogram", "box_plot", "heatmap", "radar_chart", "polar_chart"]
        self.chart_type_combo.addItems([self.tr(t) for t in chart_types])
        self.chart_type_combo.currentIndexChanged.connect(self.on_chart_type_changed)
        type_layout.addWidget(self.chart_type_combo)
        settings_layout.addWidget(type_group)

        # Dynamic Settings Container
        self.settings_container = QWidget()
        self.settings_layout = QVBoxLayout(self.settings_container)
        settings_layout.addWidget(self.settings_container)

        # General Options
        general_group = QGroupBox(self.tr("general"))
        general_layout = QFormLayout(general_group)
        self.title_edit = QLineEdit("My Chart")
        self.xlabel_edit = QLineEdit("X Axis")
        self.ylabel_edit = QLineEdit("Y Axis")
        general_layout.addRow(self.tr("title"), self.title_edit)
        general_layout.addRow(self.tr("xlabel"), self.xlabel_edit)
        general_layout.addRow(self.tr("ylabel"), self.ylabel_edit)
        settings_layout.addWidget(general_group)

        # Checkboxes
        check_group = QGroupBox(self.tr("display"))
        check_layout = QHBoxLayout(check_group)
        self.grid_check = QCheckBox(self.tr("grid"))
        self.legend_check = QCheckBox(self.tr("legend"))
        self.three_d_check = QCheckBox(self.tr("3d"))
        self.grid_check.setChecked(True)
        self.legend_check.setChecked(True)
        for chk in [self.grid_check, self.legend_check, self.three_d_check]:
            check_layout.addWidget(chk)
        settings_layout.addWidget(check_group)

        self.tabs.addTab(settings_tab, self.tr("settings_tab"))

        # Advanced Tab
        adv_tab = QWidget()
        adv_layout = QFormLayout(adv_tab)
        self.font_spin = QSpinBox(); self.font_spin.setRange(8, 28); self.font_spin.setValue(12)
        self.line_spin = QDoubleSpinBox(); self.line_spin.setRange(0.5, 10); self.line_spin.setValue(2)
        self.marker_spin = QSpinBox(); self.marker_spin.setRange(1, 30); self.marker_spin.setValue(6)
        self.opacity_spin = QDoubleSpinBox(); self.opacity_spin.setRange(0.1, 1.0); self.opacity_spin.setSingleStep(0.1); self.opacity_spin.setValue(0.8)
        self.rotation_spin = QSpinBox(); self.rotation_spin.setRange(0, 90); self.rotation_spin.setValue(0)
        self.color_combo = QComboBox()
        self.color_combo.addItems(['tab10', 'viridis', 'plasma', 'cividis', 'turbo', 'Set1', 'Set2', 'Paired', 'hsv'])

        adv_layout.addRow(self.tr("font_size"), self.font_spin)
        adv_layout.addRow(self.tr("line_width"), self.line_spin)
        adv_layout.addRow(self.tr("marker_size"), self.marker_spin)
        adv_layout.addRow(self.tr("opacity"), self.opacity_spin)
        adv_layout.addRow(self.tr("rotation"), self.rotation_spin)
        adv_layout.addRow(self.tr("colors"), self.color_combo)

        self.bins_spin = QSpinBox(); self.bins_spin.setRange(3, 100); self.bins_spin.setValue(10)
        adv_layout.addRow("Bins:", self.bins_spin)

        self.tabs.addTab(adv_tab, self.tr("advanced"))

        left_layout.addWidget(self.tabs)

        # Action Buttons
        action_layout = QHBoxLayout()
        self.generate_btn = QPushButton(self.tr("generate"))
        self.save_btn = QPushButton(self.tr("save_image"))
        self.export_btn = QPushButton(self.tr("export_data"))
        self.import_btn = QPushButton(self.tr("import_data"))

        for btn in [self.generate_btn, self.save_btn, self.export_btn, self.import_btn]:
            btn.setMinimumHeight(48)
            btn.setStyleSheet("font-weight: bold; font-size: 14px;")
            action_layout.addWidget(btn)

        self.generate_btn.clicked.connect(self.generate_chart)
        self.save_btn.clicked.connect(self.save_image)
        self.export_btn.clicked.connect(self.export_data)
        self.import_btn.clicked.connect(self.import_csv)

        left_layout.addLayout(action_layout)
        left_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        left_panel.setWidget(left_content)
        main_layout.addWidget(left_panel)

        # Right Panel - Canvas
        self.canvas = FigureCanvasQTAgg(Figure(figsize=(10, 7)))
        self.canvas.figure.patch.set_facecolor('none')
        main_layout.addWidget(self.canvas, 3)

        # Initialize
        self.on_chart_type_changed(0)
        self.load_sample_table(0)  # Load empty table

    def load_sample_table(self, index):
        key = ["empty_table", "sample_sales", "sample_weather", "sample_students", "sample_survey"][index]
        df = SAMPLE_DATA[key]
        self.table_widget.set_data(df.copy())
        self.update_column_combos()

    def on_chart_type_changed(self, index):
        chart_type = ["bar_chart", "line_chart", "pie_chart", "scatter_chart", "area_chart",
                      "histogram", "box_plot", "heatmap", "radar_chart", "polar_chart"][index]
        self.clear_layout(self.settings_layout)

        df = self.table_widget.get_data()
        cols = list(df.columns) if not df.empty else []

        if chart_type in ["bar_chart", "pie_chart"]:
            cat_combo = QComboBox()
            val_combo = QComboBox()
            if cols:
                cat_combo.addItems(cols)
                val_combo.addItems(cols)
            form = QFormLayout()
            form.addRow(self.tr("categories_column"), cat_combo)
            form.addRow(self.tr("values_column"), val_combo)
            self.settings_layout.addLayout(form)
            self.settings_widgets = {'categories_column': cat_combo, 'values_column': val_combo}

        elif chart_type in ["line_chart", "scatter_chart", "area_chart", "polar_chart"]:
            x_combo = QComboBox()
            y_list = QListWidget()
            y_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            if cols:
                x_combo.addItems(cols)
                for col in cols:
                    item = QListWidgetItem(col)
                    y_list.addItem(item)
            form = QFormLayout()
            form.addRow(self.tr("x_column"), x_combo)
            form.addRow(self.tr("multi_series"), y_list)
            self.settings_layout.addLayout(form)
            self.settings_widgets = {'x_column': x_combo, 'y_columns': y_list}

        elif chart_type == "histogram":
            y_list = QListWidget()
            y_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            if cols:
                for col in cols:
                    item = QListWidgetItem(col)
                    y_list.addItem(item)
            form = QFormLayout()
            form.addRow(self.tr("select_series"), y_list)
            self.settings_layout.addLayout(form)
            self.settings_widgets = {'y_columns': y_list}

        elif chart_type == "box_plot":
            box_list = QListWidget()
            box_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            if cols:
                for col in cols:
                    item = QListWidgetItem(col)
                    box_list.addItem(item)
            form = QFormLayout()
            form.addRow(self.tr("box_datasets"), box_list)
            self.settings_layout.addLayout(form)
            self.settings_widgets = {'box_columns': box_list}

        elif chart_type == "heatmap":
            x_combo = QComboBox(); y_combo = QComboBox(); z_combo = QComboBox()
            if cols:
                for combo in [x_combo, y_combo, z_combo]:
                    combo.addItems(cols)
            form = QFormLayout()
            form.addRow(self.tr("heatmap_x"), x_combo)
            form.addRow(self.tr("heatmap_y"), y_combo)
            form.addRow(self.tr("heatmap_z"), z_combo)
            self.settings_layout.addLayout(form)
            self.settings_widgets = {'heatmap_x': x_combo, 'heatmap_y': y_combo, 'heatmap_z': z_combo}

        elif chart_type == "radar_chart":
            cat_combo = QComboBox(); val_list = QListWidget()
            val_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
            if cols:
                cat_combo.addItems(cols)
                for col in cols:
                    item = QListWidgetItem(col)
                    val_list.addItem(item)
            form = QFormLayout()
            form.addRow(self.tr("radar_categories"), cat_combo)
            form.addRow(self.tr("radar_values"), val_list)
            self.settings_layout.addLayout(form)
            self.settings_widgets = {'radar_categories': cat_combo, 'radar_values': val_list}

        self.settings_container.setLayout(self.settings_layout)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.clear_layout(child.layout())

    def update_column_combos(self):
        self.on_chart_type_changed(self.chart_type_combo.currentIndex())

    def change_language(self, index):
        langs = ["en", "fa", "zh", "ru"]
        self.translator.set_language(langs[index])
        self.apply_language()
        QMessageBox.information(self, "Language", self.tr("language_changed"))

    def change_theme(self, index):
        themes = ["windows_default", "light", "dark", "red", "blue"]
        self.current_theme = themes[index]
        self.apply_theme()

    def apply_theme(self):
        ThemeEngine.apply_theme(QApplication.instance(), self.current_theme)

    def apply_language(self):
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight if self.translator.direction() == "ltr" else Qt.LayoutDirection.RightToLeft)
        
        for widget in self.findChildren((QLabel, QPushButton)):
            text = widget.text()
            if text and text.strip():
                key = text.split(':')[0].strip().lower().replace(' ', '_').replace('(', '').replace(')', '')
                translated = self.tr(key)
                if translated != key:
                    if ':' in text:
                        widget.setText(translated + ":")
                    else:
                        widget.setText(translated)

        for group in self.findChildren(QGroupBox):
            title = group.title()
            if title:
                key = title.lower().replace(' ', '_')
                translated = self.tr(key)
                if translated != key:
                    group.setTitle(translated)

        self.tabs.setTabText(0, self.tr("data_tab"))
        self.tabs.setTabText(1, self.tr("settings_tab"))
        self.tabs.setTabText(2, self.tr("advanced"))

        self.setWindowTitle(self.tr("app_title"))

        # Update table type combo
        current = self.table_type_combo.currentIndex()
        self.table_type_combo.blockSignals(True)
        self.table_type_combo.clear()
        self.table_type_combo.addItems([
            self.tr("empty_table"),
            self.tr("sample_sales"),
            self.tr("sample_weather"),
            self.tr("sample_students"),
            self.tr("sample_survey")
        ])
        self.table_type_combo.setCurrentIndex(current)
        self.table_type_combo.blockSignals(False)

    def generate_chart(self):
        if self.chart_worker and self.chart_worker.isRunning():
            return
        df = self.table_widget.get_data()
        if df.empty:
            QMessageBox.warning(self, "Warning", "Please enter data in the table.")
            return

        params = {
            'title': self.title_edit.text(),
            'xlabel': self.xlabel_edit.text(),
            'ylabel': self.ylabel_edit.text(),
            'grid': self.grid_check.isChecked(),
            'legend': self.legend_check.isChecked(),
            '3d': self.three_d_check.isChecked(),
            'font_size': self.font_spin.value(),
            'line_width': self.line_spin.value(),
            'marker_size': self.marker_spin.value(),
            'opacity': self.opacity_spin.value(),
            'rotation': self.rotation_spin.value(),
            'colors': self.color_combo.currentText(),
            'bins': self.bins_spin.value()
        }

        chart_type_key = ["bar_chart", "line_chart", "pie_chart", "scatter_chart", "area_chart",
                          "histogram", "box_plot", "heatmap", "radar_chart", "polar_chart"][self.chart_type_combo.currentIndex()]

        if chart_type_key in ["bar_chart", "pie_chart"]:
            params['categories_column'] = self.settings_widgets['categories_column'].currentText()
            params['values_column'] = self.settings_widgets['values_column'].currentText()
        elif chart_type_key in ["line_chart", "scatter_chart", "area_chart", "polar_chart"]:
            params['x_column'] = self.settings_widgets['x_column'].currentText()
            params['y_columns'] = [item.text() for item in self.settings_widgets['y_columns'].selectedItems()]
        elif chart_type_key == "histogram":
            params['y_columns'] = [item.text() for item in self.settings_widgets['y_columns'].selectedItems()]
        elif chart_type_key == "box_plot":
            params['box_columns'] = [item.text() for item in self.settings_widgets['box_columns'].selectedItems()]
        elif chart_type_key == "heatmap":
            params['heatmap_x'] = self.settings_widgets['heatmap_x'].currentText()
            params['heatmap_y'] = self.settings_widgets['heatmap_y'].currentText()
            params['heatmap_z'] = self.settings_widgets['heatmap_z'].currentText()
        elif chart_type_key == "radar_chart":
            params['radar_categories'] = self.settings_widgets['radar_categories'].currentText()
            params['radar_values'] = [item.text() for item in self.settings_widgets['radar_values'].selectedItems()]

        self.chart_worker = ChartWorker(chart_type_key, df, params)
        self.chart_worker.finished.connect(self.display_chart)
        self.chart_worker.error.connect(self.show_error)
        self.chart_worker.start()

    def display_chart(self, fig: Figure):
        self.last_figure = fig
        self.canvas.figure.clear()
        self.canvas.figure = fig
        self.canvas.draw()
        QMessageBox.information(self, "Success", self.tr("chart_generated"))

    def save_image(self):
        if not self.last_figure:
            QMessageBox.warning(self, "Warning", "Generate a chart first!")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Images (*.png);;JPEG Images (*.jpg)")
        if path:
            self.last_figure.savefig(path, dpi=150, bbox_inches='tight')
            QMessageBox.information(self, "Saved", self.tr("file_saved"))

    def export_data(self):
        path, _ = QFileDialog.getSaveFileName(self, "Export CSV", "", "CSV Files (*.csv)")
        if path:
            df = self.table_widget.get_data()
            df.to_csv(path, index=False)
            QMessageBox.information(self, "Exported", self.tr("file_exported"))

    def import_csv(self):
        path, _ = QFileDialog.getOpenFileName(self, "Import CSV", "", "CSV Files (*.csv)")
        if path:
            try:
                df = pd.read_csv(path)
                self.table_widget.set_data(df)
                self.table_type_combo.setCurrentIndex(0)  # Switch to custom
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def show_error(self, msg):
        QMessageBox.critical(self, self.tr("error"), msg)

# ====================== Application Entry ======================
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Advanced Dynamic Chart Generator")
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 10))

    window = ChartGeneratorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()