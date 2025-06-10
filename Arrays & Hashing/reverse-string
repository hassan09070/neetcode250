class Solution {
public:
    void reverseString(vector<char>& s) {
        vector<char> copy = s;
        int len = s.size();
        int temp;
        for(int i =0; i < len/2; i++ ){
            temp = s[i];
            s[i]= s[len-i-1];
            s[len-i-1]=temp;
        }
    }
};
