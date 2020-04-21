package Tutorial;

public class DataTypes {
    public static void main(String[] args) {
        //NON PRIMITIVE DATA TYPE
        /**
         * 1. String
         * 2. array
         * 3. class
         * 4. interface
         */
        String myString = "rizki";
        System.out.println(myString);

        //PRIMITIVE DATA TYPE
        byte myByte = 100;
        System.out.println("byte " + myByte);

        short myShort = 5000;
        System.out.println("short " + myShort);

        int myInt = 100000;
        System.out.println("int " + myInt);

        long myLong = 15000000000L;
        System.out.println("long " + myLong);

        float myFloat = 5.75f;
        System.out.println("float " + myFloat);

        double myDouble = 19.99d;
        System.out.println("double " + myDouble);

        // SCIENTIFIC
        float f1 = 35e3f; // 35 * 1000
        System.out.println(f1);

        double d1 = 12E4d;
        System.out.println(d1); // 12 * 10000

        //ASCII
        char a = 65, b = 66, c = 67;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}