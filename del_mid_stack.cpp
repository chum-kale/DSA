#include <iostream>
#include <stack>
using namespace std;

void del_mid (stack<int>& st, int mid)
{
    stack<int> temp;
    int cur = 0;
    while (!st.empty())
    {
        if (cur != mid)
        {
           temp.push(st.top());
           cur ++; 
        }

        if (cur = mid)
        {
            st.pop();
        }
        break;
    }
    while (!temp.empty())
    {
        st.push(temp.top());
    }
}

int main()
{
    stack<int> myStack;
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    myStack.push(40);
    myStack.push(50);

    int mid = myStack.size() / 2;
    del_mid(myStack, mid);
    while (!myStack.empty())
    {
        cout << myStack.top() << " ";
        myStack.pop();
    }   
    return 0;
}