class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int n = tokens.size();
        stack<string> st;

        for (int i = 0; i < n; i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                st.push(tokens[i]);
                continue;
            }

            string a_s = st.top();
            int a = stoi(a_s);
            st.pop();

            string b_s = st.top();
            int b = stoi(b_s);
            st.pop();

            if (tokens[i] == "+") {
                st.push(to_string(b + a));
            } else if (tokens[i] == "-") {
                st.push(to_string(b - a));
            } else if (tokens[i] == "/") {
                st.push(to_string(b / a));
            } else {
                st.push(to_string(b * a));
            }
        }

        return stoi(st.top());
    }
};
