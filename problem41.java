public class problem41 {
    public static void main(String[] args) {
        int i = 0;
        while(true){
            if(isPandigital(i) && isPrime(i)){
                System.out.println(i);
            }
            i++;
        }
    }

    public static boolean isPandigital(int n){
        String stringNum = Integer.toString(n);
        String stringWithAllDigits = "";
        // Sets up String with all digits from 1 to num of digits
        for(int i = 1; i <= stringNum.length(); i++){
            stringWithAllDigits += Integer.toString(i);
        }

        for(int k = 0; k < stringNum.length(); k++){
            for (int j = 0; j < stringWithAllDigits.length(); j++){
                if(stringNum.substring(k, k+1) == stringWithAllDigits.substring(j, j+1)){
                    stringNum = stringNum.substring(0, k) + stringNum.substring(k+1, stringNum.length());
                    stringWithAllDigits = stringWithAllDigits.substring(0, j) + stringWithAllDigits.substring(j+1, stringWithAllDigits.length());
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
        if (n <= 1)
            return false;

        for (int i = 3; i < n; i+=2)
            if (n % i == 0)
                return false;

        return true;
    }
}
