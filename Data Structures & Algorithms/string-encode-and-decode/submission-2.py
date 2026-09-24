class Solution:

    def encode(self, strs: List[str]) -> str:
        hashed_str = "||".join(strs)
        if len(strs) == 0: return "empty"
        return hashed_str
        
    def decode(self, s: str) -> List[str]:
        if s == "empty": return []
        decoded_list = s.split("||")
        return decoded_list