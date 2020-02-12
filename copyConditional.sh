import os
import shutil

ids = range(1, 45566)
#ids
idsNeeded=list(filter(lambda x : x % 10 == 0, ids))
#idsNeeded
len(idsNeeded)
idsNeededEven=list(filter(lambda x : x % 20 == 0, idsNeeded))
#idsNeededEven
len(idsNeededEven)

datasetLocation = "/home/abishek/Downloads/driving_dataset"

i = 1
for root, dirs, files in os.walk("/home/abishek/Downloads/driving_dataset"):
	for file in files:
		print file[:-4]
		try:
			if int(file[:-4]) in idsNeededEven:
				print i+1
				i = i+1
				shutil.copy(os.path.join(datasetLocation,file),"/home/abishek/Downloads/driving_dataset_small")
		except:
			pass

print i
