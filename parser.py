import os

#Словарь для соответствия цифр и слов
digit_to_word = {
    '0': 'window',
    '1': 'filled',
    '2': 'empty'
}
#Путь к папке "labels"
labels_folder = 'yolov5-master/runs/detect/exp/labels'


#Путь к папке "result" для сохранения обновленных файлов
result_folder = 'result'

#Создаем папку "result", если она не существует
if not os.path.exists(result_folder):
    os.mkdir(result_folder)

#Пройдем по всем файлам в папке "labels"
for root, dirs, files in os.walk(labels_folder):
    for filename in files:
        if filename.endswith('.txt'):
            file_path = os.path.join(root, filename)

#Открываем файл для чтения и чтения всего его содержимого
            with open(file_path, 'r') as file:
                lines = file.readlines()

#Заменяем первую цифру на соответствующее слово
            for i, line in enumerate(lines):
                parts = line.split()
                if parts and parts[0] in digit_to_word:
                    parts[0] = digit_to_word[parts[0]]
                    lines[i] = ' '.join(parts) + '\n'

#Формируем путь для сохранения обновленного файла в папке "result"
            result_file_path = os.path.join(result_folder, filename)

#Записываем обновленные строки в файл в папке "result"
            with open(result_file_path, 'w') as result_file:
                result_file.writelines(lines)