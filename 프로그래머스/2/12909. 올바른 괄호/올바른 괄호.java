import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int count = 0;
        for(int i = 0; i < s.length(); i++ ){
            char a = s.charAt(i);
            
            if(a == '('){
                    count++;
                }
            else if(a == ')'){
                    count--;   
                }
            if(count < 0){
                    return false;
                }
        }
        return count == 0;
    }
}