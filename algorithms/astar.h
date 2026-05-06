#pragma once
#include <bits/stdc++.h>

using namespace std;

vector<pair<int,int>> dirs_astar={{0,1},{1,0},{0,-1},{-1,0}};

int h(pair<int,int>a,pair<int,int>b){
    return abs(a.first-b.first)+abs(a.second-b.second);
}

struct Node_astar{
    int x,y,g,f;
};

struct cmp_astar{
    bool operator()(Node_astar a,Node_astar b){
        return a.f>b.f;
    }
};

vector<pair<int,int>> astar(vector<vector<int>>& grid,pair<int,int> start,pair<int,int> goal){
    int n=grid.size(),m=grid[0].size();

    priority_queue<Node_astar,vector<Node_astar>,cmp_astar> pq;
    map<pair<int,int>,int> g;
    map<pair<int,int>,pair<int,int>> parent;

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            g[{i,j}]=INT_MAX;

    g[start]=0;
    pq.push({start.first,start.second,0,h(start,goal)});

    while(!pq.empty()){
        auto cur=pq.top();pq.pop();

        if(make_pair(cur.x,cur.y)==goal) break;

        for(auto d:dirs_astar){
            int nx=cur.x+d.first;
            int ny=cur.y+d.second;

            if(nx<0||ny<0||nx>=n||ny>=m) continue;
            if(grid[nx][ny]==1) continue;

            int ng=cur.g+1;

            if(ng<g[{nx,ny}]){
                g[{nx,ny}]=ng;
                parent[{nx,ny}]={cur.x,cur.y};
                pq.push({nx,ny,ng,ng+h({nx,ny},goal)});
            }
        }
    }

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
