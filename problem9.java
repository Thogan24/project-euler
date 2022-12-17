// Solved

public class problem9 {
    public static void main(String[] args) {
        for(int a = 0; a < 1000; a++){
            for(int b = 0; b < 1000; b++){
                for(int c = 0; c < 1000; c++){
                    if(a+b+c == 1000 && pythagoreanTriplet(a, b, c)){
                        System.out.println(a*b*c);
                    }
                }
            }
        }
    }

    public static boolean pythagoreanTriplet(int a, int b, int c){
        if(Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2)){
            return true;
        }
        return false;
    }
}
