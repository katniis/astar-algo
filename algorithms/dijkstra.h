#pragma once
#include <bits/stdc++.h>

using namespace std;

vector<pair<int,int>> dirs_dijkstra={{0,1},{1,0},{0,-1},{-1,0}};

struct Node_dijkstra{
    int x,y,cost;
};

struct cmp_dijkstra{
    bool operator()(Node_dijkstra a,Node_dijkstra b){
        return a.cost>b.cost;
    }
};

vector<pair<int,int>> dijkstra(vector<vector<int>>& grid,pair<int,int> start,pair<int,int> goal){
    int n=grid.size(),m=grid[0].size();

    priority_queue<Node_dijkstra,vector<Node_dijkstra>,cmp_dijkstra> pq;
    map<pair<int,int>,int> dist;
    map<pair<int,int>,pair<int,int>> parent;

    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            dist[{i,j}]=INT_MAX;

    dist[start]=0;
    pq.push({start.first,start.second,0});

    while(!pq.empty()){
        auto cur=pq.top();pq.pop();

        if(make_pair(cur.x,cur.y)==goal) break;

        for(auto d:dirs_dijkstra){
            int nx=cur.x+d.first;
            int ny=cur.y+d.second;

            if(nx<0||ny<0||nx>=n||ny>=m) continue;
            if(grid[nx][ny]==1) continue;

            int nd=cur.cost+1;

            if(nd<dist[{nx,ny}]){
                dist[{nx,ny}]=nd;
                parent[{nx,ny}]={cur.x,cur.y};
                pq.push({nx,ny,nd});
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
