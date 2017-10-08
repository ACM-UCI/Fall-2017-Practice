#include <bits/stdc++.h>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> answer;
    unordered_map<int, int > hash;
    for (int i = 0; i < nums.size(); i++){
        hash[nums[i]] = i;
    }

    for (int i = 0; i < nums.size(); i++){
        const auto it = hash.find(target - nums[i]);
        if (it != hash.end() && it->second != i) {
            answer.push_back(i);
            answer.push_back(it->second);
            break;
        }
    }
    return answer;
}

int main() {
    int n, target;
    vector<int> nums(n);

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> nums[i];
    cin >> target;
    vector<int> answer = twoSum(nums,target);
    cout << answer[0] << ' ' << answer[1] << '\n';
}
