import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<Integer> arr = new ArrayList<Integer>();
        String[] str = s.split(" ");
        for(int i = 0; i<str.length; i++)
            arr.add(Integer.parseInt(str[i]));
        
        answer = "" + Collections.min(arr) + " " + Collections.max(arr);
        /*
        
        String[] tmp = str.split(" ");
        int min, max, n;
        min = max = Integer.parseInt(tmp[0]);
        for (int i = 1; i < tmp.length; i++) {
                n = Integer.parseInt(tmp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }

        return min + " " + max;

        */
        return answer;
    }
}