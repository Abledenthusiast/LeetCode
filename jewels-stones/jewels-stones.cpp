class Solution {
public:
    int numJewelsInStones(string J, string S) {
        //build map
        std::map<char,int> jewels;
        int res = 0;
        for (int i = 0; i < J.length(); ++i) {
            jewels[J[i]] = 1;
        }
        for (int i = 0; i < S.length(); ++i) {
            if (jewels[S[i]] != NULL) {
                res++;
            }
        }
        return res;
    }
};