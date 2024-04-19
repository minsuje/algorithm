class Solution {
    public int[] twoSum(int[] nums, int target) {
        int sum = 0;
        for(int s = 0; s < nums.length; s++){
            for(int h = s + 1; h < nums.length; h++){
                sum = nums[s]+nums[h];
                if(sum == target){
                    return new int[] {s,h};
                }
            }
        }
        return new int[0];
    }
}