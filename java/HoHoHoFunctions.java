//https://www.codewars.com/kata/52af1f150fcae8d33d0009bc/solutions/java
public class HoHoHoFunctions {
    public static String ho(String s) {
        return "Ho " + s;
    }
    public static String ho() {
        return "Ho!";
    }

    public static void main(String[] args) {
        System.out.println(ho(ho(ho())));
    }
}
