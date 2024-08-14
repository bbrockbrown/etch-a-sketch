#include <stdio.h>

int main() {
    printf("This is cool\n");

    int num = 8;
    int* ptr = &num;
    printf("This pointer is %p", ptr);
    printf("\nThis is what happens when we ask for the mem add. of the ptr %p", &ptr);

    return 0;
}