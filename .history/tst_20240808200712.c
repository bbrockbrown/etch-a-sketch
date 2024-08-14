#include <stdio.h>

int main() {
    printf("This is cool\n");

    int num = 8;
    int* ptr = &num;
    printf("This pointer is %p", ptr);
    printf("Whereas the actual value using the pointer is %d", *ptr);

    return 0;
}