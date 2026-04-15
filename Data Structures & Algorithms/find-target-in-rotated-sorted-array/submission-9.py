class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] < nums[r]: #sorted

                if target<nums[mid]:
                    r = mid-1
                else :
                    l = mid+1

            else:# nums[l] > nums[r]
                if nums[mid] > nums[r]: # l to mid is sorted
                    if target >= nums[l] and target< nums[mid]:
                        r = mid-1
                    else:
                        l = mid+1
                else: #nums[mid] < nums[r] > l  || mid to right sorted:
                    if target > nums[mid] and target<= nums[r]:
                        l = mid+1
                    else:
                        r = mid-1
        return -1

                

        