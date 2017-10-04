// ACM @ UCI
// Week 1 Problem 4
// Trapping Rain water (https://leetcode.com/problems/trapping-rain-water)
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() == 0)
            return 0;
        
        vector<int> l(height.size());
        vector<int> r(height.size());
        
        // Finding tallest to our left
        l[0] = height[0];
        for(int i = 1; i < height.size(); i++){
            l[i] = max(l[i-1], height[i]);
        }
        
        // Finding tallest to our right
        r[height.size()-1] = height[height.size()-1];
        for(int i = height.size()-2 ; i>=0; i--){
            r[i] = max(r[i+1], height[i]);
        }
        
        // Find how much water remains on top of each column and them add up
        int ans = 0;
        for(int i = 1;i < height.size()-1; i++){
            int num = min( l[i-1], r[i+1] ) - height[i]; 
            if(num > 0)
                ans += num; 
        }
        
        return ans;
    }
};
