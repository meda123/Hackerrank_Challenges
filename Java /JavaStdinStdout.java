// Link to full challenge: https://www.hackerrank.com/challenges/java-stdin-stdout/problem


import java.util.Scanner;

public class JavaStdinStdout {

    public static void main (String[] args) {
        Scanner scan = new Scanner (System.in);
        
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();
        String s = scan.nextLine();
        
       
        scan.close();

        // Write your code here (all done!).      
        System.out.println("String: " + s);             
        System.out.println("Double: " + d);            
        System.out.println("Int: " + i);
    }

}