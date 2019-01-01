import mysql.connector
import config
# import pypika:https://github.com/kayak/pypika
from pypika import MySQLQuery, Table, Field

# connect to database
database = mysql.connector.connect(
    host=config.db_host,
    user=config.db_user,
    passwd=config.db_password,
    database=config.db_database
)

curr = database.cursor()


def insert_feature(features, frame_number):
    """Inserts video features into VideoFeatures table
                Args:
                    features (:obj:`tuple`): Tuple of list of key points and list of descriptors with corresponding indexes, respectively.
                    frame_number (int) frame number that feature list has extracted.
                """
    feature_count = 0

    table = Table('VideoFeatures')

    # Create sql object.
    sql = MySQLQuery.into(table).columns('FrameNo', 'KeyPointPtX', 'KeyPointPtY', 'Descriptor')

    # Iterate over data and add insert part for every piece.
    for i in range(len(features[0])):
        feature_count = feature_count + 1
        sql = sql.insert(frame_number, features[0][i].pt[0], features[0][i].pt[1], str(features[1][i].astype(int).tolist()).replace(" ", ""))

    # Extract sql string from sql object and execute.
    curr.execute(sql.get_sql())
    database.commit()

    return True


def get_video_path(id):
    """Get video features with id

                Args:
                    id (int): VideoId to be used.
                Returns:
                    path (:obj:`str`): Video path
                """
    table = Table('Videos')

    # Create sql object.
    sql = MySQLQuery.from_('Videos').select('Path').where(table.VideoId == id)

    # Extract sql string from sql object and execute.
    curr.execute(sql.get_sql())

    video = curr.fetchone()

    return video[0]


def get_video_features(begin, end):
    """Get video path with id

            Args:
                begin (int): Beginning FrameNo to be collected.
                end (int): Ending FrameNo to be collected.
            Returns:
                :obj:`tuple`: A tuple consist of list of key points and descriptors with corresponding indexes, respectively
            """
    table = Table('VideoFeatures')

    # Create sql object.
    sql = MySQLQuery.from_('VideoFeatures').select("KeyPointPtX", "KeyPointPtY", "Descriptor", "FrameNo").where(
        (table.FrameNo <= end) & (table.FrameNo >= begin))

    # Extract sql string from sql object and execute.
    curr.execute(sql.get_sql())

    features = curr.fetchall()

    return features