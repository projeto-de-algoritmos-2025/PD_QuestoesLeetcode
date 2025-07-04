class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Se a lista estiver vazia, a subsequência mais longa tem comprimento 0
        if not nums:
            return 0
        
        # Array dp onde dp[i] mantém o comprimento da LIS até o índice i
        dp = [1] * len(nums)  # Cada elemento é inicialmente uma subsequência de comprimento 1
        
        # Iterar sobre cada elemento no array nums
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # Se o número atual for maior que nums[j], pode formar subsequência crescente
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # O comprimento da maior subsequência será o máximo valor encontrado no dp
        return max(dp)
