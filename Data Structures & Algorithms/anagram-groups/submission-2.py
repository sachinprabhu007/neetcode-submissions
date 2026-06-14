from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = character frequency tuple
        # value = list of words with that frequency
        res = defaultdict(list)

        for s in strs:
            # Count letters a-z
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            # Convert list to tuple so it can be a dictionary key
            res[tuple(count)].append(s)

        return list(res.values())