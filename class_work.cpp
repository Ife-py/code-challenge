#include <iostream>

using namespace std;

int main() {
    int no;
    int valCount = 0;
    
    cout << "Enter an integer: "<<endl;
    cin >> no;
    
    int tempNumber = no;

    // Counting digits using a loop
    do {
        valCount++;
        tempNumber /= 10;
    } while (tempNumber != 0);

    cout << "Number of digits in " << no << " is: " << valCount << endl;

    return 0;
}