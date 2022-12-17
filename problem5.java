// Solved

public class problem5 {
    public static void main(String[] args) {
        int number = 0;
        while(true){
            
            for(int i = 1; i <= 20; i++){
                if(number % i != 0)
                    break;
                if(i == 20){
                    System.out.println(number);
                }
            }
            number++;
        }
    }
}
