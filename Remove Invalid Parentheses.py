#User function Template for python3
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        # BFS
        queue = [s]
        visited = set()
        found = False
        result = []
        
        while queue:
            current = queue.pop(0)
            
            if self.isValid(current):
                found = True
                result.append(current)
                
            if found:
                continue
            
            for i in range(len(current)):
                if current[i] in {'(', ')'}:
                    new_str = current[:i] + current[i+1:]
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append(new_str)
        
        return result

    def isValid(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

