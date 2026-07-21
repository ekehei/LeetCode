def isPalindrome(x)->bool:
    a=[]
    if x<0:
        return False
    if x==0:
        return True
    while(x!=0):
        a.append(x%10)
        x//=10
    for j in range(0,len(a)):
        if a[j]!=a[len(a)-1-j]:
            return False
    return True

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))