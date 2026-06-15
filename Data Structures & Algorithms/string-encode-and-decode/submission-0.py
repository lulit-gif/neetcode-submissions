class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            length = len(word)
            result += str(length)
            result += "#"
            result += word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            j = i

            # find '#'
            while s[j] != "#":
                j += 1

            #get length
            length = int(s[i:j])

            #get word
            word_start = j + 1
            word_end = word_start + length
            word = s[word_start:word_end]

            result.append(word)

            #move pointer forward
            i = word_end
        return result
