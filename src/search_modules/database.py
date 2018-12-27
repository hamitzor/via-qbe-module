import mysql.connector
import config
from args import parser
from pypika import MySQLQuery, Table, Field
import random

args = parser.parse_args()

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
                Returns:
                    None
                """
    feature_count = 0

    table = Table('VideoFeatures')

    q = MySQLQuery.into(table)

    for i in range(len(features[0])):
        feature_count = feature_count + 1
        q = q.insert(random.randrange(1, 2147483646), frame_number,
                     features[0][i].pt[0], features[0][i].pt[1], features[1][i][0], features[1][i][1], features[1][i][2], features[1][i][3],
                     features[1][i][4], features[1][i][5], features[1][i][6], features[1][i][7], features[1][i][8], features[1][i][9],
                     features[1][i][10], features[1][i][11], features[1][i][12], features[1][i][13], features[1][i][14], features[1][i][15],
                     features[1][i][16], features[1][i][17], features[1][i][18], features[1][i][19], features[1][i][20], features[1][i][21],
                     features[1][i][22], features[1][i][23], features[1][i][24], features[1][i][25], features[1][i][26], features[1][i][27],
                     features[1][i][28], features[1][i][29], features[1][i][30], features[1][i][31], features[1][i][32], features[1][i][33],
                     features[1][i][34], features[1][i][35], features[1][i][36], features[1][i][37], features[1][i][38], features[1][i][39],
                     features[1][i][40], features[1][i][41], features[1][i][42], features[1][i][43], features[1][i][44], features[1][i][45],
                     features[1][i][46], features[1][i][47], features[1][i][48], features[1][i][49], features[1][i][50], features[1][i][51],
                     features[1][i][52], features[1][i][53], features[1][i][54], features[1][i][55], features[1][i][56], features[1][i][57],
                     features[1][i][58], features[1][i][59], features[1][i][60], features[1][i][61], features[1][i][62], features[1][i][63],
                     features[1][i][64], features[1][i][65], features[1][i][66], features[1][i][67], features[1][i][68], features[1][i][69],
                     features[1][i][70], features[1][i][71], features[1][i][72], features[1][i][73], features[1][i][74], features[1][i][75],
                     features[1][i][76], features[1][i][77], features[1][i][78], features[1][i][79], features[1][i][80], features[1][i][81],
                     features[1][i][82], features[1][i][83], features[1][i][84], features[1][i][85], features[1][i][86], features[1][i][87],
                     features[1][i][88], features[1][i][89], features[1][i][90], features[1][i][91], features[1][i][92], features[1][i][93],
                     features[1][i][94], features[1][i][95], features[1][i][96], features[1][i][97], features[1][i][98], features[1][i][99],
                     features[1][i][100], features[1][i][101], features[1][i][102], features[1][i][103], features[1][i][104], features[1][i][105],
                     features[1][i][106], features[1][i][107], features[1][i][108], features[1][i][109], features[1][i][110], features[1][i][111],
                     features[1][i][112], features[1][i][113], features[1][i][114], features[1][i][115], features[1][i][116], features[1][i][117],
                     features[1][i][118], features[1][i][119], features[1][i][120], features[1][i][121], features[1][i][122], features[1][i][123],
                     features[1][i][124], features[1][i][125], features[1][i][126], features[1][i][127])

    curr.execute(q.get_sql())
    database.commit()

    if not args.quiet and not args.api:
        print str(feature_count) + " features extracted and inserted"


def get_video_path(id):
    """Get video features with id

                Args:
                    id (int): VideoId to be used.
                Returns:
                    path (:obj:`list`): Video path
                """
    table = Table('Videos')

    q = MySQLQuery.from_('Videos').select('Path').where(table.VideoId == id)

    curr.execute(q.get_sql())

    video = curr.fetchone()

    return video[0]


def get_video_features(no):
    """Get video path with id

            Args:
                id (int): VideoId to be used.
            Returns:
                :obj:`tuple`: A tuple consist of list of key points and descriptors with corresponding indexes, respectively
            """
    table = Table('VideoFeatures')

    q = MySQLQuery.from_('VideoFeatures').select("*")

    curr.execute(q.get_sql())

    features = curr.fetchall()

    return features
