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

#get path path of running script
def get_runtime_script_path(file):
    return os.path.dirname(os.path.realpath(file))

def escape_path(file_path):
    file_path = "\"" + file_path + "\""
    return file_path
            