class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
    
        rows = [''] * numRows
        direction = 1  # Direction of movement: 1 (down) or -1 (up)
        row = 0
    
        for char in s:
            rows[row] += char
            row += direction
        
        # Change direction when reaching the first or last row
            if row == 0 or row == numRows - 1:
                direction *= -1
    
        return ''.join(rows)
