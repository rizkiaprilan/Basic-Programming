package Tutorial;

public class Operators {
    public static void main(String[] args) {
        byte bt = 5;
        System.out.println("bt: " + bt);
        
        // Binary Left Shift and assigns
        bt <<= 3;
        System.out.println("bt <<= 3: " + bt);

        // Binary Right Shift and assigns
        bt >>= 4;
        System.out.println("bt >>= 4: " + bt);

        // Shift right zero fill and assigns
        bt >>>= 1;
        System.out.println("bt >>>= 1: " + bt);

        // Binary AND assigns
        bt &= 4;
        System.out.println("bt &= 4: " + bt);

        // Binary exclusive OR and assigns
        bt ^= 4;
        System.out.println("bt ^= 4: " + bt);

        // Binary inclusive OR and assigns
        bt |= 4;
        System.out.println("bt |= 4: " + bt);

    }
}