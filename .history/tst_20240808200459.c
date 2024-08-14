#include <stdio.h>

int main() {
    printf("This is cool");

    int num = 8;
    int* ptr = &num;
    printf(ptr);

    return 0;
}