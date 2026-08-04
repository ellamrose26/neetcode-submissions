class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        dict1 = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in "({[":
                check.append(ch)
            else:
                if len(check) ==0:
                    return False
                
                #remove the most recent bracket
                last = check.pop()

                if last != dict1[ch]:
                    return False
        return len(check) ==0