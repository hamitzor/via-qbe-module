import mysql.connector
from search_modules.args import parser

args = parser.parse_args()

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8732",
    database="via-search-demo"
)


def insert_feature(vals):
    feature_count = 0

    curr = database.cursor()

    sql = "INSERT INTO `VideoFeatures` (`FrameNo`, `KeypointPtX`,`KeypointPtY`, `Descriptor`) VALUES (%s, %s, %s, %s)"

    val = []

    for index, f in enumerate(vals):
        frame_number = f['frame_number']
        f = f['data']
        for i in range(len(f[0])):
            feature_count = feature_count + 1
            val.append(
                (str(int(frame_number)), str(f[0][i].pt[0]), str(f[0][i].pt[1]), str(f[1][i].tolist())))

    curr.executemany(sql, val)
    database.commit()

    if not args.quiet:
        print str(feature_count) + " features inserted"


def get_video_path(id):
    curr = database.cursor()

    query = "SELECT Path FROM `Videos` WHERE `VideoId` = " + str(id)

    curr.execute(query)

    video = curr.fetchone()

    return video[0]
