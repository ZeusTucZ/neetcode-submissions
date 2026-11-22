class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();

        vector<pair<int, int>> st;
        for (int i = 0; i < n; i++) {
            pair<int, int> car = {position[i], speed[i]};
            st.push_back(car);
        }

        sort(st.rbegin(), st.rend());

        vector<float> times;
        for (int i = 0; i < n; i++) {
            int a = st[i].first;
            int b = st[i].second;
            float time = (target - a) / (float) b;
            times.push_back(time);
        }

        float maxTime = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (times[i] > maxTime) {
                count++;
                maxTime = times[i];
            }
        }

        return count;
    }
};
