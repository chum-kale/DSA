class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        temp = []
        for i in words:
            store = i.split(separator)
            temp = temp + store
        
        while "" in temp:
            temp.remove("")
        
        return temp