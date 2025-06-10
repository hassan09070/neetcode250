class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
       sort(nums.begin(), nums.end());
       int min = 1 ;
        for (int num : nums){
            if (num == min ) {
                min++;
            }
        }
        return min;
    }
};
