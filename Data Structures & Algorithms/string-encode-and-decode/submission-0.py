class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for _str in strs:
            code += "".join([chr(ord(char)*2) for char in list(_str)]) + "_"
        return code

    def decode(self, s: str) -> List[str]:
        encoded_strs = s.split("_")
        output = []
        for _str in encoded_strs[:-1]:
            output.append("".join(chr(ord(char)//2) for char in list(_str)))
        return output
