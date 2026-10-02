class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        # An empty string is always a subsequence. Generally people will miss condition.
        if s_len == 0:
            return True
        source = 0
        dest = 0
        # Use two pointers to compare characters in s and t.
        while source < s_len and dest < t_len:
            # If characters match, move to the next character in s.
            if s[source] == t[dest]:
                source += 1
            # Always move forward in t.
            dest += 1
        #     if source == s_len:
        #         return True
        # return False
        # If all characters in s were matched, s is a subsequence of t.
        return source == s_len


