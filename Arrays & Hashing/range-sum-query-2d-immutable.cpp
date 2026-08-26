class NumMatrix {
private:
    vector<vector<int>> ps;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        int rows = matrix.size();
        int cols = matrix[0].size();

        // Create prefix sum matrix of size (rows+1)x(cols+1), all 0s initially
        ps = vector<vector<int>>(rows + 1, vector<int>(cols + 1, 0));

        for (int r = 1; r <= rows; ++r) {
            for (int c = 1; c <= cols; ++c) {
                ps[r][c] = matrix[r - 1][c - 1]
                         + ps[r - 1][c]
                         + ps[r][c - 1]
                         - ps[r - 1][c - 1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return ps[row2 + 1][col2 + 1]
             - ps[row1][col2 + 1]
             - ps[row2 + 1][col1]
             + ps[row1][col1];
    }
};
