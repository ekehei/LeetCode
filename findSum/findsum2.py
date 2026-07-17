def sum(nums,target):
    hashtable = dict()
    for i, num in enumerate(nums):
        x=target - num
        if x in hashtable:
            print(hashtable[x],i)
            return
        hashtable[num] = i

nums1 = [2,7,11,15]
target1 = 9
sum(nums1,target1)
nums2 = [3,2,4]
target2 = 6
sum(nums2,target2)
nums3 = [3,3]
target3 = 6
sum(nums3,target3)