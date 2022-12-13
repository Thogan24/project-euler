public class problem16 {
    // ** JAVA VERSION NOT WORKING **

    // Math.pow(2, 1000) not displaying all nums
    public static void main(String[] args) {
        long bigNumber = 1;
        for (int i = 0; i < 1000; i++){
            bigNumber *= 2;
            System.out.println(bigNumber);
        }
        //System.out.printf("%.0f", bigNumber);
        System.out.println(bigNumber);
        System.out.println(sumOfDigits(bigNumber));
    }
    public static long sumOfDigits(long num){
        String numString = Long.toString(num);
        System.out.println(numString);
        long sum = 0;
        for(int i = 0; i < numString.length(); i++){
            sum += Long.parseLong(numString.substring(i, i+1));
        }
        return sum;
    }
}
