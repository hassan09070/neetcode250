class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        sort(nums.begin(), nums.end());
        int cur = 1;
        int maxLen = 1;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                continue; // skip duplicate
            }
            else if (nums[i] == nums[i - 1] + 1) {
                cur++;
            } else {
                maxLen = std::max(maxLen, cur);
                cur = 1; // reset for new sequence
            }
        }

        return std::max(maxLen, cur); // check final sequence
    }
};
