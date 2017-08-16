// package whatever; // don't place package name!

import java.io.*;
import java.util.*;


class myCode
{
    public static void main (String[] args) throws java.lang.Exception
    {
//         System.out.println("Hello Java");
        int[] input = {-2, -2, -2, -2, 3, 4};
        System.out.println(maxFrequencyInt(input));
    }

    public static int maxFrequencyInt (int[] input) {


        // initialize hash map
        Map<Integer,Integer> intFrequencies = new HashMap<Integer,Integer>();
        int count = 0;
        int maxKey = Integer.MIN_VALUE;

        for(int i = 0; i < input.length; i ++) {
            if (intFrequencies.containsKey(input[i])) {
                intFrequencies.put(input[i], intFrequencies.get(input[i]) + 1);

            } else {
                intFrequencies.put(input[i], 1);
            }

            if(intFrequencies.get(input[i]) > count) {
                count = intFrequencies.get(input[i]);
                maxKey = input[i];
            }
        }

        return maxKey;

    }
}

   
