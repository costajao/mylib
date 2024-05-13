import os


def list_files(directory):
    return os.listdir(directory)


def file_exists(filename):
    return os.path.exists(filename)
