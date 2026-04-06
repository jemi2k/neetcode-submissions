class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            #find len
            j = i
            while s[j] != "#":
                j += 1
            leng = int(s[i:j])

            #extract word

            word = s[j+1 : j+1+leng]
            result.append(word)

            #update pointer
            i = j + 1 + leng

        return result




