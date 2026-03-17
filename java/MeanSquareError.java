// function accepts two integer arrays of equal length
// compares the value each member in one array to the corresponding member in the other
// squares the absolute value difference between those two values
// and returns the average of those squared absolute value difference between each member pair.

public class MeanSquareError {
  public static double solution(int[] arr1, int[] arr2) {
    double dif = 0;
    for (int i = 0; i < arr1.length; i++) {
      dif += (Math.pow(Math.abs(arr1[i] - arr2[i]), 2));
    }
    return dif / arr1.length;
  }

  public static void main(String[] args) {
    System.out.println(solution(new int[] { 10, 10, 10, 2 }, new int[] { 10, 25, 5, -2 }));
  }

}


// public class Solution {
//     public static double solution(int[] arr1, int[] arr2) {
//         return java.util.stream.IntStream.range(0, arr1.length).map(i -> arr1[i] - arr2[i]).map(diff -> diff * diff).average().getAsDouble();
//     }
// }