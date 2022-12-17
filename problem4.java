// Solved

public class problem4 {
    public static void main(String[] args) {
        int biggest = 0;
        for(int i = 999; i >= 100; i--){
            for(int j = 999; j >= 100; j--){
                System.out.println(biggest);
                if(isPalindrome(i*j) && (i*j)>biggest){                   
                    biggest = i*j;
                    
                }
            }
        }
    }

    public static boolean isPalindrome(int n){
        String number = Integer.toString(n);
        StringBuilder rev = new StringBuilder();
        rev.append(number);
        rev.reverse();
        if(number.length() == 5){
            if(number.substring(0, 2).equals(rev.substring(0, 2))){
                return true;
            }
        }
        if(number.length() == 6){
            if(number.substring(0, 3).equals(rev.substring(0, 3))){
                return true;
            }
        }
        return false;
    }
}
