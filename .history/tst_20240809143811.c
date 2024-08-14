#include <stdio.h>
#include <stdlib.h>

struct Node{
    int val;
    struct Node* next;
};

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

void printList(struct Node* head) {
    struct Node* current = head;

    while (current->next != NULL) {
        printf("%d->", current->val);
        current = current->next;
    }

    printf("%d", current->val);
}

int main() {
    struct Node* head = NULL;
    printf(&head);

    int num = 36;
    int* ptr = &num;
    printf("The value of num is %d\n", num); printf("The pointer address is %p\n", ptr); printf("This is the '&' before ptr %p", &ptr)
    // pass head by reference so that it can be modified
    insertAtHead(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);
    insertAtEnd(&head, 40);
    insertAtEnd(&head, 50);
 
    // Print the Linked List
    printf("Linked List: ");
    printList(head);
 
    return 0;
}