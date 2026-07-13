log = "2026-07-13 14:02:15 | ERROR | /api/login | 500 | 104ms"

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
