def isAnagram(s, t):
    return sorted(s)==sorted(t)
s=str(input())
t=str(input())
print(isAnagram(s, t))