class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {

        vector<int> output;
        unordered_map<int, int> feq;

        for (int num : nums){
            feq[num]++;
        }

        for (const auto& pair : feq) {
            
            if (pair.second > (nums.size()/3)){
                output.push_back(pair.first);
            }
        } 

        return output;
    }
};
