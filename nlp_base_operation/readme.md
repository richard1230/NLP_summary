# 思路

### 动态规划

我们要求的两个字符串的编辑距离，可以从两个字符串的子串的编辑距离得到。

设 D(i,j) D(i,j)D(i,j) 为 word1 前i个字符和 word2 前j个字符的编辑距离。

那么有递推关系式
--------------------- 
$$
D(i, j)=\min \left\{\begin{array}{l}{D(i-1, j)+1} \\ {D(i, j-1)+1} \\ {D(i-1, j-1)+\left\{\begin{array}{l}{0, \quad \text { word } 1(i)==\operatorname{word} 2(j)} \\ {1, \quad \text { else }}\end{array}\right.}\end{array}\right.
$$

我们要求的是 D(m,n) D(m,n)D(m,n)，其中 m 和 n 分别为 word1 和 word2 的长度。

这样，最终会将 D 构成一个m∗n m*nm∗n的二维矩阵，从左上角开始，从上到下从左到右开始遍历，最后到右下角为止。右下角的值即为所求。

注意：在遍历之前，需要先对矩阵进行初始化
$$
\left\{\begin{array}{ll}{D(i, 0)=i,} & {i=1, \ldots, m} \\ {D(0, j)=j,} & {j=1, \ldots, n}\end{array}\right.
$$
即：一个非空字符串和一个空字符串的编辑长度，就等于非空字符串的长度。

本算法时间复杂度为 O(mn)。


原文：https://blog.csdn.net/happyrocking/article/details/86491042 
