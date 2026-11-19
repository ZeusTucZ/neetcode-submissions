class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0, r = matrix.size() - 1;
        int m;
        bool found = false;

        while (l <= r) {
            m = (l + r) / 2;
            int sub_left = matrix[m][0], sub_right = matrix[m][matrix[m].size() - 1];

            if (sub_left <= target && target <= sub_right) {
                found = true;
                break;
            } else if (target < sub_left) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        if (found == false) {
            return false;
        }

        l = 0, r = matrix[m].size() - 1;

        while (l <= r) {
            int sub_m = (l + r) / 2;
            int f_m = matrix[m][sub_m];

            if (target == f_m) {
                return true;
            } else if (target > f_m) {
                l = sub_m + 1;
            } else {
                r = sub_m - 1;
            }
        }

        return false;
    }
};
