class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            key = "".join(sorted(word))
            try:
                if len(dict[key]) >= 0:
                    dict[key].append(word)
            except KeyError:
                dict[key] = dict.get(key,[word])
        return [*dict.values()]