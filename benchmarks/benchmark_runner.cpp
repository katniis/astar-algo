#include <bits/stdc++.h>
#include <vector>
#include <utility>
#include "../lib/json.hpp"
#include "../algorithms/astar.h"
#include "../algorithms/bfs.h"
#include "../algorithms/dfs.h"
#include "../algorithms/dijkstra.h"

using namespace std;
using json = nlohmann::json;

// Get current memory usage in MB
double getMemoryUsage() {
    FILE* fp = fopen("/proc/self/status", "r");
    double vm = 0;
    if (fp) {
        char line[256];
        while (fgets(line, sizeof(line), fp)) {
            if (sscanf(line, "VmRSS: %lf", &vm) == 1) {
                fclose(fp);
                return vm / 1024.0; // Convert KB to MB
            }
        }
        fclose(fp);
    }
    return 0;
}

long long now() {
    return chrono::duration_cast<chrono::microseconds>(
        chrono::high_resolution_clock::now().time_since_epoch()
    ).count();
}

// measure path length safely
int path_length(vector<pair<int,int>>& path) {
    return path.empty() ? -1 : (int)path.size();
}

int main() {

    ifstream f("../data/testcases.json");
    json data;
    f >> data;

    vector<string> algorithms = {"bfs", "dfs", "dijkstra", "astar"};

    json results = json::array();

    for (auto& test : data["tests"]) {

        vector<vector<int>> grid = test["grid"]["cells"];

        pair<int,int> start = {
            test["start"][0], test["start"][1]
        };

        pair<int,int> goal = {
            test["goal"][0], test["goal"][1]
        };

        string test_name = test["metadata"]["test_name"];
        int size = test["metadata"]["size"];
        double density = test["metadata"]["density"];
        string category = test["metadata"]["category"];

        for (string algo : algorithms) {

            long long t1 = now();

            vector<pair<int,int>> path;

            if (algo == "bfs") path = bfs(grid, start, goal);
            else if (algo == "dfs") path = dfs(grid, start, goal);
            else if (algo == "dijkstra") path = dijkstra(grid, start, goal);
            else if (algo == "astar") path = astar(grid, start, goal);

            long long t2 = now();

            json entry;
            entry["test"] = test_name;
            entry["algorithm"] = algo;
            entry["size"] = size;
            entry["density"] = density;
            entry["category"] = category;
            entry["time_us"] = (t2 - t1);
            entry["time_ms"] = (t2 - t1) / 1000.0;
            entry["path_length"] = path_length(path);
            entry["success"] = !path.empty();

            results.push_back(entry);
        }
    }

    ofstream out("../data/results.json");
    out << results.dump(2);

    cout << "Benchmark completed -> results.json generated\n";

    return 0;
}