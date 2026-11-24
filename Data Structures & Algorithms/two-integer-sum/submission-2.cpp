class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> seen;

        for (int i = 0; i < n; i++) {
            int comp = target - nums[i];
            if (seen.contains(comp)) {
                return {seen[comp], i};
            }
            seen[nums[i]] = i;
        }

        return {};
    }
};
