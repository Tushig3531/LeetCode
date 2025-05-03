# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
# A building is covered if there is at least one building in all four directions: left, right, above, and below.
# Return the number of covered buildings.
# Example 1:
# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
# Output: 1
# Explanation:
# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.
# Example 2:
# Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
# Output: 0
# Explanation:
# No building has at least one building in all four directions.
# Example 3:
# Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
# Output: 1
# Explanation:
# Only building [3,3] is covered as it has at least one building:
# above ([1,3])
# below ([5,3])
# left ([3,2])
# right ([3,5])
# Thus, the count of covered buildings is 1.


def countCoveredBuildings(n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        row_min={}
        row_max={}
        column_min={}
        column_max={}
        for x,y in buildings:
            if x not in row_min:
                row_min[x]=row_max[x]=y
            else:
                row_min[x]=min(row_min[x],y)
                row_max[x]=max(row_max[x],y)
            if y not in column_min:
                column_min[y]=column_max[y]=x
            else:
                column_min[y]=min(column_min[y],x)
                column_max[y]=max(column_max[y],x)
        covered=0
        for x,y in buildings:
            if row_min[x]<y<row_max[x] and column_min[y]<x<column_max[y]:
                covered+=1
        return covered
            
        
        
        # x_axis=[]
        # for x,y in buildings:
        #         x_axis.append(x)
        # # return x_axis,y_axis
        # hashmap_x={}
        # for x in x_axis:
        #     hashmap_x[x]=hashmap_x.get(x,0)+1
        
        # # return hashmap_x
        # for axis,count in hashmap_x.items():
        #     if count 
            
        
        
        
n = 3
buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
print(countCoveredBuildings(n,buildings))