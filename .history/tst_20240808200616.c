#include <stdio.h>

int main() {
    printf("This is cool\n");

    int num = 8;
    int* ptr = &num;
    printf("This pointer is %p", ptr, "Whereas the actual value using the pointer is", *ptr);

    return 0;
}