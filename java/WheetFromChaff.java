public class WheetFromChaff {

    public static long[] wheatFromChaff(long[] values) {

        long[] result = values.clone();

        int left = 0;
        int right = result.length - 1;

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
        long[] result = wheatFromChaff(new long[]{-6, -4, 6, 2});
        System.out.println(java.util.Arrays.toString(result));
    }
}