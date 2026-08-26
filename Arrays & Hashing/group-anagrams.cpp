class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    
        std::unordered_map<std::string, std::vector<std::string>> anagramGroups;

        
        for (const std::string& word : strs) {
            std::string sortedWord = word;
            std::sort(sortedWord.begin(), sortedWord.end());
            anagramGroups[sortedWord].push_back(word);
        }

        
        std::vector<std::vector<std::string>> result;
        for (const auto& pair : anagramGroups) {
            result.push_back(pair.second);
        }
        return result;
    } 
};
