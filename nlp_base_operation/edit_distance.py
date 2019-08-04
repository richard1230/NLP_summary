# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')




def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    动态规划。
    """
    m = len(word1)
    n = len(word2)
    # 初始化，D(i,0)=i, D(0,j)=j
    D = [[0] * (n+1) for _ in range(m+1)]
    D[0] = [i for i in range(n+1)]
    for i in range(m+1):
        D[i][0] = i
    # 迭代
    for i in range(1,m+1):
        for j in range(1,n+1):
            tmp1 = min(D[i-1][j], D[i][j-1]) + 1
            tmp2 = D[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)
            D[i][j] = min(tmp1, tmp2)
    return D[m][n]

if '__main__' == __name__:
    # word1 = "intention"
    word1 = input('please input the first string:')
    word2 = input('please input the second string:')
    print(minDistance(word1, word2))
