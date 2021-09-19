vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> out(2);
    unordered_map<int, int> map;
    for (int i = 0; i < nums.size(); i++) {
        map[nums[i]] = i;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (map.find(target - nums[i]) != map.end() && map[target - nums[i]] != i) {
            out[0] = i;
            out[1] = map[target - nums[i]];
            return out;
        }
    }
    return {};
}