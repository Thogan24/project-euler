public class problem7{
    public static void main(String[] args) {
        int i = 0;
        int primeCounter = 1;
        while (primeCounter <= 10001){
            if (isPrime(i)){
                System.out.println(primeCounter + ": " + i);
                primeCounter++;
            }
            i++;
        }
    }

    public static boolean isPrime(int n)
    {
        if (n <= 1)
            return false;

        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;

        return true;
    }
}