public class problem2 {
    public static void main(String[] args) {
        int sum = 0;
        int current = 0;
        int previous = 1;
        while(current < 4000000){
            int next = previous + current;
            previous = current;
            current = next;
            //System.out.println(current);
            if (current % 2 == 0){
                sum += current;
                System.out.println(sum);
            }
        }
    }
}
