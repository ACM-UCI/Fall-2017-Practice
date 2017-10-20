#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int N, M;
        if (matrix.size() == 0) return false;
        N = matrix.size();
        M = matrix[0].size();
        long long low, high;
        low = 0; high = N * M - 1;

        while (low <= high) {
            long long mid = (low + high) / 2;
            if (matrix[mid/M][mid%M] == target) return true;
            else if (matrix[mid/M][mid%M] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
    }
};


int main(){
    int N, M;
    cin >> N >> M;
    vector<vector<int> > table(N);
    for (int i = 0; i < N; i++){
        table[i].resize(M);
        for (int j = 0; j < M; j++) {
            cin >> table[i][j];
        }
    }
    int t;
    cin >> t;
    Solution solution;
    cout << solution.searchMatrix(table, t) << '\n';
}


