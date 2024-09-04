class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        for(int people : array){
            if(people > height) answer++;
        }
        return answer;
    }
}