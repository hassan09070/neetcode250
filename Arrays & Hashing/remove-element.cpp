class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int back = nums.size() - 1;
        for (int i = 0; i <= back; ) {
            if (nums[i] == val) {
                // Swap with the back
                int temp = nums[back];
                nums[back] = nums[i];
                nums[i] = temp;
                back--; // shrink the usable array
                // do NOT increment i, we need to check the new nums[i]
            } else {
                i++; // valid value, move forward
            }
        }
        return back + 1; // size of the array excluding val
    }
};
