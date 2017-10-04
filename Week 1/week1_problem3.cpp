// ACM @ UCI
// Week 1 Problem 3
// Unique Paths II (https://leetcode.com/problems/unique-paths-ii)
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        
        if(n == 0)
            return 0;
        
        int m = obstacleGrid[0].size();
        
        vector<vector<int> > d(n, vector<int>(m));
        
        d[0][0] = 1;
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                        
                if(obstacleGrid[i][j]){
                    d[i][j] = 0;
                    continue;
                }
                
                if (i - 1 >= 0)
                    d[i][j] += d[i-1][j];
                if (j - 1 >= 0)
                    d[i][j] += d[i][j-1];      
            }
        }
        return d[n-1][m-1];
    }
};