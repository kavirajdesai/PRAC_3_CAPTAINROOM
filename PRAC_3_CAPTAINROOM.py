"""KAVIRAJ DESAI 20CE023"""
# taking input for k
k=int(input())
# input for room list
s=map(int,input().split())
# sorting the list
s=sorted(s)

for i in range(len(s)):
    if(i!=len(s)-1):
      if(s[i]!=s[i-1] and s[i]!= s[i+1]):
          print(s[i])
          break
    else:
         print(s[i])