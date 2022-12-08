public class problem10 {
    public static void main(String[] args) {
        int i = 1;
        long sum = 0;
        while(i < 2000000){
            if(isPrime(i))
                sum += i;        
            i++;
            //System.out.println(i);
        }
        System.out.println(sum);

    }

    public static boolean isPrime(long n)
    {
        // Check if number is less than
        // equal to 1
        if (n <= 1)
            return false;
 
        // Check if number is 2
        else if (n == 2)
            return true;
 
        // Check if n is a multiple of 2
        else if (n % 2 == 0)
            return false;
 
        // If not, then just check the odds
        for (long i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}
