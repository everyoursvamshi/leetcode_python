class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs)==1:
            return [[strs[0]]]
        result_map = {}
        for value in strs:
            #strs[i] consists of lowercase English letters.
            alpha_list = [0]*26
            for letter in value:
                alpha_list[ord(letter)-ord('a')]+=1
            # word =""
            # i = 0
            # for count in alpha_list:
            #     if count >0:
            #         word=word+chr(i+ord('a'))+chr(count)
            #     i+=1
            word = tuple(alpha_list)
            # if word in result_map:
            #     result_map[word].append(value)
            # else:
            #     result_map[word]=[value]
            result_map.setdefault(word, []).append(value)
        #result = [x for x in result_map.values()]
        return list(result_map.values())
