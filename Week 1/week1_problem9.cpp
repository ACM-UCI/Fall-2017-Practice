// ACM @ UCI
// Week 1 Problem 9
// Search in Rotated Sorted Array (https://leetcode.com/problems/search-in-rotated-sorted-array)
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if(nums.size() == 0)
            return -1;
        // will use a customized binary search
        return pivot(nums, 0, nums.size()-1, target);
    }
    
    
    // in range [l, r]
    int pivot(vector<int>& nums, int l, int r, int target){
        if (l > r)
            return -1;
        
        // base case
        if (l == r || l == r - 1){
            if(nums[l] == target)
                return l;
            else if(nums[r] == target)
                return r;
            else
                return -1;
        }
        
        int mid = (l + r) / 2;
        
        if(nums[mid] < nums[r]){
            if (target >= nums[mid] && target <= nums[r])
                return pivot(nums, mid, r, target);
            else
                return pivot(nums, l, mid, target);
        }
        else
        {
            if (target >= nums[l] && target <= nums[mid])
                return pivot(nums, l, mid, target);
            else
                return pivot(nums, mid, r, target);
        }
        
    }
    
};
