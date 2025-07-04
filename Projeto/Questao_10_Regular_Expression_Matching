class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Inicializa a tabela DP
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # A string vazia corresponde a um padrão vazio
        dp[0][0] = True
        
        # Tratar padrões como "a*" que podem corresponder a uma string vazia
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Preencher a tabela DP
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        return dp[len(s)][len(p)]
