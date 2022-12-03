public class problem10 {
    public static void main(String[] args) {
        int i = 1;
        int sum = 0;
        while(i < 2000000){
            if(i % 3 != 0 && isPrime(i))
                sum += i;        
            i+=2;
            System.out.println(i);
        }
        System.out.println(sum+3);

    }

    public static boolean isPrime(int n)
    {
        if (n <= 1)
            return false;

        for (int i = 3; i < n; i+=2)
            if (n % i == 0)
                return false;

        return true;
    }
}
