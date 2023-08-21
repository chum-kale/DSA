//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h> 
using namespace std; 

struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};

void printList(Node* node) 
{ 
    while (node != NULL) { 
        cout << node->data%10; 
        node = node->next; 
    }  
    cout<<"\n";
} 


// } Driver Code Ends
//User function template for C++

/* 

struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
};

*/

class Solution
{
    public:
    Node* addOne(Node *head) 
    {
        // Your Code here
        Node *curr = head;
        Node *next = NULL;
        Node *prev = NULL;
        while (curr != NULL)
        {
            next = curr -> next;
            curr -> next = prev;
            prev = curr;
            curr = next;
        }
        
        Node *current = prev;
        int carry = 1;
        while (current != NULL && carry != 0)
        {
            int sum = current->data + carry;
            carry = sum / 10;
            current->data = sum % 10;
            current = current->next;
        }

        curr = prev;
        prev = NULL;
        while (curr != NULL)
        {
            next = curr -> next;
            curr -> next = prev;
            prev = curr;
            curr = next;
        }
        
        if (carry)
        {
            Node *newNode = new Node(carry); 
            newNode->next = prev;
            prev = newNode;
        }
        
        return prev;
        
        
        // return head of list after adding one
    }
};

//{ Driver Code Starts.

int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        
        Node* head = new Node( s[0]-'0' );
        Node* tail = head;
        for(int i=1; i<s.size(); i++)
        {
            tail->next = new Node( s[i]-'0' );
            tail = tail->next;
        }
        Solution ob;
        head = ob.addOne(head);
        printList(head); 
    }
    return 0; 
} 

// } Driver Code Ends