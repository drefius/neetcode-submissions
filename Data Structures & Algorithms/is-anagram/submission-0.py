class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lista_1 = list(s)
        lista_2 = list(t)
        lista_1.sort()
        lista_2.sort()
        return lista_1 == lista_2