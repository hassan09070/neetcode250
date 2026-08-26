class Solution {
public:

    string encode(vector<string>& strs) {
        string output;
        for (string& s : strs) {
            output += to_string(s.length()) + "#" + s;
        }
        return output;
    }

    vector<string> decode(string s) {
    vector<string> output;
    int i = 0;

    while (i < s.length()) {
        // 1. Parse number until '#'
        int j = i;
        while (s[j] != '#') j++;

        int len = stoi(s.substr(i, j - i));  // convert number string to int

        // 2. Get the word of length `len`
        string word = s.substr(j + 1, len);

        // 3. Add to output and move i forward
        output.push_back(word);
        i = j + 1 + len;
    }

    return output;
}
};
