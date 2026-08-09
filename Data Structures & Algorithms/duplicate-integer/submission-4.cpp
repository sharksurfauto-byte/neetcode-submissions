#include <unordered_set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> hashed;
        
        for (int n : nums) {
            // .count() returns 1 if present, 0 if not
            if (hashed.count(n)) { 
                return true;
            }
            hashed.insert(n);
        }
        
        return false;
    }
};