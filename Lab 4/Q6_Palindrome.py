def palindrome(s):
    i=0
    j=len(s)-1
    while(i<j) :
        if(s[i]!=s[j]): return False
        else:
            i+=1
            j-=1
    return True
print('It\'s Parindrome') if palindrome(input('Enter a String: ')) else print('In\'s Not Palindrome')