#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    int Q;
    int cc = 0;
    while(cin >> N && ++cc) {
        cin >> Q;
        vector<int> data(N);
        for(int i = 0; i < N; i++) {
            cin >> data[i];
        }
        if (!Q)
            continue;
        sort(data.begin(), data.end());
        cout << "CASE# " << cc << ":\n";
        for (int i = 0; i < Q; i++) {
            int q;
            cin >> q;
            auto it = lower_bound(data.begin(), data.end(), q);
            if (*it == q)
                cout << q << " found at " << it - data.begin() + 1 << '\n';
            else
                cout << q << " not found\n";
        }
    }
}
