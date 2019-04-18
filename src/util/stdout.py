"""Includes some helper functions."""

import time
import sys


class Stdout(object):
    """Class that handles standart out operations."""

    def __init__(self, supress):
        """Class constructor.

        Arguments:
          supress {Boolean} -- True if stdout is supressed
        """
        self.supressed = supress

    def passed_time(self, start_time, desc):
        """Print an info message that containts time since start_time and desc.

        Arguments:
          start_time {int} -- Start time
          desc {string} -- Description
        """
        if not self.supressed:
            print ""
            elapsed_time = time.time() * 1000 - start_time
            print desc, str(int(elapsed_time)) + "ms"

    def progres_info(self, percentage):
        """Print an info message about progress.

        Arguments:
          percentage {int} -- Percentage of progress
        """
        if not self.supressed:
            sys.stdout.write("\r" + str(percentage) + "% of video processed")
            sys.stdout.flush()

    def write(self, message):
        """Print message.

        Arguments:
          message {string} -- Message
        """
        if not self.supressed:
            print str(message)
