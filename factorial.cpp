//program to calculate the factorial of
//a number entered by the user using recursion
//created by: Rukmini Bapat

#include <iostream>

using namespace std;

int factorial(int num);

int main(){
  int num = 0;
  cout<<"Please enter a number to find the factorial of: ";
  cin>>num;

  int answer = factorial(num);

  cout<<"The factorial of " << num << " is " << answer << endl;

}


int factorial(int num){
  if(num == 0 || num ==1) {
     return 1;
  }
  else {
     return num*factorial(num-1);
  }

}
