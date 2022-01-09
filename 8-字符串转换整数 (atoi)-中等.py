import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2**31-1    
        INT_MIN = -2**31
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则,对于小数采用向下取整的方式,^符号表示限定在开头
        num = num_re.findall(str)   #查找匹配的内容，findall()方法用于在整个字符串中搜索所有符合正则表达式的字符串,并以列表的形式返回
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值
