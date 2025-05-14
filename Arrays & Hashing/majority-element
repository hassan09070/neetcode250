class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> freq;
        int n = nums[0];
        int f = 1;
        for (int num : nums) {
            freq[num]++;
            if(freq[num] > f){
                n = num;
                f= freq[num];
            }
        }
        return n;
    }
};
