// https://www.codewars.com/kata/5672682212c8ecf83e000050

class DoubleLinear {
    
    public static int dblLinear(int n) {
        int[] u = new int[n + 1];
        u[0] = 1;

        int i = 0;
        int j = 0;

        for (int k = 1; k <= n; k++) {
            int x = 2 * u[i] + 1;
            int y = 3 * u[j] + 1;

            int next = Math.min(x, y);
            u[k] = next;

            if (next == x) i++;
            if (next == y) j++;
        }

        return u[n];
    }
}