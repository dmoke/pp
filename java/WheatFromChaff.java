
public class WheatFromChaff {

    // The task of this kata is to write a function that takes an array of integers,
    // where every element of the array is either negative or positive.
    // The function should return the array sorted in such a way that all the
    // negative numbers come before all the positive numbers.

    public static long[] wheatFromChaff(long[] values) {

        long[] result = values.clone();

        int left = 0;
        int right = result.length - 1;

        // Using two pointers to traverse the array from both ends.
        // If the left pointer points at a positive number and the
        // right pointer points at a negative number, they are swapped.
        // This continues until the two pointers meet.

        while (left < right) {

            while (left < right && result[left] < 0)
                left++;

            while (left < right && result[right] > 0)
                right--;

            if (left < right) {
                long temp = result[left];
                result[left] = result[right];
                result[right] = temp;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        long[] result = wheatFromChaff(new long[] { -6, -4, 6, 2 });
        System.out.println(java.util.Arrays.toString(result));
    }
}
