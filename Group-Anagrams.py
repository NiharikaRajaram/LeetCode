class Solution:
    def calculate_prime_product(self, word, primes):
        product = 1
        for char in word:
            product *= primes[ord(char) - ord('a')]
        return product
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == None or len(strs) == 0:
            return []
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        anagram_map = {}
        
        for word in strs:
            product = self.calculate_prime_product(word, primes)
            
            if product not in anagram_map:
                anagram_map[product] = []
            anagram_map[product].append(word)
        
        return anagram_map.values()
