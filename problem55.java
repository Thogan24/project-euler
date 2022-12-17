// Unsolved in java

public class problem55 {
    public static void main(String[] args) {
        System.out.println("");
    }

    public static boolean isPalindromic(int num){
        // store the number to originalNum
        int originalNum = num;
        int reversedNum = 0;
        int remainder;
        // get the reverse of originalNum
        // store it in variable
        while (num != 0) {
          remainder = num % 10;
          reversedNum = reversedNum * 10 + remainder;
          num /= 10;
        }
    
        // check if reversedNum and originalNum are equal
        if (originalNum == reversedNum) {
          return true;
        }
        return false;
    }
}
