# There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.
# Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.
# Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.
# Example 1:


# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
# Example 2:

# Input: wall = [[1],[1],[1]]
# Output: 3

def leastBricks(wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counts={}
    
        for row in wall:
            prefix=0
            for brick in row[:-1]:
                prefix+=brick
                if prefix in counts:
                    counts[prefix]+=1
                else:
                    counts[prefix]=1
        max_edge=0
        for count in counts.values():
            if count>max_edge:
                max_edge=count
        return len(wall)-max_edge            
        
        
        
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(leastBricks(wall))
        