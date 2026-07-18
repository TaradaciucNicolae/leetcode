class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == "":
            return [[""]]
        rezultat = []
        dict_of_groups = defaultdict(list)


        for each_word in strs:
            amprenta_word = ""
            for _, each_letter in enumerate(each_word):
                amprenta_word = ''.join(sorted(each_word))

            
            dict_of_groups[amprenta_word].append(each_word)

        for valorile_din_dictionar in dict_of_groups.values():
                #print(valorile_din_dictionar)
                rezultat.append(valorile_din_dictionar)

        #print(dict_of_groups)
        return rezultat
