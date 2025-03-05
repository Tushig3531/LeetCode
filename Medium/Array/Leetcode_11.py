# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        L=0 #init left line
        R=len(height)-1 #init right line
        final_area=0 #this is what we are going to return
        while L<R: #while L<R, we gonna loop our algorithm, because if length of L becomes lower than R, there will be only one cause that is those lines are already passed each other. Because we are going to give condition that if Left is bigger  than R move the R's index else L's index. So there will not be any condition that L is gonna bigger than R. Therefore, it also talks about the index, if L is bigger than R, which means it is also passed.
            height_of_line=min(height[L],height[R]) #because we need the height of the line. The reason why I choosing min is because max must have other's min value. Else it will not become rectangular
            width=R-L
            area_of_water=height_of_line*width #simple math
            final_area=max(area_of_water,final_area) #it takes the max of the new areas and old areas

            if height[L]>height[R]: #moving index
                R-=1
            else:
                L+=1
        return final_area
        
        
height=[4,3,2,1,4]
print(maxArea(height))