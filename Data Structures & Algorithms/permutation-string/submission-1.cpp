class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.size(), n2 = s2.size();
        if (n1 > n2) {
            return false;
        }

        unordered_map<char, int> count_s1;
        unordered_map<char, int> count_s2;
        for (int i = 0; i < n1; i++) {
            count_s1[s1[i]]++;
        }

        int l = 0, r = n1 - 1;
        for (int x = l; x <= r; x++) {
            if (count_s1.find(s2[x]) != count_s1.end()) {
                count_s2[s2[x]]++;
            }
        }

        while (r < n2) {
            if (count_s1 == count_s2) {
                return true;
            }

            r++;
            if (count_s1.find(s2[r]) != count_s1.end()) {
                count_s2[s2[r]]++;
            }

            if (count_s1.find(s2[l]) != count_s1.end()) {
                count_s2[s2[l]]--;
            }
            l++;
        }

        return false;
    }
};
