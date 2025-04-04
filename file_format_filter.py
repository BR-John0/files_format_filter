from zipfile import ZipFile
from pathlib import Path


path_to_zip_file = "test_files.zip" #Путь к файлу .zip
filter_format_for_files = ".java" #Расширение файла для фильтрования


def extract_all_files_from_zip(path_to_file): #Функция для извлечения всех файлов архива
    with ZipFile(path_to_file, 'r') as zip_archive:
        return zip_archive.namelist()

def filter_files_in_zip(filter_format, files): #Функция для фильтрования всех извлечённых файлов
    for file in files:
        if file.endswith(filter_format):
            filtered.append(file)
        else:
            others.append(file)

filtered = []
others = []

res = extract_all_files_from_zip(path_to_zip_file)
filter_files_in_zip(filter_format_for_files, res)

print("Все файлы в архиве:", res)
print("фильтрованные:", filtered)
print("Другие:", others)
