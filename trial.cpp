#include <iostream>
using namespace std;
int main()
{
    int number;
    int sum;
    cout << "enter a positive integer:";
    cin >> number;

    if (number < 0)
    {
        cout << "please enter a positive integer";
    }
    else
    {
        int i = 0;
        while (i <= number)
            {
                if (i % 2 == 0) {
                    sum = sum + i;
                } i++;
            }
    }
    cout << "Sum of the even number less than or equal to " << number << " is " << sum;
    return 0;
}