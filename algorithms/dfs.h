#pragma once
#include <bits/stdc++.h>

using namespace std;

vector<pair<int,int>> dirs_dfs = {{0,1},{1,0},{0,-1},{-1,0}};

bool dfsUtil(vector<vector<int>>& grid, int x, int y,
             pair<int,int> goal,
             vector<vector<int>>& vis,
             map<pair<int,int>, pair<int,int>>& parent){

    if(make_pair(x,y)==goal) return true;

    vis[x][y]=1;

    for(auto d:dirs_dfs){
        int nx=x+d.first, ny=y+d.second;

        if(nx<0||ny<0||nx>=(int)grid.size()||ny>=(int)grid[0].size()) continue;
        if(grid[nx][ny]==1||vis[nx][ny]) continue;

        parent[{nx,ny}] = {x,y};

        if(dfsUtil(grid,nx,ny,goal,vis,parent))
            return true;
    }

    return false;
}

vector<pair<int,int>> dfs(vector<vector<int>>& grid, pair<int,int> start, pair<int,int> goal){
    vector<vector<int>> vis(grid.size(), vector<int>(grid[0].size(),0));
    map<pair<int,int>, pair<int,int>> parent;

    dfsUtil(grid,start.first,start.second,goal,vis,parent);

    if(!parent.count(goal)&&start!=goal) return {};

    vector<pair<int,int>> path;
    auto cur=goal;

    while(cur!=start){
        path.push_back(cur);
        cur=parent[cur];
    }
    path.push_back(start);
    reverse(path.begin(),path.end());

    return path;
}
