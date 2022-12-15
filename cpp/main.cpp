#include <iostream>
using namespace std;

int larger (int a, int b)
{

  int z;
   if (a == b)
        cout << "both are equal"; 
   else if (a > b){
        cout << a << " is the bigger Number ";
    }
    else{
        if (b > a)
        cout << b << " is the bigger Number ";
      }
    return 0;
}

int main ()
{
  std::cout << "Hello, World!" << std::endl;
    int z;
   z = larger (5,7); 
  
    z = larger(5,5);
  }
