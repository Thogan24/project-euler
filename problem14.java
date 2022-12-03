public class problem14 {
    public static void main(String[] args) {
        long i = 1;
        float biggestCount = 0;
        while(i < 1000000){
            if(collatzSequence(i) > biggestCount){
                biggestCount = collatzSequence(i);
                System.out.println(i + " | " + biggestCount + " | " + collatzSequence(i));
            }
            i++;
        }
    }

    public static float collatzSequence(long i){
        float count = 0;
        while(i != 1){
            if(i % 2 == 0){
                i /= 2;
            }
            else{
                i = (3 * i) + 1;
            }
            count++;
        }
        count++;
        return count;
    }
}
