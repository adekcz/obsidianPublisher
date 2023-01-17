import os

#remove prefix from string
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        suffix = text[len(prefix):]
        if suffix.startswith(os.sep):
            suffix = suffix[len(os.sep):]
        return suffix
    return text  # or whatever

def get_file_name(file_path):
    return file_path.split(os.sep)[-1]

#copy file
def copy_file(source, destination):
    with open(source, "rb") as file:
        data = file.read()
    with open(destination, "wb") as file:
        file.write(data)

#get path path of running script
def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))

def escape_path(file_path):
    file_path = "\"" + file_path + "\""
    return file_path
            