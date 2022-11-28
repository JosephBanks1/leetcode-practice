class Solution:
    def isPalindrome(self, x: int) -> bool:
        #establish empty place for nums to go
        reverse_num = ''
        num_str = str(x)

        #take in a number
        for i in range(0, len(num_str)):
        #convert to str

        #reverse number
            reverse_num = num_str[i] + reverse_num
        #compare reversed number to orig
        if reverse_num == num_str:
        #return bool
            print (True)
        else:
            print (False)

