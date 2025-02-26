/* public class Dog { /* public means anyone can access the class, class is class and Dog is the name of the class */ 
 /* public static void main(String[] args) { /*void means the method which return nothing and main is the name of this method, String is the argument of this method */
  /*System.out.println("Home based Learnig");
 }*/
/*}*/

public class Dog {
 // Writing class 
 int x = 8; // class attribute
 int y = 9; // multiple attribute
 public static void main(String[] args) {
  // class method 
  Dog age1 = new Dog(); // instantiate objects
  Dog age2 = new Dog();
  age1.x = 8;
  age2.y = 9;
  System.out.println(age1.x * age2.y);
 }
}

