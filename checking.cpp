#include <iostream>
using namespace std;
int main(){
    int x=2,y=2,z;
    z=x++;
    y=++z;
    x -= y-- + --z;
    y +=x+z--;

    x=(y>z)?z:y;
    cout<<"\n x="+ x;
    cout<<"\n y="+ y;
    cout<<"\n z="+ z;
    return 0;
}