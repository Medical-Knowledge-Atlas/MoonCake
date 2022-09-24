import os


def get_filename(file_path):
    """
    根据路径名称获取文件夹下的文件名
    :param file_path:
    :return:
    """
    return os.listdir(file_path)


def read_files(file_path) -> list:
    """
    根据文件夹路径获取改文件夹下文件内容
    :param file_path:
    :return:
    """
    filenames = get_filename(file_path)
    current_path = os.getcwd()
    for filename in filenames:
        # 过滤非json文件
        if not filename.endswith('json'):
            continue
        dataset_path = f'{current_path}/{file_path}/{filename}'
        with open(dataset_path, 'r') as f:
            yield f.read()


if __name__ == '__main__':
    for i in read_files('../dataset'):
        print(i)
