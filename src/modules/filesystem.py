"""Module contains methods for filesystem operations."""

from os import path


def write_base64(bin_string, extension, directory="/tmp"):
    """Decode base 64 encoded string and write into a file with specified extension and directory.

    Arguments:
      bin_string {str} -- encoded string
      extension {str} -- extension of the file

    Keyword Arguments:
      directory {str} -- directory that file will be created in (default: {"/tmp"})

    Returns:
      str -- path of the file that has been created

    """
    import base64
    from random import randint

    decoded_string = base64.b64decode(bin_string)
    file_name = str(randint(100000, 999999)) + extension

    with open(path.join(directory, file_name), "w") as file:
        file.write(decoded_string)

    return path.join(directory, file_name)
