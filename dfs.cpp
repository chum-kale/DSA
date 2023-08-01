#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <map>

using namespace std;

void dfs(vector<vector<int>>& graph, int start) 
{
    int n = graph.size();
    vector<bool> visited(n, false);
    stack<int> s;
    
    s.push(start);
    visited[start] = true;

    while (!s.empty())
    {
        int current = s.top();
        s.pop();
        cout << current << " ";

        for (int neigh : graph[current])
        {
            if(!visited[neigh])
            {
                s.push(neigh);
                visited[neigh] = true;
            }
        }
    }
}

int main() {
    int n = 5; // Number of nodes in the graph
    vector<vector<int>> graph(n);

    // Adding edges to the graph (Undirected graph)
    graph[0].push_back(1);
    graph[0].push_back(4);
    graph[1].push_back(0);
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(4);
    graph[2].push_back(1);
    graph[2].push_back(3);
    graph[3].push_back(1);
    graph[3].push_back(2);
    graph[3].push_back(4);
    graph[4].push_back(0);
    graph[4].push_back(1);
    graph[4].push_back(3);

    int startNode = 0; // Start node for DFS
    cout << "DFS traversal starting from node " << startNode << ": ";
    dfs(graph, startNode);
    cout << endl;

    return 0;
}