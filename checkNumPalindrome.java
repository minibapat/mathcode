//check whether number is palindrome without converting integer to string
//used stacks
import java.io.*; 
import java.util.*; 
class Main {
  public static void main(String[] args) {
    //check whether integer is palindrome
    int num = 102;
    boolean answer = findAns(num);
    System.out.println(answer);
  }

  public static boolean findAns(int num){
    Stack<Integer> s = new Stack<Integer>();
    int ptr = num;
    while(ptr != 0){
      s.push(ptr%10);
      ptr = ptr/10;
    }
    int ptr2 = num;
    while(!s.empty()){
      if(s.pop() != ptr2%10){
        return false;
      }
      ptr2/=10;
    }
  return true;
  }

}
