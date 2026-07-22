class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        while i < len(chars):
            ch = chars[i]
            count = 0

            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1

            chars[k] = ch
            k += 1

            if count > 1:
                for digit in str(count):
                    chars[k] = digit
                    k += 1

        return k