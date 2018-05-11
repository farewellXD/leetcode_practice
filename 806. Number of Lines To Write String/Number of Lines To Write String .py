class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
#         line = 1
#         rest = 0
#         for i in S:
#             width = widths[ord(i) - ord('a')]
#             rest += width 
            
#         if  rest > 100:
#             line += 1
#             rest = width 
    
#         return [line, width]
        lines = 0
        cnt = 0
        for c in S:
            lc = widths[ord(c) - ord('a')]
            # cnt += lc
            
            if cnt + lc> 100:
                lines += 1
                cnt = lc
            else:
                cnt += lc
        return [lines + (cnt > 0), cnt]