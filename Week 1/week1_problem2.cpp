// ACM @ UCI
// Week 1 Problem 2
// Unique Paths (https://leetcode.com/problems/unique-paths)
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int> > d(n, vector<int>(m));
        
        for(int i = 0; i < n; i++)
            d[i][0] = 1;
        for(int j = 0; j < m; j++)
            d[0][j] = 1;
        
        for(int i = 1; i < n; i++)
            for(int j = 1; j < m; j++)
                d[i][j] = d[i-1][j] + d[i][j-1];
        
        return d[n-1][m-1];
    }
};
