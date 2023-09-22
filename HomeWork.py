import os

def rename_files(directory, desired_name, num_digits, source_extension, destination_extension, name_range=None):
    """
    :param directory: Каталог, в котором нужно переименовать файлы.
    :param desired_name: Желаемое конечное имя файлов.
    :param num_digits: Количество цифр в порядковом номере.
    :param source_extension: Расширение исходного файла.
    :param destination_extension: Расширение конечного файла.
    :param name_range: Диапазон символов, которые берутся из исходного имени файла.
    """
    files = os.listdir(directory)
    files = [file for file in files if file.endswith(source_extension)]
    counter = 1
    for file in files:
        counter_str = str(counter).zfill(num_digits)

        base_name, _ = os.path.splitext(file)

        if name_range:
            base_name = base_name[name_range[0] - 1:name_range[1]]

        new_name = base_name + desired_name + counter_str + destination_extension

        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)

        counter += 1

rename_files('C:/Users/shake/PycharmProjects/pogruzhenie_seminar7', '_myNew_', 3, '.png', '.txt', (3, 6))
