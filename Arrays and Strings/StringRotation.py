
# TIME - O(m + n)
# SPACE - O(n)

class KMP:

	def createlookupArray(self,s):
		lookup = [0] * len(s)
		j = 0
		for i in range(1,len(s)):
			if s[j] == s[i]:
				lookup[i] = j + 1
				j += 1
				i += 1
			elif i == 0:
				i += 1
			else:
				j = lookup[j-1]
		return lookup
			

	def KMPsearch(self,text,substring):
		lookupArray = self.createlookupArray(substring)
		j = 0
		while i < len(text) and j < len(substring):
			if text[i] == substring[j]:
				i += 1
				j += 1
			else:
				if j == 0:
					i += 1
				else:
					j = lookupArray[i-1]
			if j == len(substring):
				return True
		return False

	def stringRotation(self,s1,s2):
		text = s2 + s2
		return self.KMPsearch(text,s1)
		
		
if __name__ == "__main__":
	obj = KMP()
	print(obj.stringRotation('waterbottle','erbottlewat'))
