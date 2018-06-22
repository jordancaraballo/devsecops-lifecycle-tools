//============================================================================
// Name        : ci-test.cpp
// Author      : Jordan A. Caraballo-Vega
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

// Prototypes
// Adding function to sum values
int sumValues(int,int);

// Main
int main() {

        // Friendly output
	cout << "!!!Hello People!!!" << endl; // prints !!!Hello World!!!
	cout << "This is our first commit for this CI Project. This commit will compile succesfully." << endl;

        int sum = sumValues(2,3);
        cout << "The result of the sum is " << sum << ". Ha! Can you guess the values?" << endl; 

        // Adding syntax error to see if build fails over bamboo
        int huge = {0,0,0,0}

	return 0;
}

// Functions
int sumValues(int a, int b) {
    return a + b;
}
