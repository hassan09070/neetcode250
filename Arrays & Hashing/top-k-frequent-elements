class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int num:nums ){
            freq[num]++;
        }
        vector<int>output ;
        for(int i=0;i<k;i++){
            int n;
            int max = 0;
            for (int num : nums){
                 if (freq[num] > max){
                    max = freq[num];
                    n = num;
                 } 
            }
            freq.erase(n);
            output.push_back(n);
        }

        return output;

        
    }
};
