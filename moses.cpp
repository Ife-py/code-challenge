#include <iostream>
using namespace std;
int main(){
    int input;
    cout<<"enter number from range 0 to 20"<<endl;
    cin >> input;
    if (input >= 0 && input <= 20){
        cout<<"the  result expected is "<< (input + 17);
    } else {
        cout <<"ERROR" <<" ENTER NUMBER WITHIN RANGE"<<endl;
        // cout<<"enter number from range 0 to 20:";
        // cin >> input;
        // cout<<"the  result expected is "<< (input + 17);
        main();
    }
    return 0;
}
