"""This module has VideoModel"""

from .model import Model


class VideoModel(Model):
    """Model to be used in database operations related with videos"""

    def get(self, video_id):
        """Get video with video_id.

        Args:
          video_id (int): id of the video

        Returns:
          :obj:`dict`: video dict object

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""SELECT *
                FROM videos
                WHERE
                video_id = %s""")

        sql_data = (video_id,)

        curr.execute(sql, sql_data)
        result = curr.fetchone()

        self.disconnect()
        return self.convert_dict(curr.description, result)

    def update(self, video_id, data):
        """Update video

        Args:
          video_id (int): id of the video
          data (:obj:`dict`): data dict object

        """
        self.connect()
        curr = self.connection.cursor()

        set_statements, set_data = self.get_set_statements(data)

        set_data.append(video_id)

        sql = ("""UPDATE videos SET %s WHERE video_id = %s""" %
               (set_statements, "%s"))

        print sql
        curr.execute(sql, set_data)
        self.connection.commit()

        self.disconnect()
