"""This module has OperationModel"""

from .model import Model


class OperationModel(Model):
    """Model to be used in database operations related with operations"""

    def get(self, operation_id):
        """Get operation with operation_id.

        Args:
          operation_id (int): id of the operation

        Returns:
          :obj:`list` of :obj:`str`: operation tuple

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""SELECT *
                FROM operations
                WHERE
                operation_id = %s""")

        sql_data = (operation_id,)

        curr.execute(sql, sql_data)
        result = curr.fetchone()
        self.disconnect()
        return self.convert_dict(curr.description, result)

    def update(self, operation_id, data):
        """Update operation

        Args:
          operation_id (int): id of the operation
          data (:obj:`dict`): data dict object

        """
        self.connect()
        curr = self.connection.cursor()

        set_statements, set_data = self.get_set_statements(data)

        set_data.append(operation_id)

        sql = ("""UPDATE operations SET %s WHERE operation_id = %s""" %
               (set_statements, "%s"))

        print sql
        curr.execute(sql, set_data)
        self.connection.commit()

        self.disconnect()
