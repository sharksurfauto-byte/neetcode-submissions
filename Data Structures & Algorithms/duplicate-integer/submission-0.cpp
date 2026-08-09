class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        
        sort(nums.begin(), nums.end());
        
        // Loop to n-1 so i+1 is always valid
        for (int i = 0; i < (int)nums.size() - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                return true; // Found it! Exit early.
            }
        }
        
        return false;
    }
};