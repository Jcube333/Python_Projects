from collections import defaultdict

def groupAnagrams(lst):
    #  Similar to map, wherein the constructor papameter initalizes default empty list for each vale in the dictionary
 ans = defaultdict(list)
 for word in lst:
    str="".join(sorted(word))
    # Sorted(i) created a list of all elements in a sorted order and we're joining it to create a string out of it.

    ans[str].append(word)

 return ans

x = groupAnagrams(["eat","ate","Jcube333","333cubeJ","cubeJ333"])   

print(x)

