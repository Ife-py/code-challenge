#include<iostream>
using namespace std;

int main()
{
 int p, r, volume, area;
 cout<<" enter a value for radius"<<endl;
 cin>> r;

 p=3.14159265;
 volume=(0.75)*p*(r*r*r);
 area=4*p*(r*r);
 cout<< "the volume of the sphere is:"<<volume<<endl;
 cout<<"the area of the sphere is:"<<area;

}