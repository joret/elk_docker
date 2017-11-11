java.util.Random


public class HelloWorld {
   public static void main(String[] args) {
      // Prints "Hello, World" in the terminal window.
       Random randGenerator = new Random();

       int ad_id = randGenerator.nextInt(10000);      
       System.out.println("Hello, World");
   }
}
