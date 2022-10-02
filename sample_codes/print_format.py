## print 형식 ##

my_str = '나의 문자열'

## 안녕하세요! 문자열: 나의 문자열
# 1. %s
print("안녕하세요! 문자열: %s" % (my_str))

# 2. .format
print("안녕하세요! 문자열: {}".format(my_str))

# 3. f-string
print(f"안녕하세요! 문자열: {my_str}")
