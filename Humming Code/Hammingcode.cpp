#include<bits/stdc++.h>
using namespace std;

int main(){
    cout<<"Enter data bits: ";
    string s; cin>>s;
    int d = s.length();
    int r = log2(d);

    while((1<<r) < d+r+1)
        r++;
    int l = d+r;
    cout<<"Data Lenght: "<<d<<"\nRedundant length: "<<r<<"\nTotal length: "<<l<<endl;

    int pos = 0;
    int humming[l+1];
    //Generate humming code with all redundant bit = 0
    for(int i=1; i<=l; ++i){
        if(log2(i) == (int)log2(i))
            humming[i-1] = 0;
        else{
            humming[i-1] = s[pos]-'0';
            ++pos;
        }
    }
    cout<<"Humming code without generating redundant bit: \n";
    for(int i=0; i<l; ++i) cout<<humming[i]<<" ";
    cout<<endl;
    //redundant bit generation
    for(int i=1; i<=l; ++i){
        if(log2(i)==(int)log2(i)){
            cout<<"Calculate redundant bit "<<i<<":\n";
            int idx = i-1;
            int parity = 0;

            while(idx<l){
                for(int j=0; j<i; ++j){
                    if(idx>=l) break;
                    if(humming[idx]==1) ++parity;
                    cout<<idx+1<<"th bit is "<<humming[idx]<<endl;
                    idx++;
                }
                for(int j=0; j<i; ++j){
                    if(idx>=l) break;
                    idx++;
                }
            }
            humming[i-1] = parity%2;
            cout<<"The "<<i<<"th redundant bit is "<<parity%2<<endl;
        }
    }
    cout<<"Humming code: ";
    for(int i=0; i<l;++i) cout<<humming[i]<<" ";
    return 0;
}
