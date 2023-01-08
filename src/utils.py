import os

#remove prefix from string
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever


#get path path of running script
def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))

def escape_path(file_path):
    file_path = "\"" + file_path + "\""
    return file_path
            