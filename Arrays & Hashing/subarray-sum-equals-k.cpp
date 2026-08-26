class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixSums;
        prefixSums[0] = 1; // To handle the case when sum == k
        int sum = 0, count = 0;

        for (int num : nums) {
            sum += num;

            // Check if there is a previous prefix sum so that current_sum - previous = k
            if (prefixSums.count(sum - k)) {
                count += prefixSums[sum - k];
            }

            // Store the current sum in the map
            prefixSums[sum]++;
        }

        return count;
    }
};
