class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 开始读时row[0]
        # 向后读row逐渐+1
        # 向前转折时row逐渐-1
        if numRows==1 or numRows>=len(s):
            return s
        zigzig = ['' for x in range(numRows)]
        row,step = 0,1

        for i in s:
            zigzig[row]+=i

            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row+=step
        return ''.join(zigzig)
