"""This module has FeatureModel"""

from .model import Model


class FeatureModel(Model):
    """Model to be used in database operations related with features"""

    def get_multiple(self, video_id, frame_no):
        """Get features of video from begin frame to end frame.

        Args:
          video_id (int): id of the video that features are queried from
          frame_no (int): Number of the frame that features are in

        Returns:
          :obj:`list` of :obj:`tuple`: List of features

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""SELECT keypoint_pt_x, keypoint_pt_y, descriptor, frame_no
                FROM qbe_features
                WHERE
                (frame_no = %s)
                AND
                (qbe_feature_id IN 
                (SELECT qbe_feature_id from video_qbe_feature 
                WHERE video_qbe_feature.video_id = %s)) """)

        sql_data = (frame_no, video_id)

        curr.execute(sql, sql_data)
        features = curr.fetchall()
        self.disconnect()
        return features

    def insert_multiple(self, video_id, data):
        """Insert specified rows.

        Arguments:
          video_id (int): video_id of the video that features are extracted from
          data (:obj:`list` of :obj:`tuple`): List of tuples holds appropriate data

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""INSERT INTO qbe_features
                (keypoint_pt_x, keypoint_pt_y, descriptor, frame_no)
                VALUES (%s, %s, %s, %s)""")

        curr.executemany(sql, data)
        first_row_id = curr.lastrowid
        last_row_id = first_row_id + curr.rowcount - 1

        sql = ("""INSERT INTO video_qbe_feature
                (qbe_feature_id, video_id)
                VALUES (%s, %s)""")

        sql_data = []

        # Iterate and append to sql_data
        for i in range(first_row_id, last_row_id+1):
            sql_data.append((i, video_id))

        curr.executemany(sql, sql_data)

        self.connection.commit()
        self.disconnect()

        return last_row_id - first_row_id + 1
