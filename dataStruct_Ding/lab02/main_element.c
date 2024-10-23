#include<stdlib.h>
#include<stdio.h>

void quickSort(int *nums, int left, int right);
int find_main_ele(int *nums, size_t size); 
int quickHelper(int *nums, int left, int right); 
// O(NlgN)
int find_main_ele(int *nums, size_t size) {
    // (1, 2, 3, 4, 5, 5, 5, 5, 5) 5 is Main element
    quickSort(nums, 0, (int)(size) - 1);
    int need = size / 2;
    for(int i = 0; i < size; i++) {
        if(i + need >= size) break;
        if(*(nums + i) == *(nums + i + need)) {
            return *(nums + i);
        }
    }
    return -1;
}
void quickSort(int *nums, int left, int right) {
    if(left >= right) return;
    int sen = quickHelper(nums, left, right);
    // sen get left and right
    quickSort(nums, left, sen - 1);
    quickSort(nums, sen + 1, right);
}
int quickHelper(int *nums, int left, int right) {
    int i = left; int j = right;
    while(i < j) {
        while(i < j && *(nums + j) >= *(nums + left)) j--;
        while(i < j && *(nums + i) <= *(nums + left)) i++;
        int tmp = *(nums + i);
        nums[i] = nums[j];
        nums[j] = tmp;
    } 
    // swap sen and i
    int tmp = *(nums + left);
    nums[left] = nums[i];
    nums[i] = tmp;
    return i;
}
int main() {
    int test[] = {0, 5, 5, 3, 5, 7, 5, 5};
    int *test1 = test;
    int test_num = 5;
    int res = find_main_ele(test1, 8);
    if(test_num != res) {
        for(int i = 0; i < 8; i++) {
            printf("%d ", test[i]);
        }
        printf("Not correct!, expected is %d, but get is %d\n", test_num, res);
        return 0;
    }
    for(int i = 0; i < 8; i++) {
        printf("%d ", test[i]);
    }
    printf("Test is passed!\n");
    return 0;
}