public class problem20 {
    // ** JAVA VERSION NOT WORKING **
    // Facotiral 100 is too large
    public static void main(String[] args) {
        long factorial100 = factorial(100L);
        System.out.println(factorial100);
        System.out.println(sumOfDigits(factorial100));
    }

    public static long factorial(long num){
        long product = 1L;
        for(long i = num; i > 0; i--){
            product *= i;
            System.out.println(product);
            System.out.println();
        }
        return product;
    }

    public static float sumOfDigits(float num){
        String numString = Integer.toString((int) num);
        float sum = 0;
        for(int i = 0; i < numString.length(); i++){
            sum += Integer.parseInt(numString.substring(i, i+1));
        }
        return sum;
    }
}
