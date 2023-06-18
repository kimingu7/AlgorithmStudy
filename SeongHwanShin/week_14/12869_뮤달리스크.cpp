#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int dp[61][61][61] = { 0, };

// 중복 계산 방지를 위한 dp 배열
int func(int a, int b, int c) {
    if (a < 0)return func(0, b, c);
    if (b < 0)return func(a, 0, c);
    if (c < 0)return func(a, b, 0);

    if (a == 0 && b == 0 && c == 0) return 0;

    if (dp[a][b][c] != 999)return dp[a][b][c];

    dp[a][b][c] = min(dp[a][b][c], func(a - 9, b - 3, c - 1) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 9, b - 1, c - 3) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 3, b - 9, c - 1) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 3, b - 1, c - 9) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 1, b - 3, c - 9) + 1);
    dp[a][b][c] = min(dp[a][b][c], func(a - 1, b - 9, c - 3) + 1);

    return dp[a][b][c];
}



int N;
int main() {
    cin >> N;
    for (int i = 0; i < 61; i++) {
        for (int j = 0; j < 61; j++) {
            for (int k = 0; k < 61; k++) {
                dp[i][j][k] = 999;
            }
        }
    }

    vector<int> scv;
    for (int i = 0; i < N; i++) {
        int hp;
        cin >> hp;
        scv.push_back(hp);
    }
    cout << func(scv[0], scv[1], scv[2]) << '\n';


    return 0;
}