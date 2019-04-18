"""This module has Logger class to be used in logging purposes"""
import time
from os import path


class Logger(object):
    def __init__(self, directory, supress=False):
        """Class Constructor.

          Args:
            directory (str): logging directory
            supress (bool): if true logging is supressed

          """
        self._directory = directory
        self._supress = supress

    def _date(self):
        return time.strftime("%d_%m_%Y")

    def _time(self):
        return time.strftime("%H:%M:%S")

    def _path(self):
        return path.join(self._directory, self._date()+".log")

    def _log(self, message):
        time = self._time()
        save_path = self._path()

        if not self._supress:
            if path.exists(self._directory):
                with open(save_path, "a") as f:
                    try:
                        f.write(time+": "+message+"\n")
                    except IOError:
                        print "Could not log this message : " + time+": "+message+"\n"
            else:
                print "Could not log this message : " + time+": "+message+"\n"

    def error(self, message):
        self._log("ERROR -- "+message)

    def info(self, message):
        self._log("INFO -- "+message)
