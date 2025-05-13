class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        std::string prefix = strs[0];

        for (int i = 1; i < strs.size(); i++) {
            std::string temp = "";
            for (int j = 0; j < prefix.size() && j < strs[i].size(); j++) {
                if (prefix[j] == strs[i][j]) {
                    temp += prefix[j];
                } else {
                    break;
                }
            }
            prefix = temp;
            if (prefix.empty()) return "";
        }

        return prefix;
    }
};
