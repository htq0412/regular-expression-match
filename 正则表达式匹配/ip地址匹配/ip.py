import re
f = open('ip地址匹配前文件.txt','r',encoding='utf-8')
text = f.readlines()
ip =str(text)
trueIp =re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',ip)
print(trueIp)
f.close