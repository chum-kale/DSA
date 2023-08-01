#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <map>
#include <queue>

using namespace std;

void bfs(vector<vector<int>>& graph, int start)
{
    int n = graph.size();
    vector<bool> visited(n, false);
    queue<int> q;

    q.push(start);
    visited[start] = true;

    while (!q.empty())
    {
        int current = q.front();
        q.pop();
        cout << current <<" ";
        for (int neigh : graph[current])
        {
            if (!visited[neigh])
            {
                q.push(neigh);
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
    cout << "BFS traversal starting from node " << startNode << ": ";
    bfs(graph, startNode);
    cout << endl;

    return 0;
}