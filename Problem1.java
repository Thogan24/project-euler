class Problem1{
    public static void main(String[] args) {
        int sum = 0;
        int count = 0;
        while(count < 1000){
            if(count % 3 == 0 || count % 5 == 0){
                System.out.println(count);
                sum += count;
                
            }
            count++;
        }
        System.out.println(sum);
    }
    
}
