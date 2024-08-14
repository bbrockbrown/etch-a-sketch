#include <stdio.h>
#include <stdlib.h>

struct Node{
    int val;
    struct Node* next;
};

int main() {
    char word[] = "hello";
    char word = "h";
}

void insert(struct Node** head, int val) {

    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->val = val;
    newNode->next = *head;

    *head = newNode;
}

