// Basic if/else example from HR 
// Details: https://www.hackerrank.com/challenges/java-if-else/problem


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class IfElseExample {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String ans = "";
        if (n%2!=0) {
            ans = "Weird";}

        else {

            if ((2<=n) && (n<=5))  {
            ans = "Not Weird";}
            
            else if ((6<=n) && (n<=20)) {
            ans = "Weird";}

            else {
                ans = "Not weird";
            }

        }

        System.out.println(ans);
    }
}


// Lesson learned? You have to wrap your statements in lines 23 and 26 so that
// when the entire line is evaluated, the && operator doesn't short-circuit 
// and just evaluate the first statement.