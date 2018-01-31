# P4 Longest Palindromic substring

+ ## Reference websites:
	+ http://blog.csdn.net/hopeztm/article/details/7932245
+ Idea 1
	+ Dynamic Planning
		+ 最长回文子串 (LPS:Longest Palindromic Substring)
			+ dp[i][j] 表示从i到j的子串是否是回文子串
			+ 如果s[i] == s[j],那么是否为回文子串取决于 dp[i+1][i-1]
			+ 如果s[i] != s[j],那么dp[i][j] 直接false