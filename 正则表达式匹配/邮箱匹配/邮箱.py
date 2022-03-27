import re
f = open('邮箱匹配前文件.txt','r',encoding='utf-8')
text = f.readlines()
email =str(text)
trueemail =re.search(r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*',email)
print(trueemail)
f.close