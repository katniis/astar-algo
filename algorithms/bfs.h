#pragma once
#include <bits/stdc++.h>

using namespace std;

vector<pair<int,int>> dirs_bfs = {{0,1},{1,0},{0,-1},{-1,0}};

vector<pair<int,int>> bfs(vector<vector<int>>& grid, pair<int,int> start, pair<int,int> goal) {
    int n = grid.size(), m = grid[0].size();

    queue<pair<int,int>> q;
    map<pair<int,int>, pair<int,int>> parent;
    vector<vector<int>> vis(n, vector<int>(m,0));

    q.push(start);
    vis[start.first][start.second] = 1;

    while(!q.empty()) {
        auto cur = q.front(); q.pop();

        if(cur == goal) break;

        for(auto d: dirs_bfs){
            int nx = cur.first + d.first;
            int ny = cur.second + d.second;

            if(nx<0||ny<0||nx>=n||ny>=m) continue;
            if(grid[nx][ny]==1||vis[nx][ny]) continue;

            vis[nx][ny]=1;
            parent[{nx,ny}] = cur;
            q.push({nx,ny});
        }
    }

    if(!parent.count(goal) && start!=goal) return {};

    vector<pair<int,int>> path;
    pair<int,int> cur = goal;

    while(cur != start){
        path.push_back(cur);
        cur = parent[cur];
    }
    path.push_back(start);
    reverse(path.begin(), path.end());

    return path;
}
