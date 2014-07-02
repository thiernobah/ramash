__author__ = 'root'

import sys, socket

"""
result =  socket.getaddrinfo(sys.argv[1], None)
count = 0
for item in result:

    print("%-2d: %s" %(count,item[4]))
    count+=1
"""

result = socket.gethostbyaddr(sys.argv[1])
print("host primaire %s" %result[1])

for item in result[2]:
    print(item)




