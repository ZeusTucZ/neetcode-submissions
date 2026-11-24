class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int n = piles.size();
        int max_value = *max_element(piles.begin(), piles.end());

        int l = 1, r = max_value;
        int k = max_value;
        while (l <= r) {
            int m = l + (r - l) / 2;

            long long count = 0;
            for (int i = 0; i < n; i++) {
                count += ceil((double) piles[i] / m);
            }

            if (count <= h) {
                k = min(k, m);
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return k;
    }
};
