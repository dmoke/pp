// # everytime you press the button it sends you an array of one-letter strings representing directions
// # to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
// # and you know it takes you one minute to traverse one city block, so create a function that will return
// # true if the walk the app gives you will take you exactly ten minutes
// # and will, of course, return you to your starting point

public class TenMinWalk {
  public static boolean isValid(char[] walk) {

    int x = 0, y = 0;

    for (char c : walk) {
      switch (c) {
      case 'n':
        x++;
        break;
      case 's':
        x--;
        break;
      case 'w':
        y++;
        break;
      case 'e':
        y--;
        break;
      }
    }
    return walk.length == 10 && x == 0 && y == 0;
  }

  public static void main(String[] args) {
    boolean res = isValid(new char[] { 'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's' });
    System.out.println(res);
  }
}