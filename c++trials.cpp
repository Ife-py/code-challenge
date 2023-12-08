#include <iostream>
using namespace std;

// A function that takes an int totalNumberOfDays and returns the equivalent years, months, and days
void convertDays(int totalNumberOfDays) {
  // Assume that a year has 365 days and a month has 30 days
  int years = totalNumberOfDays / 365; // Calculate the number of years
  int remainingDays = totalNumberOfDays % 365; // Calculate the remaining days after subtracting the years
  int months = remainingDays / 30; // Calculate the number of months
  int days = remainingDays % 30; // Calculate the remaining days after subtracting the months
  // Print the result
  cout << totalNumberOfDays << " days = " << years << " years, " << months << " months, and " << days << " days." << endl;
}

// A main function that asks the user to input the number of days and calls the convertDays function
int main() {
  int totalNumberOfDays; // Declare a variable to store the user input
  cout << "Please enter the number of days: "; // Prompt the user to enter the number of days
  cin >> totalNumberOfDays; // Read the user input and store it in the variable
  convertDays(totalNumberOfDays); // Call the convertDays function with the user input as the argument
  return 0;
}