import os
import pandas as pd
import pathlib as pl
import ntpath
import logging
import smart_open as so
from datetime import datetime
import glob
import pickle as pkl
import shutil
import json


def date_time(dt: str, tz: bool = True) -> str:
    """
    Converts a datetime from any possible datatime format as a string into a string of YYYY-MM-DDThh:mm:ssZ format.
    This is used frequently to store datetimes in databases (e.g. Graph Stores need this for "<date>"^^xsd:dateTime).

    BEWARE THAT IN CASE OF VALUE ERROR THE DATE RETURNED IS ABSURD.
    :param dt: the datetime as to convert into 'YYYY-MM-DD hh:mm:sS'
    :param tz: adds a T between the date and the time, and appends 'Z' at the end of the resulting datetime
    :return: 1) the date formatted as 'YYYY-MM-DDThh:mm:ssZ' if the conversion was successful, 2) None if the
        incoming parameter is None or '', an absurd date () if the incoming datetime does not contain a valid datetime;

    """
    error = '0000-00-00T00:00:00Z'
    if not dt or dt == '':
        return None
    try:
        return pd.to_datetime(dt).__str__().replace(' ', 'T') + 'Z' if tz else pandas.to_datetime(dt).__str__()
    except Exception as ex:
        log(f"Error parsing datetime. Exception: {ex}")
        return error

def url_tail(url: str, sep: str = '/'):
    return url.rsplit(sep, 1)[1]


def timestamp(file: str) -> str:
    """
    Returns the timestamp of a file
    """
    modified = os.path.getmtime(file)
    return datetime.fromtimestamp(modified).__str__()


def rmdir(dir_: str):
    """
    Removes a directory from the filesystem
    """
    if xst_file(dir_):
        shutil.rmtree(dir_)


def copy_file(source: str, target: str):
    make_file_dirs(target)
    shutil.copy(source, target)
    return


def xst_dir(dir_: str) -> bool:
    """
    Tells whether a directory is a directory and if it exists.
    """
    path = pl.Path(dir_)
    return path.exists() and path.is_dir()


def find_first(base_dir: str, file_pattern: str) -> str:
    if not xst_file(base_dir):
        raise IOError
    res = list(pl.Path(base_dir).rglob(file_pattern))
    if len(res) > 0:
        return res[0]
    else:
        return None


def now() -> datetime:
    return datetime.now()


def pickle(out: str, obj):
    make_file_dirs(out)
    with open(out, 'wb') as handle:
        pkl.dump(obj, handle, protocol=pkl.HIGHEST_PROTOCOL)
    return


def to_csv(out: str, dictionary: dict):
    cols = list(dictionary.keys())
    data = list(dictionary.values())
    df = pd.DataFrame(data=[data], columns=cols)
    df.to_csv(out, index=False)


def unpickle(file: str):
    with open(file, 'rb') as handle:
        return pkl.load(handle, fix_imports=True)


def log(message: str, level: str = None, condition: bool = True, logger: logging.Logger = None) -> datetime:
    """
    Logs a message
    :param message: the text to print and log
    :param level: info, warning or error
    :param condition: skips the job if a specified condition is not met
    :param logger: the logger used to print and save the execution events
    """
    if condition:
        _logger = logging.getLogger() if not logger else logger
        if _logger.level == logging.getLevelName('INFO') or level == 'i':
            _logger.info(message)
        elif _logger.level == logging.getLevelName('WARNING') or level == 'w':
            _logger.warning(message)
        elif _logger.level == logging.getLevelName('ERROR') or level == 'e':
            _logger.error(message)
    return now()


def list_dirs(root_dir: str):
    """
    Returns list with the names of the first level directories inside a root path.
    """
    return list(os.walk(root_dir))[1]


def drop_file(path: str):
    if os.path.isfile(path):
        os.remove(path)


def drop_dir(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)


def drop_sub_dir_except(path_dir: str, list_except_dir: list):
    sub_folders = [file_dir.path for file_dir in os.scandir(path_dir) if file_dir.is_dir()]
    for path_folder in sub_folders:
        if path_folder not in list_except_dir:
            drop_dir(path_folder)


def file_drop_ext(file_name: str) -> str:
    return file_split_name_ext(file_name)[0]


def file_split_name_ext(file_name: str) -> (str, str):
    v = os.path.splitext(file_name)
    return v[0], v[1]


def txt_to_file(path: str, text: str):
    to_file(text, path)


def to_file(txt: str, path: str):
    with open(path, 'w+', encoding="utf-8") as file:
        if txt:
            file.write(txt)


def make_file_dirs(file_pathname: str) -> str:
    """
    Given the complete path to a file, creates the directories preceding the name of the file
    :param file_pathname: the name of the file
    :return: the path created, without the name of the file
    """
    dir_, file_ = ntpath.split(file_pathname)
    os.makedirs(dir_, exist_ok=True)
    return dir_ if len(dir_) != 0 else None


def get_dir_file_ext(path_filename: str) -> (str, str, str):
    dir_, file_ = ntpath.split(path_filename)
    file_, ext_ = get_file(path_filename)
    return dir_, file_, ext_


def get_file_name_from_path(path) -> str:
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def xst_file(path: str) -> bool:
    """
    Checks whether a file or directory exists or not.
    :param path:  the path to the dir or file
    :return: the result of the checking
    """
    return os.path.isdir(path) or os.path.isfile(path)


def dir_tail(dir_: str):
    return pl.PurePath(dir_).name


def get_file(path_filename: str) -> (str, str):
    name, ext = file_split_name_ext(get_file_name_from_path(path_filename))
    return name, ext


def get_files(root_dir: str, exclude: [] = None) -> (int, str, str, str):
    """
    Returns lazily and recursively each path file name, the file name, extension and an index number from
    inside the folders of a root folder
    :param root_dir: the initial folder with the directories and files
    :param exclude: list of files or directories to not get into
    :return: file absolute path, file name, extension, and its index number
    """
    exclude = [] if not exclude else exclude
    i: int = 0
    # dir?
    xst_file(root_dir)
    # For every file in the directory structure
    for path in glob.iglob(root_dir + '**/**', recursive=True):
        xpath = pl.PurePath(path)
        if xpath.name not in exclude:
            if os.path.isfile(path):
                i += 1
                name, ext = get_file(path)
                yield i, path, name, ext


def from_json(file: str) -> dict:
    with open(file, 'r') as fp:
        return json.load(fp)


def to_json(dic: dict, file: str):
    with open(file, 'w') as fp:
        json.dump(dic, fp, indent=4)


def file_to_str(path_filename: str, bytes_number: int = 0) -> str:
    """
    Use this to avoid problems with encoding.
    """
    if not xst_file(path_filename):
        return None
    file_size = pl.Path(path_filename).stat().st_size
    offset = bytes_number if bytes_number != 0 and bytes_number < file_size else file_size
    try:
        with so.open(path_filename, 'rb') as fin:
            return fin.read(offset).decode('utf-8')
    except Exception as ex:
        raise ex


def is_number(alpha: str) -> bool:
    if '%' in alpha:
        return False

    try:
        num = complex(alpha)
        return num == num or '%' in alpha
    except ValueError:
        return False
