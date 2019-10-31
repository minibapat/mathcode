// A program that removes the odd numbers in a list of numbers
// entered by the user.

import java.util.ArrayList;
import java.util.Scanner;

public class RemoveOdds{

   public static void main(String [] args){
         RemoveOdds r = new RemoveOdds();
         r.run();
   }

   public void run(){
        Scanner input = new Scanner(System.in);
        ArrayList<Integer> nums = new ArrayList<Integer>();
        System.out.println("Enter a list of six numbers and I will remove the odd numbers:");
        int counter = 0;
        while(counter<6){
            nums.add(input.nextInt());
            counter++;
        }
        ArrayList<Integer> answer = removeOdds(nums);
        System.out.println("Here is your list with the odd numbers removed:");
        for(Integer a: answer){
          System.out.print(a + " ");
        }
  }

  public ArrayList<Integer> removeOdds(ArrayList<Integer> nums){
        for(int i = 0; i<nums.size(); i++){
           if(nums.get(i)%2 != 0){
              nums.remove(i);
              i--;
           }
        }
        return nums;


  }

}
