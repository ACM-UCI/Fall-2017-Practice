// ACM @ UCI
// Week 2 Warmup contest
// Millionaire Madness (Problem D @ https://open.kattis.com/contests/g8e7sa)

#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> > grid;
vector<vector<int> > visited;
int n,m;

void dfs(int i, int j, int lad){
    visited[i][j] = 1;
    int dx[] = { 0, 0, -1, +1};
    int dy[] = {-1, 1,  0,  0};

    for(int z = 0;z < 4; z++){
        int nx = i + dx[z];
        int ny = j + dy[z];

        if(nx < 0 || nx >= n)
            continue;
        if(ny < 0 || ny >= m)
            continue;
        if(visited[nx][ny])
            continue;

        if(grid[nx][ny] - grid[i][j] <= lad)
            dfs(nx, ny, lad);
    }
}

int main(){
    cin >> n >> m;
    grid = vector<vector<int> >(n, vector<int>(m));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> grid[i][j];
        }
    }

    int l = 0;
    int r = 1000*1000*1000 + 100;

    // Binary Search on Ladder Size
    while(r - l > 1){
        int mid = (r + l) / 2;
        visited = vector<vector<int> >(n, vector<int>(m));
        dfs(0, 0, mid);
        bool ok = (visited[n-1][m-1] == 1);

        if (ok)
            r = mid;
        else
            l = mid;

    }

    visited = vector<vector<int> >(n, vector<int>(m));
    dfs(0, 0, l);
    bool ok = (visited[n-1][m-1] == 1);

    if(ok)
        cout << l << endl;
    else
        cout << r << endl;

    return 0;
}
