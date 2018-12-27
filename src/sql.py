
ds = "features[1][i][0]"

for i in range(127):
	ds = ds + ",features[1][i]["+str(i+1)+"]"


print ds
