class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            n = len(s)
            encoded_string += str(n)
            encoded_string += "#"
            encoded_string += s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        i = 0
        while i < len(s):
            word = ""
            count = ""
            while s[i] != '#':
                count += s[i]
                i += 1

            count = int(count)

            while count > 0:
                i += 1
                word += s[i]
                count -= 1
            
            decoded_strs.append(word)
            i += 1

        return decoded_strs
