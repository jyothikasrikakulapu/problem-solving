//FIND THE ORIGINAL TYPED STRING
class Solution:
    def possibleStringCount(self, word):
        from itertools import groupby

        groups = ["".join(group) for _, group in groupby(word)]
        result_set = set()
        result_set.add(word)

        start = 0
        for group in groups:
            end = start + len(group)
            if len(group) > 1:
                for i in range(1, len(group)):
                    new_group = group[:len(group) - i]
                    new_word = word[:start] + new_group + word[end:]
                    result_set.add(new_word)
            start = end

        return len(result_set)
