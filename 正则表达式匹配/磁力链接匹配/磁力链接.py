import re
f = open('磁力链接匹配前文件.txt','r',encoding='utf-8')
text = f.readlines()
magnet =str(text)
truemagnet =re.search(r'(magnet:\?xt=urn:btih:)[0-9a-fA-F]{40}.*',magnet)
print(truemagnet)
f.close