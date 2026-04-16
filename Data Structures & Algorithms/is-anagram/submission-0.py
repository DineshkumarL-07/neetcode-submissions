class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = Counter(s)
        hashMap2 = Counter(t)

        return hashMap1 == hashMap2