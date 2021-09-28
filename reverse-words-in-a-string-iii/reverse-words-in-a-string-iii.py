class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split(" ")
        b=""
        for i in range(len(str_list)-1):
            b+=str_list[i][::-1]+' '
        b+=str_list[len(str_list)-1][::-1]
        return b