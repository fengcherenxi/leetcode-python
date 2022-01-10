class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # 根据paths得到每个相邻的节点
        d = [[] for _ in range(N)]
        # 将大节点放到前面
        for i in paths:
            n,m = max(i),min(i)
            d[n-1].append(m)# 得到每一个节点对应的相应的节点，且索引按照节点值对应
        s={1,2,3,4}# 使用Python内置的集合存储可选的4种颜色
        # 每次从可选的4种颜色中去掉相邻花园的颜色，然后取最小值
        res = [1]*N# 为结果初始化矩阵
        #print(res)
        for i in range(N):
            used = {res[j-1] for j in d[i]}
            if not used:continue
            res[i] = sorted(s-used)[0]# 集合相减，在直接转换为排序列表
        return res
