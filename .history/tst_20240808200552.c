#include <stdio.h>

int main() {
    printf("This is cool\n");

    int num = 8;
    int* ptr = &num;
    printf("This pointer is %p", ptr);

    return 0;
}