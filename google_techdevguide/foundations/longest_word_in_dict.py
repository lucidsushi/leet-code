"""The Challenge
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
Learning objectives
This question gives you the chance to practice with algorithms and data structures. It’s also a good example of why careful analysis for Big-O performance is often worthwhile, as is careful exploration of common and worst-case input conditions.
"""


def find_longest_subsequence(s, d):
    longest = "0"
    for word in d:
        sub_word = is_subsequence(s, word)
        if sub_word and not len(sub_word) > len(longest):
            continue
        elif sub_word:
            longest = sub_word
    print("longest is", longest)
    return longest


def is_subsequence(s, word):
    word_index = 0
    for i in range(len(s)):
        try:
            if not word[word_index] == s[i]:
                continue
            else:
                word_index += 1
        except IndexError:
            return word


find_longest_subsequence("abppplee", {"able", "ale", "apple", "bale", "kangaroo"})
