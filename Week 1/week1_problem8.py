# ACM @ UCI
# Week 1 Problem 8
# Largest Rectangle in Histogram (https://leetcode.com/problems/largest-rectangle-in-histogram/description/)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.insert(0,0) 
        heights.append(0)
		# ^just so I don't incur out of bounds errors^
        stack = [0] # put the first thing in the stack; stack keeps track of indices
        biggest_box = 0
		
		#keep track of the values with the property that every height in the list of 
		#heights before it until the next value in the stack is greater than it
        descended = set()
		
        for a in range(1,len(heights)): #O(n)
			# alg: if curr height is greater than the height at the top of the stack simply add it to stack.
			#      this gives stack the property that at any point a height is smaller than all the heights coming after it.
			#      this means that you can calculate area of the box from a value in the stack to the current index safely 
			#      (all the buildings in that range will be limited by the box you are looking at).
			#      if value is smaller you know that the rectangles prior will be limited by this box so start calculating 
			#      all the rectangles you can make using each height in the stack smaller than the current one. then add the 
			#      value to the descended set as this value has an interesting property in the stack(all the values after it 
			#      and until the one before it will be larger than it). Use that property to calculate the width of the 
			#      rectangle includeing that height. go through all values, 0 at the end I put in earlier will force a full 
			#      check of the stack as heights are all non-negative.
            if(heights[stack[-1]] > heights[a]):
                descended.add(a)
                while len(stack)>0 and stack[-1] != 0 and heights[stack[-1]] >= heights[a]: 
					# this loop will execute n times total as the rectangle made from the height of each thing put into the 
					# stack will be calculated only once (that's the point of the stack, things enter and leave once).
                    chk_ht_i = stack.pop(-1)
                    prev_i = stack[-1]
					# if value is descended then they have much larger width as popped previous values were also larger than it.
                    width = a-chk_ht_i if chk_ht_i not in descended else a-prev_i-1
					# each rectangle generated by the height is compared to the maximum
                    biggest_box = max(biggest_box,(width)*heights[chk_ht_i])
            stack.append(a)
            
        return biggest_box
    
    

                
