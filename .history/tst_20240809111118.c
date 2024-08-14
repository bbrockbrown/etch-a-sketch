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

void insertAtHead(struct Node** head, int val) {

    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->val = val;
    newNode->next = *head;

    *head = newNode;
}

void insertAtEnd(struct Node** head, int val) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->val = val;
    newNode->next = NULL;

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    struct Node* current = *head;

    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;
}

void printList(struct Node** head) {
    struct Node* current = *head;

    while (current->next != NULL) {
        printf("%d->", current->val);
        current = current->next;
    }

    printf("%d", current->val);
}