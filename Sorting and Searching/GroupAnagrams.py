
import collections
def groupAnagrams(s):
    lookup = collections.defaultdict(list)

    for word in s:
        lookup[''.join(sorted(word))].append(word)

    result = []
    for key in lookup:
        result.extend(lookup[key])

    return result


print(groupAnagrams(['dog','red','edr','odg','god']))
