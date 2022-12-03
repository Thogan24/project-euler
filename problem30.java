public class problem30 {
    public static void main(String[] args) {
        float i = 0;
        while(true){
            if(i == sumOfDigitsToFifthPower(i))
                System.out.println(i);
            i++;
        }
    }

    public static float sumOfDigitsToFifthPower(Float num){
        String numString = String.format("%.0f", Float.toString(num));
        System.out.println(numString.length());
        float sum = 0;
        for(int i = 0; i < numString.length(); i++){
            System.out.println(numString.substring(i, i+1));
            sum += Math.pow(Float.parseFloat(numString.substring(i, i+1)), 5);
        }
        return sum;
    }
}
