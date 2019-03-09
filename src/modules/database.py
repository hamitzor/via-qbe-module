"""File holds Database class."""
import mysql.connector
from modules import config as default_config


class Database(object):
    """Class that handles database operations."""

    def __init__(self, config):
        """Class Constructor."""
        self.config = config
        self.connection = None

    def connect(self):
        """Connect to database specified by config.

        Returns:
          mysql.connection.MySQLConnection -- connection object

        """
        self.connection = mysql.connector.connect(
            host=self.config.db_host,
            user=self.config.db_user,
            passwd=self.config.db_password,
            database=self.config.db_database
        )

    def disconnect(self):
        """Disconnect and remove connection."""
        self.connection.close()
        self.connection = None

    def insert_features(self, video_id, data):
        """Insert specified data into VideoFeatures table.

        Arguments:
          video_id {int} -- VideoId of the video that features are extracted from
          data {:obj:`list` of :obj:`tuple`} -- List of rows

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""INSERT INTO VideoFeatures
                (FrameNo, KeyPointPtX, KeyPointPtY, Descriptor)
                VALUES (%s, %s, %s, %s)""")

        curr.executemany(sql, data)
        first_row_id = curr.lastrowid
        last_row_id = first_row_id + curr.rowcount - 1

        sql = ("""INSERT INTO VideoVideoFeature
                (VideoFeatureId, VideoId)
                VALUES (%s, %s)""")

        sql_data = []

        # Iterate over data format and append to sql_data
        for i in range(first_row_id, last_row_id):
            sql_data.append((i, video_id))

        curr.executemany(sql, sql_data)

        self.connection.commit()
        self.disconnect()

    def get_features(self, video_id, frame_no):
        """Get features from video from begin frame to end frame.

        Arguments:
          video_id {int} -- VideoId of the video that features are queried from
          frame_no {int} -- Number of frame that features are in

        Returns:
          :obj:`list` of :obj:`tuple` -- List of features

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""SELECT KeyPointPtX, KeyPointPtY, Descriptor, FrameNo
                FROM VideoFeatures
                WHERE
                (VideoFeatures.FrameNo = %s)
                AND
                (VideoFeatures.VideoFeatureId IN (SELECT VideoFeatureId from VideoVideoFeature WHERE VideoVideoFeature.VideoId = %s)) """)
        sql_data = (frame_no, video_id)

        curr.execute(sql, sql_data)
        features = curr.fetchall()
        self.disconnect()
        return features

    def get_video(self, video_id, field="*"):
        """Get a video.

        Arguments:
          video_id {int} -- VideoId of the video
          field {str} -- Particular field to be selected (default: {"*"})

        Returns:
          :obj:`tuple` -- Result tuple

        """
        self.connect()
        curr = self.connection.cursor()

        sql = """SELECT %s
                FROM Videos
                WHERE Videos.VideoId = %s""" % (field, video_id)

        curr.execute(sql)
        video = curr.fetchone()
        self.disconnect()
        return video if field == "*" else video[0]

    def insert_video(self, data):
        """Insert specified data into Videos table.

          Arguments:
            data {:obj:`tuple`} -- Row to be inserted

        """
        self.connect()
        curr = self.connection.cursor()

        sql = ("""INSERT INTO Videos
            (Title, Length, Format, Name, Size,
            Content, FPS, TotalFrame, Width, Height)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")

        curr.execute(sql, data)
        self.connection.commit()
        self.disconnect()


database = Database(default_config)
