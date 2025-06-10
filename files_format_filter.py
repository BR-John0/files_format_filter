import sys
import zipfile
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Фильтр формата файлов")
window.resize(750, 650)
window.show()

formats_list = ["*"]
files_list = []

def open_file_dialog():
    global files_list
    file_path, _ = QFileDialog.getOpenFileName(choose_file_btn, "Выбрать ZIP-файл","","ZIP Архив (*.zip)")
    if not file_path:
        return
    try:
        with zipfile.ZipFile(file_path, 'r') as zf:
            file_name_txt.setText(f"Название файла: {zf.filename}")
            file_path_txt.setText(f"Путь к файлу: {file_path}")
            
            files_list = zf.namelist()
            files_list_view.addItems(files_list)
            for item in files_list:
                ext = item.split('.')[-1].lower()
                if not ext in formats_list:
                    formats_list.append(ext)
            unload_file_btn.setEnabled(True)
            filter_btn.setEnabled(True)
            unload_file_btn.setToolTip("Отгружает .zip архив.")
            filter_btn.setToolTip("Фильтрует файлы по выбранному расширению.")
            formats_combo_box.clear()
            formats_combo_box.addItems(formats_list)

    except Exception as i:
        file_name_txt.setText(f'Ошибка взаимодействия с архивом: {i}')

def unload_file():
    unload_file_btn.setEnabled(False)
    filter_btn.setEnabled(False)
    formats_list = ["*"]
    files_list = []
    formats_combo_box.clear()
    formats_combo_box.addItem("*")
    files_list_view.clear()
    file_name_txt.setText("Название выбранного файла")
    file_path_txt.setText("Путь к выбранному файлу")
    unload_file_btn.setToolTip("Отгружает .zip архив. Необходимо выбрать .zip архив.")
    filter_btn.setToolTip("Фильтрует файлы по выбранному расширению. Необходимо выбрать .zip архив.")

def filter_files_by_format():
    global files_list
    new_list = []
    if formats_combo_box.currentText() == "*":
        files_list_view.clear()
        files_list_view.addItems(files_list)
    else:
        for item in files_list:
            ext = item.split('.')[-1].lower()
            if formats_combo_box.currentText() == ext:
                new_list.append(item)
        files_list_view.clear()
        files_list_view.addItems(new_list)

main_layout = QHBoxLayout()
window.setLayout(main_layout)

buttons_group_box = QGroupBox("Инструменты")
list_layout = QVBoxLayout()
buttons_layout = QVBoxLayout()
inner_buttons_layout = QVBoxLayout(buttons_group_box)
main_layout.addLayout(list_layout)
main_layout.addLayout(buttons_layout)

files_list_view = QListWidget()
file_name_txt = QLabel(text="Название выбранного файла")
file_path_txt = QLabel(text="Путь к выбранному файлу")

formats_combo_box = QComboBox(buttons_group_box)
choose_file_btn = QPushButton("Выбрать .zip файл", buttons_group_box)
filter_btn = QPushButton("Фильтровать", buttons_group_box)
unload_file_btn = QPushButton("Отгрузить файл", buttons_group_box)

list_layout.addWidget(file_name_txt)
list_layout.addWidget(file_path_txt)
list_layout.addWidget(files_list_view)
buttons_layout.addWidget(buttons_group_box)
inner_buttons_layout.addWidget(choose_file_btn)
inner_buttons_layout.addWidget(formats_combo_box)
inner_buttons_layout.addWidget(filter_btn)
inner_buttons_layout.addWidget(unload_file_btn)
formats_combo_box.addItems(formats_list)
inner_buttons_layout.addStretch(1)
unload_file_btn.setEnabled(False)
filter_btn.setEnabled(False)

filter_btn.setToolTip("Фильтрует файлы по выбранному расширению. Необходимо выбрать .zip архив.")
choose_file_btn.setToolTip("Выберете .zip архив")
unload_file_btn.setToolTip("Отгружает .zip архив. Необходимо выбрать .zip архив.")

choose_file_btn.clicked.connect(open_file_dialog)
unload_file_btn.clicked.connect(unload_file)
filter_btn.clicked.connect(filter_files_by_format)

app.exec_()
