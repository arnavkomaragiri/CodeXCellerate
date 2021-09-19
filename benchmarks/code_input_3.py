def threeSum(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
    res = [sorted(x) for x in res]
    return [list(x) for x in set(tuple(x) for x in res)]