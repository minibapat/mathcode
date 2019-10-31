//Finding the max of two numbers
#include <iostream>
#include <cstdlib>
using namespace std;

int findMax(int one, int two);

int main(int argc, char *argv[]){

   if (argc!=3) {
    cerr << "Usage: " << argv[0] << " first number  second number"<< endl;
    exit(1);
   }


   int first = stoi(argv[1]);
   int second = stoi(argv[2]);

   if(first == second){
     cout<<"Both numbers are the same, so there is no max."<<endl;
     return 0;
   }

   int max = findMax(first, second);
   cout<<"The max of the two numbers is " << max<<endl;
   return 0;

}


int findMax(int one, int two){
   if(one>two)
      return one;
   return two;

}
