import time
k = 1
while k>=1:
	init_time = time.time()
	k = time.time() - init_time
	while k<1:
		k = time.time() - init_time
	else:
		print(int(time.time()))
	
	
	