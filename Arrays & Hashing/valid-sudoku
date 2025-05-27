class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Use 9 maps for rows, cols, and boxes
        unordered_map<char, int> row[9];
        unordered_map<char, int> col[9];
        unordered_map<char, int> box[9];

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.') continue;

                // Calculate box index
                int boxIndex = (r / 3) * 3 + (c / 3);

                // Check row, col, and box
                if (++row[r][val] > 1 || ++col[c][val] > 1 || ++box[boxIndex][val] > 1) {
                    return false;
                }
            }
        }
        return true;
    }
};
