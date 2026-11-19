class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            int f_m = nums[m];

            if (target == f_m) {
                return m;
            } else if (target < f_m) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return -1;
    }
};
