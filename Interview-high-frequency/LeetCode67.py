# 二进制求和


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = a.__len__()
        b_len = b.__len__()
        i, j = a_len - 1, b_len - 1
        result = []
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            carry = 1 if sum > 1 else 0
            result.append(str(sum % 2))
        if carry == 1:
            result.append("1")
        result.reverse()
        return "".join(result)