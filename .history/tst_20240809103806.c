#include <stdio.h>

struct data{
    int x;
}

int main() {
    char word[] = "hello";
    for (int i = 0; i < sizeof(word); i++) {
        printf("%c\n", word[i]);
    }
}