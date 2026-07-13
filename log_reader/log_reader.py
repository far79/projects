# /home/mm/projects/log_reader/logs

with open("/home/mm/projects/log_reader/logs","r") as file:
	lines = file.readlines()
	lines_counts= len(lines)

i=0
while i<=lines_counts-1:
	log = lines[i]

	log_finder = log.find("|")#for first "|"
	date = log[:log_finder]


	log1 = log[log_finder+2:]#for second "|"
	log1_finder = log1.find("|")
	info = log1[:log1_finder]


	log2 = log1[log1_finder+2:]
	log2_finder = log2.find("|")
	type = log2[:log2_finder]


	log3 = log2[log2_finder+2:]
	log3_finder = log3.find("|")
	status=log3[:log3_finder]
	

	log4 = log3[log3_finder+2:]
	latency=log4

	print(date, info, type, status, latency)
	i+=1
