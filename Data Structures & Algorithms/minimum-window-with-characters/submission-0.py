class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = have = 0
        required = len(need)
        ans = ""

        for right, c in enumerate(s):
            if c in need:
                need[c] -= 1
                if need[c] == 0:
                    have += 1

            while have == required:
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                c = s[left]
                if c in need:
                    need[c] += 1
                    if need[c] > 0:
                        have -= 1
                left += 1

        return ans