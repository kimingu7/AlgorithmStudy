#include<iostream>
#include<algorithm>
#include<vector>
#include<list>
#include<ctime>

#define MaxAge 140

using namespace std;

// 연결 리스트 구현

struct tree{
    int x;
    int y;
    tree* next;
    tree* prev;
    tree() :x(0), y(0), next(nullptr), prev(nullptr) { }
}tr[10000000];

int cnt;

tree* getNewTree(int x = 0, int y = 0, tree* pv = nullptr) {
    tree* ret = &tr[cnt++];
    ret->x = x;
    ret->y = y;
    ret->prev = pv;
    ret->next = nullptr;
    return ret;
}

struct tree_list {
    tree* head;
    tree* tail;
    int size;

    void clear(){
        head = getNewTree();
        tail = head;
        size = 0;
    }

    void push(tree* temp) {
        tail->next = temp;
        temp->prev = tail;
        tail = temp;
        size++;
    }
};

int N, M, K;
int delta[8][2] = { {-1,-1}, {-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1} };

int nourishment[11][11] = { 0, };   // 겨울에 추가되는 양분 양
int food[11][11];                   // 땅에 남아있는 양분 양
int temp[11][11] = { 0, };          // 죽은 나무 양분 양
tree_list List[MaxAge+1];           // 나이마다 나무를 저장

void spring() {
    for (int i = 1; i <= MaxAge; i++) {
        if (List[i].head->next == nullptr) continue;

        auto iter = List[i].head->next;
        while (iter != nullptr) {
            if (food[iter->x][iter->y] < i) {
                temp[iter->x][iter->y] += (i / 2);
                List[i].size--;

                if (iter->next == nullptr) {
                    iter->prev->next = nullptr;
                }
                else {
                    iter->next->prev = iter->prev;
                    iter->prev->next = iter->next;
                }

                iter = iter->next;
            }
            else {
                food[iter->x][iter->y] -= i;
                iter = iter->next;
            }
        }
    }

    for (int i = MaxAge; i >= 0; i--) {
        List[i + 1].head = List[i].head;
        List[i + 1].tail = List[i].tail;
        List[i + 1].size = List[i].size;
    }
    List[0].clear();
}

void summer() {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            food[i][j] += temp[i][j];
            temp[i][j] = 0;
        }
    }
}

void fall() {
    int nx, ny;
    for (int i = 5; i <= MaxAge; i += 5) {
        if (List[i].head->next == nullptr) continue;
        auto iter = List[i].head->next;
        while (iter != nullptr) {
            for (int k = 0; k < 8; k++) {
                nx = iter->x + delta[k][0];
                ny = iter->y + delta[k][1];
                if (nx < 1 || nx > N || ny < 1 || ny > N) continue;
                List[1].push(getNewTree(nx, ny, List[1].tail));
            }

            iter = iter->next;
        }
    }
}

void winter() {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            food[i][j] += nourishment[i][j];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int x, y, z;

    cin >> N >> M >> K;

    cnt = 0;

    for (int i = 0; i <= MaxAge; i++) {
        List[i].head = getNewTree();
        List[i].tail = List[i].head;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> nourishment[i][j];
            food[i][j] = 5;
        }
    }

    for (int i = 0; i < M; i++) {
        cin >> x >> y >> z;
        List[z].push(getNewTree(x, y, List[z].tail));
    }

    clock_t start, end;
    start = clock();
    for (int i = 1; i <= K; i++) {
        if (i == 100) {
            i = 100;
        }
        //start = clock();
        spring();
        //end = clock();
        //cout << i << "번째 해 봄   " << end - start << "ms\n";

        //start = clock();
        summer();
        //end = clock();
        //cout << i << "번째 해 여름 " << end - start << "ms\n";

        //start = clock();
        fall();
        //end = clock();
        //cout << i << "번째 해 가을 " << end - start << "ms\n";

        //start = clock();
        winter();
        //end = clock();
        //cout << i << "번째 해 겨울 " << end - start << "ms\n";
    }
    end = clock();
    //cout << end - start << "ms\n";
    int ans = 0;
    for (int i = 0; i < 110; i++) {
        ans += List[i].size;
    }
    cout << ans;
    return 0;
}