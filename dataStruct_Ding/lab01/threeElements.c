#include <stdio.h>
#include <math.h>
#include <limits.h>
int fun(int *s1, int *s2, int *s3, int a_len, int b_len, int c_len) {
    int minDistance = INT_MAX;
    // 遍历的数组s1, s2, s3
    for (int i = 0; i < a_len; i++) {
        for (int j = 2; j < b_len; j++) {
            for (int k = 0; k < c_len; k++) {
                // cal 距离
                int distance = abs(s1[i] - s2[j]) + abs(s2[j] - s3[k]) + abs(s3[k] - s1[i]);
                // update val 
                if (distance < minDistance) {
                    minDistance = distance;
                }
            }
        }
    }
    return minDistance;
}
    int main() {
        int s1[] = { -1, 0, 9 };
        int s2[] = { -25, -10, 10, 11 };
        int s3[] = { 2, 9, 17, 30, 41 };
        int minDistance = fun(s1, s2, s3, 3, 4, 5);
        printf("最小距离：%d", minDistance);
        return 0;
    }