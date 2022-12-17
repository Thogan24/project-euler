// Solved

public class problem12 {
    public static void main(String[] args) {
        int i = 1;
        int triangleNumber = 0;
        while(true){
            triangleNumber = 0;
            for(int j = 0; j < i; j++){
                triangleNumber += j;
            }
            
            if(numOfDivisors(triangleNumber) >= 300){
                System.out.println(triangleNumber + " " + numOfDivisors(triangleNumber));
                
            }
            i++;
        }
    }

    public static int numOfDivisors(int n){
        int count = 0;
        for(int i = 1; i <= n; i++){
            if(n % i == 0){
                count++;
            }
        }
        return count;
    }
}
