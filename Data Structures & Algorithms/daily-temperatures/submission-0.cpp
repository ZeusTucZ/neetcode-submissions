class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res(n, 0);
        stack<pair<int, int>> stack;

        for (int i = 0; i < n; i++) {
            pair<int, int> p = {i, temperatures[i]};
            while (!stack.empty() && stack.top().second < temperatures[i]) {
                int index = stack.top().first;
                int value = stack.top().second;
                stack.pop();

                res[index] = i - index;
            }
            stack.push(p);
        }

        return res;
    }
};
