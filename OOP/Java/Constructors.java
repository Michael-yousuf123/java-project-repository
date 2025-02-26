// create a Constructors class
public class Constructors {
 int x; // create a class attribute
 // create a class constructor for the constructor class
 public Constructors() {
  x = 5; // set the initial value for the class attribute x
 }

 public static void main(String[] args) {
  Constructors myObj = new Constructors();
  System.out.println(myObj.x);
 }
}
