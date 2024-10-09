word1 = "test"
word2 = "testing"

if len(word1) % 2 == 0:
	print(word1[len(word1)//2-1]+word1[len(word1)//2])
else: print(word1[len(word1)//2])

if len(word2) % 2 == 0:
	print(word2[len(word2)//2-1],word2[len(word2)//2])
else: print(word2[len(word2)//2])

