//{ Driver Code Starts
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};


// } Driver Code Ends
/* Structure of the linked list node is as
struct Node 
{
    int data;
    struct Node* next;
    Node(int x) { data = x;  next = NULL; }
};
*/


class Solution{
  public:
    //Function to sort the given linked list using Merge Sort.
    Node* merge(Node *left, Node *right)
    {
        if (!left)
        {
            return right;
        }
        if (!right)
        {
            return left;
        }
        
        Node *result = NULL;
        if (left -> data <= right -> data)
        {
            result = left;
            result -> next = merge(left -> next, right);
        }
        else
        {
            result = right;
            result -> next = merge(left, right -> next)
        }
        return result;
    }
    
    void split(Node *source, Node **front_ref, Node **back_ref)
    {
        Node *slow = source;
        Node *fast = source -> next;
        while (fast != NULL)
        {
            fast = fast -> next;
            if (fast != NULL)
            {
                slow = slow -> next;
                fast = fast -> next;
            }
        }
        *front_ref = source;
        *back_ref = source -> next;
        slow -> next = NULL;
    }
    Node* mergeSort(Node** head_ref) 
    {
        Node *head = head_ref;
        if (head == NULL || head -> next == NULL)
        {
            return;
        }
        
        Node *front = NULL;
        Node *back = NULL;
        split (head, &front, &back);
        mergeSort(&front);
        mergeSort(&back);
        *head_ref = merge(front, back);
        // your code here
    }
};


//{ Driver Code Starts.

void printList(Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

void push(struct Node** head_ref, int new_data) {
    Node* new_node = new Node(new_data);

    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

int main() {
    long test;
    cin >> test;
    while (test--) {
        struct Node* a = NULL;
        long n, tmp;
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            push(&a, tmp);
        }
        Solution obj;
        a = obj.mergeSort(a);
        printList(a);
    }
    return 0;
}
// } Driver Code Ends