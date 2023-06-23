#include<iostream>
#include<vector>
#include<unordered_set>
#include<queue>
#include<set>
#include <windows.h>

using namespace std;

pair<int,int> start(); 
void draw(set<pair<int,int>>);

string start_point = "O";
string end_posint = "X";

vector<vector<string>> maze ={
    {"#", "O", "#", "#", "#", "#", "#", "#", "#"},
    {"#", " ", " ", " ", " ", " ", " ", " ", "#"},
    {"#", " ", "#", "#", " ", "#", "#", " ", "#"},
    {"#", " ", "#", " ", " ", " ", "#", " ", "#"},
    {"#", " ", "#", " ", "#", " ", "#", " ", "#"},
    {"#", " ", "#", " ", "#", " ", "#", " ", "#"},
    {"#", " ", "#", " ", "#", " ", "#", "#", "#"},
    {"#", " ", " ", " ", " ", " ", " ", " ", "#"},
    {"#", " ", " ", " ", " ", "#", "#", " ", "#"},
    {"#", " ", "#", " ", " ", "#", " ", " ", "#"},
    {"#", " ", "#", " ", " ", "#", " ", " ", "#"},
    {"#", " ", "#", " ", " ", "#", " ", " ", "#"},
    {"#", " ", "#", " ", " ", "#", " ", " ", "#"},
    {"#", " ", " ", " ", " ", " ", " ", " ", "#"},
    {"#", "#", "#", "#", "#", "#", "#", "X", "#"}
 };

set<pair<int,int>> ans;

int main(){
    queue<pair<pair<int,int>,set<pair<int,int>>>> que;
    set <pair<int,int>> visits;
    pair<int,int> start_pair = start(); 
    set<pair<int,int>> vic;
    vic.insert(start_pair);
    pair<pair<int,int>,set<pair<int,int>>> new_pair = make_pair(start_pair, vic);
    que.push(new_pair);

    vector<pair<int,int>> dir = {{1,0},{0,1},{-1,0},{0,-1}};
    
    while (que.size() > 0)
    {
        pair<pair<int,int>,set<pair<int,int>>> pose = que.front();
        set<pair<int,int>> vics;
        vics = pose.second;
        pair<int,int> pos;
        pos = pose.first;
        draw(vics);
        if (maze[pos.first][pos.second] == end_posint){
            ans = vics;
            break;
        }
        que.pop();
        for (int i = 0; i < dir.size(); i++){
            pair<int,int> pa = dir[i];
            int newrow = pa.first + pos.first; 
            int newcol = pa.second + pos.second;
            pair<int,int> rowcol = make_pair(newrow, newcol);
            if (newrow >= 0 && newrow < maze.size() && newcol >= 0 && newcol < maze[0].size() && maze[newrow][newcol] != "#" && visits.count(rowcol) == 0){
                vics.insert(rowcol);
                que.push(make_pair(rowcol,vics));
                visits.insert(rowcol);
            }
        }
    }

}


pair<int,int>start(){

    for (int i = 0; i < maze.size();i++){
        for (int j = 0; j < maze[i].size();j++){
            if (maze[i][j] == start_point){
                return make_pair(i,j);
            }
        }
    }
}

void draw(set<pair<int,int>> path){
    system("cls");
    for (int i = 0; i < maze.size(); i++){  
        for(int j = 0; j < maze[i].size(); j++)
        {
            if(path.count(make_pair(i,j)) == 0){
 
                cout << maze[i][j] << "  ";
                cout << " ";
            }
            else{
                cout << "&" << "  ";
                cout << " ";
            }
        }
        cout << " ";
        cout << endl;
        }
    Sleep(200);
}
