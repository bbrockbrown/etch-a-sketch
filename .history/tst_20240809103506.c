#include <stdio.h>

int main() {
    printf("This is cool\n");
    char word[] = "hello";
    for (int i = 0; i < sizeof(word); i++) {
        printf("%c", word[i]);
    }
}