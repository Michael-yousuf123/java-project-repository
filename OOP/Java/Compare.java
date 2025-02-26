public class Compare {
 static void myMethod() {
  System.out.println("Static Method");
 }
 public void myPublicMethod() {
  System.out.println("Public Method");
 }
 public static void main(String[] args) {
  myMethod();
  
  Compare myObj = new Compare();
  myObj.myPublicMethod();
 }
}
