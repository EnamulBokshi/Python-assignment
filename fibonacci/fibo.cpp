#include<iostream>
#include<vector>
using namespace std;
int nthFeboUtil(int n, vector<int> &memo){
    if(n<=1){
        return n;
    }
    if(memo[n] != -1){
        return memo[n];
    }
    memo[n] = nthFeboUtil(n-1,memo) + nthFeboUtil(n-2,memo);
    return memo[n];
}
int nthFibo(int n){
    vector<int>memo(n+1,-1);
    int result = nthFeboUtil(n,memo);
    for(auto it = memo.begin(); it != memo.end(); ++it) 
        cout<<*it<<" ";
    return result;
}
int main(){
    int n = 6;
    int result = nthFibo(n);
    cout<<result<<endl;
    return 0;
}