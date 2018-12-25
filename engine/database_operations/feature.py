def insertFeature(vals):
    import _mysql

    mydb = _mysql.connect(
        host="localhost",
        user="root",
        passwd="8732",
        db="via-search-demo"
    )

    featureCount = 0

    sql = "INSERT INTO `VideoFeatures` (`VideoFeatureId`, `FrameNo`, `KeypointPt`, `Descriptor`) VALUES "

    for index, f in enumerate(vals):
        frameNumber = f['frameNumber']
        f = f['data']
        for i in range(len(f[0])):
            if i > 0:
                sql = sql + ","
            featureCount = featureCount + 1
            sql = sql + "(NULL, '" + str(int(frameNumber)) + "', ST_GeomFromText('POINT(" + str(f[0][i].pt[0]) + " " + str(
                f[0][i].pt[1]) + ")'), '" + str(f[1][i].tolist()) + "')"

        if index != len(vals) - 1:
            sql = sql + ","

    mydb.query(sql)

    mydb.commit()

    print str(featureCount) + " features inserted"
