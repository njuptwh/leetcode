class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        x = -1 #初始化一个位置选择变量
        while True:
            a=[] #用于收集当前位置，各个字符串的字符
            x+=1 #推进到下一个位置
            for s in strs: #本循环用于生成当前位置，各字符串对应字符组成的列表
                if s[x:x+1] != '':
                    a.append(s[x:x+1])
                else:
                    return strs[0][0:x] #如果某个字符串已经没有字符了，则直接返回上一次循环的结果
            if len(set(a)) != 1: #如果本位置字符不相同，则跳出循环，上个位置已经是最长公共前缀
                return strs[0][0:x]
sss = Solution()
s= ['flower','flow','floweq']
sss.name = Solution.longestCommonPrefix(sss,s)
print(sss.name)