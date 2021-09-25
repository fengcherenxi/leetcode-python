class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for(int i = 0; i<n; i++) {
            for(int j = i+1; j<n; j++){
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};//暴力求解
                }
            }
        } 
        return new int[0];//这个 return 什么用都没有，只是返回一个垃圾，防止编译器报错而已。
    }
}