public class problem3 {
    
    static boolean isPrime(double n)
    {
        if(n == 2){
            return true;
        }
        for (double i = 3; i < n; i+=2)
            if (n % i == 0)
                return false;
  
        return true;
    }

    static double primeFactor(double n)
    {
        double biggest = 0;
        while(n != 1){
            for(double i = 2; i <= n; i++){
                System.out.println(i);
                if(isPrime(i) && n%i == 0){
                    n /= i;
                    if(i>biggest){
                        biggest = i;
                    }
                }
            }
        }
        return biggest;
    }

    public static void main(String[] args){
        double ret = primeFactor(600851475143L);
        System.out.println(ret);
    }
}