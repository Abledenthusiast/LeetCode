class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        std::map<int, bool> visited;
        dfs(rooms, 0, visited);
        return visited.size() == rooms.size();
    }
    
    void dfs(vector<vector<int>>& rooms, int currRoom,  std::map<int, bool>& visited) {
        if(!visited[currRoom]) {
            visited[currRoom] = true;
            for (int i = 0; i < rooms[currRoom].size(); ++i) {
                dfs(rooms, rooms[currRoom][i], visited);
            }
        }
        return;
    }
};