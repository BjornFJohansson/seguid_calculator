#include <stdio.h>
#include <string.h>

int smallest_rotation(char *s) {
    int n = strlen(s);
    int i = 0, j = 1, k = 0;
    while (i < n && j < n && k < n) {
        int cmp = s[(i+k)%n] - s[(j+k)%n];
        if (cmp == 0) {
            k++;
        } else {
            if (cmp > 0) {
                i = i + k + 1;
            } else {
                j = j + k + 1;
            }
            if (i == j) {
                j++;
            }
            k = 0;
        }
    }
    return i < j ? i : j;
}

int main() {
    char s[] = "duvalduval";
    int i = smallest_rotation(s);
    printf("Smallest rotation: %.*s%s\n", strlen(s)-i, s+i, s);
    return 0;
}
