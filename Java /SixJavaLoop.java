// Challege link: https://www.hackerrank.com/challenges/java-loops-i/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        
        // From here on it's Meda's code 
        for (int i =1; i<=10;i++) {
            int total = i  * N;
            System.out.println(N + " x " + i + " = " + total);
        }
        
    }
}

// Notes: Yass! Record time. Took only two minutes at 6am haha.