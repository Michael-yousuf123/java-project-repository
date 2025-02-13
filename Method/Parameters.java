public class Parameters {
 static void checkBill(int num) {
  if (num > 20){
   System.out.println("No Payement");
  } else {
   System.out.println("Payement is Available");
  }
 }
 public static void main(String[] args) {
  checkBill(10);
 }
}
