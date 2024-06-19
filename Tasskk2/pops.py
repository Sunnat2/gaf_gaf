#include <iostream>
using namespace std

int main() {
int n;
count<<"Enter how many integers: "; 
cin>>n;
int num[n];
for(int i = 0; i<n; i++)
{
    cout <<"Enter integer"<<(i + 1)<<":";
    cin>> num[i];
}

cout << endl << endl << "Integers" << endl;
for(int i = 0; i < n; i++)
{
    cout<<num[i]<<" ";
}

return 0;

}