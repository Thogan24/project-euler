// Unsolved in java

public class problem41 {
    // Pandigital not working
    public static void main(String[] args) {
        int i = 0;
        while(i <= 987654321){
            if(isPandigital(i) && isPrime(i)){
                System.out.println(i);
            }
            i++;
        }
    }

    public static boolean isPandigital(int n){
        String stringNum = Integer.toString(n);
        String stringWithAllDigits = ""; // Stores all digits from 1 to digit length
        // Sets up String with all digits from 1 to num of digits
        for(int i = 1; i <= stringNum.length(); i++){
            stringWithAllDigits += Integer.toString(i);
        }

        for(int k = 0; k < stringNum.length(); k++){
            for (int j = 0; j < stringWithAllDigits.length(); j++){
                if(stringNum.substring(k, k+1) == stringWithAllDigits.substring(j, j+1)){
                    stringNum = stringNum.substring(0, k) + stringNum.substring(k+1, stringNum.length()); // Removes the letter from the list
                    stringWithAllDigits = stringWithAllDigits.substring(0, j) + stringWithAllDigits.substring(j+1, stringWithAllDigits.length()); // Removes it from here
                }
                // System.out.println(stringNum);
                // System.out.println(stringWithAllDigits);
            }
        }

        if(stringWithAllDigits.length() == 0 && stringNum.length() == 0){
            System.out.println("PANDIGITAL!!!");
            return true;
        }
        return false;
    }

    public static boolean isPrime(int n)
    {
        if(n < 2) return false;
        if(n == 2 || n == 3) return true;
        if(n%2 == 0 || n%3 == 0) return false;
        long sqrtN = (long)Math.sqrt(n)+1;
        for(long i = 6L; i <= sqrtN; i += 6) {
            if(n%(i-1) == 0 || n%(i+1) == 0) return false;
        }
        return true;
    }
}
