#��ȡ�ļ�һ��
#!/usr/bin/python
f=open('/etc/hosts')
line=f.readline()
print line,
f.close()

#��ȡ�����ļ�
#!/usr/bin/python
import sys
f=open('/etc/hosts')
for line in f:
  print line,
f.close()

#!/usr/bin/python
for i in open('/etc/hosts'):
  print i,