# 19948 음유시인 영재

def make_shorter(temp_words):
    words = temp_words[0]
    for idx in range(1, len(temp_words)):
        if temp_words[idx] == words[-1]:
            continue
        words += temp_words[idx]
        
    return words


words = list(input().split())
space_bar = int(input())
alpha = list(map(int, input().split()))

between_space = len(words) - 1

title = [word[0].upper() for word in words]
real_title = ''.join(title)
title = make_shorter(title)
words = ' '.join(words).upper()
words = make_shorter(words)

# 제목 숫자 세기
for tit in title:
    idx = ord(tit) - ord('A')
    alpha[idx] -= 1
    if alpha[idx] < 0:
        real_title = -1
    break
    
# 스페이스바 숫자 세기
if between_space > space_bar:
    real_title = -1
    
# 본문 세기
if real_title != -1:
    for word in words:
        if word == ' ':
            continue
        idx = ord(word) - ord('A')
        alpha[idx] -= 1
        if alpha[idx] < 0:
            real_title = -1
            break

print(real_title)
