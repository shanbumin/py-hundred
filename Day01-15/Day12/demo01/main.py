# 字符串常用操作


print('My brother\'s name is \'007\'') # 转义字符
print(r'My brother\'s name is \'007\'') # 原始字符串
# -------------------------------------------------------
str = 'hello123world'
print('he' in str) #True
print('her' in str) #False
print(str.isalpha()) # 字符串是否只包含字母  False
print(str.isalnum()) # 字符串是否只包含字母和数字 True
print(str.isdecimal()) # 字符串是否只包含数字 False
print(str[0:5].isalpha()) #True
print(str[5:8].isdecimal()) #True
# ------------------------------------------------------------------
list = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('-'.join(list)) #床前明月光-疑是地上霜-举头望明月-低头思故乡
#----------------------------------------------
sentence = 'You go your way I will go mine'
words_list = sentence.split()
print(words_list) #['You', 'go', 'your', 'way', 'I', 'will', 'go', 'mine']
#----------------------------------------------

email = '     jackfrued@126.com          '
print(email)
print(email.strip())
print(email.lstrip())

