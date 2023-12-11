#include <iostream>
using namespace std;
int main(){
    int input;
    cout<<"enter number from range 0 to 20"<<endl;
    cin >> input;
    if (input > 20){
        cout <<"ERROR" <<" ENTER NUMBER WITHIN RANGE"<<endl;
        cout<<"enter number from range 0 to 20:";
        cin >> input;
        cout<<"the  result expected is "<< (input + 17);
    }
    else if (input <= 20){
        cout<<"the  result expected is "<< (input + 17);
    }
    return 0;
}