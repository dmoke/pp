#https://www.codewars.com/kata/58b57f984f353b3dc9000030/solutions
"""
Your task is to generate a palindrome string, using the specified length n, 
the specified characters c(all characters in c must be used at least once),
and the code length should less than: python 55 characters javascript 62 characters
"""


# def palindrome(n,c):return(n-len(c)*2)//2*"a"+c+"a"+c[::-1]+(n-len(c)*2)//2*"a"
# def palindrome(n,c):return(c[:n//2]+c[:n//2][::-1]).center(n,"$")



# def test(n,c):
#     if n % 2 ==0 :
#         return(n-len(c)*2)//2*"a"+c+c[::-1]+(n-len(c)*2)//2*"a"
    
#     return(n-len(c)*2)//2*"a"+c+"a"+c[::-1]+(n-len(c)*2)//2*"a"



# # no odd numbers

# def main():
#     # print(palindrome(20, 'EbccFR'))
#     # print(palindrome(20, 'EbccFR').__len__())

#     # print(palindrome(21, 'EbccFR'))
#     # print(palindrome(21, 'EbccFR').__len__())

#     # print(test(20, 'EbccFR'))
#     # print(test(20, 'EbccFR').__len__())

#     # print(test(21, 'EbccFR'))
#     # print(test(21, 'EbccFR').__len__())
#     return

# if __name__ == "__main__":
#     main() 


# #######################################################
# def palindr0me(n,c):return(c+c[::-1][1:])[:n].center(n,"$")
# # def palindr0me(n,c):return(c+c[::-1][n%2:n]).center(n,'$')
# # def palindr0me(n,c):return(c+"$"+c[::-1]).center(n,"$")


# print(palindr0me(20, 'EbdcFR'))


palindrome=lambda n,с:(с+с[-1-с%2::-1]).center(n,"$")
