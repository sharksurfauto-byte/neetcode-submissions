#include <unordered_map>
#include <vector>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        
        for (int n : nums) {
            // If the count is already > 0, we've seen it before
            if (counts[n] > 0) {
                return true;
            }
            counts[n]++;
        }
        
        return false;
    }
};