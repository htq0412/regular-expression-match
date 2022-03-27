import re
f = open('身份证号码匹配前文件.txt','r',encoding='utf-8')
text = f.readlines()
id =str(text)
trueId =re.search(r'[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]',id)
print(trueId)
f.close