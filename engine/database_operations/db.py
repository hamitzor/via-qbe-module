import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8732",
    database="via-search-demo"
)


def insertFeature(vals):
    featureCount = 0

    curr = database.cursor()

    sql = "INSERT INTO `VideoFeatures` (`FrameNo`, `KeypointPtX`,`KeypointPtY`, `Descriptor`) VALUES (%s, %s, %s, %s)"

    val = []

    for index, f in enumerate(vals):
        frameNumber = f['frameNumber']
        f = f['data']
        for i in range(len(f[0])):
            featureCount = featureCount + 1
            val.append(
                (str(int(frameNumber)), str(f[0][i].pt[0]), str(f[0][i].pt[1]), str(f[1][i].tolist())))

    curr.executemany(sql, val)
    database.commit()

    print str(featureCount) + " features inserted"


def getVideoPath(id):
    curr = database.cursor()

    query = "SELECT Path FROM `Videos` WHERE `VideoId` = " + str(id)

    curr.execute(query)

    video = curr.fetchone()

    return video[0]