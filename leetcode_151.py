class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.split(' ',-1)) #按空格切分
        q=[] 
        for i in s[::-1]: #反向放在一个列表里，去掉空格，只留下单词和符号
            if i != '':
                q.append(i)
        return ' '.join(q)  #把列表里的单词用空格连接成一句话