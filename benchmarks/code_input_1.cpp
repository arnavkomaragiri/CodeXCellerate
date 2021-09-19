vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> out(2);
    for (int i = 0; i < nums.size() - 1; i++) {
        for (int j = nums.size() - 1; j > i; j--) {
            if (nums[i]+nums[j] == target){
                out[0] = i;
                out[1] = j;
                return out;
            }
        }
    }
    return {};
}