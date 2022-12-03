public class problem16 {
    public static void main(String[] args) {
        System.out.printf("%.0f", Math.pow(2, 1000));
        System.out.println();
        System.out.println(sumOfDigits(Math.pow(2, 1000)));
    }
    public static float sumOfDigits(double num){
        String numString = Double.toString(num);
        System.out.println(numString);
        float sum = 0;
        for(int i = 0; i < numString.length(); i++){
            sum += Float.parseFloat(numString.substring(i, i+1));
        }
        return sum;
    }
}
