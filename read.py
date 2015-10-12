#读取文件一行
#!/usr/bin/python
f=open('/etc/hosts')
line=f.readline()
print line,
f.close()

#读取整个文件
#!/usr/bin/python
import sys
f=open('/etc/hosts')
for line in f:
  print line,
f.close()

#!/usr/bin/python
for i in open('/etc/hosts'):
  print i,