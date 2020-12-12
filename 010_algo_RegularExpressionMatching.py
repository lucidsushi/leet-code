import pytest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
        # '.' Matches any single character.
        # '*' Matches zero or more of the preceding element.

        # Conditions
        # The matching should cover the entire input string (not partial)
        # s could be empty and contains only lowercase letters a-z.
        # p could be empty and contains only lowercase letters a-z, and characters like . or *

        # matching is done when:
        #     pattern is depleted and no strings left (all matched)
        #     pattern is depleted but strings are left (not all matched)
        #     pattern is NOT depleted but no strings are left (not all matched)
        if not p:
            return (
                not s
            )  # p all used up, all matched if s all used up (not False = True), else not all matched

        # how about when p is depleted before s? <-- means match should fail

        # what is a match

        # only match '.'

        s_is_empty = bool(s)  # s could be empty
        if s_is_empty and p[0] in {s[0], "."}:
            return self.isMatch(s[1:], p[1:])
        else:
            return False


def test_match_cases():
    assert Solution().isMatch("ab", ".b") == True
    # assert solution.isMatch('ab', '.*') == True
    # assert solution.isMatch('ab', '.*c') == False
    # assert solution.isMatch('ab', '.*.') == True
    # assert solution.isMatch('aa', 'aa*a') == True
    # assert solution.isMatch('aaa', 'ab*a*c*a') == True


pytest.main()
# python3 -m pytest 010_algo_RegularExpressionMatching.py
