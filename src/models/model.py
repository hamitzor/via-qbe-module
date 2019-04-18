"""This module has a Model class to be inherited by all model classes."""
import mysql.connector


class Model(object):
    """Parent class of all model classes"""

    def __init__(self, config):
        """Class Constructor.

        Args:
          config (tuple): A tuple holds configuration settings 

        """
        self.config = config
        self.connection = None

    def connect(self):
        """Connect to database specified by config.

        Returns:
          Connection object

        """
        self.connection = mysql.connector.connect(
            host=self.config["db_host"],
            user=self.config["db_username"],
            passwd=self.config["db_password"],
            database=self.config["db_name"]
        )

    def disconnect(self):
        """Disconnect and remove connection."""
        self.connection.close()
        self.connection = None

    def convert_dict(self, description, result):
        """Convert tuple result into a more useful dictionary with a key
        of column name and a value of column value"""
        if result is None:
            return None

        result_dictionary = dict()

        for i in range(len(description)):
            result_dictionary[description[i][0]] = result[i]

        return result_dictionary

    def get_set_statements(self, data):
        """Arrange a string and a list to be used in UPDATE operations

        Args:
          data (:obj:`dictionary`): new data

        Returns:
          :obj:`tuple`: tuple of string and list

        """
        string = ""
        value_list = []

        for key, value in data.iteritems():
            string += str(key)+" = %s, "
            value_list.append(value)

        string = string[:-2]

        return string, value_list
