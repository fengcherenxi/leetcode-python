class Solution {
    public boolean isMatch(String s, String p) {
        if (s==null || p==null)
            return false;
        int m = s.length();
        int n = p.length();
        boolean[][] dp = new boolean[m+1][n+1];// 设置二维布尔数组的空间大小
        dp[0][0]=true;// 设置初始条件
        for (int i=0;i<n;i++){//设置边界条件
            // p是匹配对象
            //如果p的第i+1个字符也就是p.charAt(i)是"*"的话,
            //那么他就可以把p的第i个字符给消掉(也就是匹配0次)。
            //我们只需要判断p的第i-1个字符和s的前0个字符是否匹配即可。比如p是"a*b*",如果要判断p的第4个字符
            //"*"和s的前0个字符是否匹配,因为字符"*"可以消去前面的任意字符,只需要判断p的"a*"和s的前0个字符是否匹配即可
            if (p.charAt(i) == '*' && dp[0][i - 1]) {
                dp[0][i + 1] = true;
            }
        }
        for (int i=0;i<m;i++){
            for (int j=0; j<n; j++){
                if (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.'){
                    dp[i+1][j+1]=dp[i][j];
                }else if (p.charAt(j)=='*'){
                    //递推公式
                    if (p.charAt(j-1)==s.charAt(i)||p.charAt(j-1)=='.'){
                        dp[i+1][j+1]=dp[i][j+1];
                    }
                    dp[i + 1][j + 1] |= dp[i + 1][j - 1];
                }
            }
        }
        return dp[m][n];
    }
}