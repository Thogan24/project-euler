public class problem6 {
    public static void main(String[] args) {
        System.out.printf("%.0f", squareOfSums(100) - sumOfSquares(100));
    }

    public static double squareOfSums(int numSquare){
        double sumSquare = 0;
        for(int i = 1; i <= numSquare; i++){
            sumSquare += i;
        }
        return Math.pow(sumSquare, 2);
    }

    public static double sumOfSquares(int numSum){
        double sumSum = 0;
        for(int j = 1; j <= numSum; j++){
            sumSum += Math.pow(j, 2);
        }
        return sumSum;
    }
}
