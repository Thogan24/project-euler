// Solved

public class problem23 {
    public static void main(String[] args) {
        boolean shouldBreak = false;
        int sum = 0;
        for (int i = 0; i < 100; i++){ // For all numbers less than 28123

            for (int j = 0; j < i; j++){
                if (isAbundant(j)){
                    //System.out.println(j);
                    for (int k = 0; k < i; k++){
                        if (k+j == i && k != j && isAbundant(k)){
                                //System.out.println(i + " can be written");
                                shouldBreak = true;
                                break;
                        }
                    }
                }
                if (shouldBreak){
                    break;
                }
            }
            if (shouldBreak == false){
                sum += i;
                //System.out.println(i + " CANNOT BE WRITTEN!!!!!!!!! | " + sum);
                
            }
            shouldBreak = false;
            System.out.println("The current sum is: " + sum + " | Index at: " + i);

        }
    }


    
    public static boolean isAbundant(int num){
        int sum = 0;
        for(int i = 1; i < num; i++){
            if(num % i == 0){
                sum+= i;
            }
        }
        if (sum > num){
            return true;
        }
        return false;
    }
}
