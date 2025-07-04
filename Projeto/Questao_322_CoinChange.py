class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Inicializa a tabela de DP com um valor grande (maior que qualquer número possível de moedas)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Para atingir a quantidade 0, precisamos de 0 moedas
        
        # Preenche a tabela de DP
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Se dp[amount] ainda for inf, significa que não foi possível atingir o valor
        return dp[amount] if dp[amount] != float('inf') else -1
