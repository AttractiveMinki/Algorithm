"""
시간에 민감한 일부 백준 문제에서 readline이 필요한 경우가 있다.

다음 코드를 사용하면, 추가적인 변경 없이 readline을 사용할 수 있다.

참고로
input = sys.stdin.readline()
위와 같이 쓰면, TypeError가 발생한다.

"""

import sys

input = sys.stdin.readline
