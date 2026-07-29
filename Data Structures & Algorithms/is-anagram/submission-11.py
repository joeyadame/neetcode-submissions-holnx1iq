class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = []
        t_hash = []

        for char in sorted(s):
            count = s.count(char)
            s_hash.append(count)
        for char in sorted(t):
            count = t.count(char)
            t_hash.append(count)
        
        return (s_hash) == (t_hash) and sorted(s) == sorted(t)
            