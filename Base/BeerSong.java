public class BeerSong {
    public static void main(String[] args) {
        int BeerNum = 99;
        String word = "Bottles";
        while (BeerNum > 0) {
            if (BeerNum == 1){
                word = "Bottle";
            }
            System.out.println(BeerNum + " " + word + " of Beer on the Wall");
            System.out.println(BeerNum + " " + word + " of Beer.");
            System.out.println("Take one Down");
            System.out.println("Pass it Around.");
            BeerNum = BeerNum - 1;
            if (BeerNum == 0) {
                System.out.println("No more bottles of beer on the wall");
            }
        }
    }
}