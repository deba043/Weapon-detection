import os
path = '/home/hp/Desktop/all_knife_ache/knife_ache_waale_7'
files = os.listdir(path)


for index, file in enumerate(files):
	os.rename(os.path.join(path, file), os.path.join(path, ''.join(['knife'+str(index+245), '.jpg'])))
