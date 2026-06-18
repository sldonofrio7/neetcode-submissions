class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i

        return res


    def decode(self, s: str) -> List[str]:
        
        print("String:", s)
        
        res = []
        p1, p2 = 0, 0

        while p1 < len(s) - 1:
            temp, length = "", ""

            while s[p1].isdigit():
                length += s[p1]
                p1 += 1
            
            p2 = p1 + 1
            while p2 < p1 + int(length) + 1:
                temp += s[p2]
                p2 += 1

            p1 = p2
            res.append(temp)

        return res








