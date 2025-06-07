class Solution:
    def union(self, nums1, nums2):
        l, r = 0, 0
        res = []
        
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                if not res or res[-1] != nums1[l]:
                    res.append(nums1[l])
                l += 1
            elif nums1[l] > nums2[r]:
                if not res or res[-1] != nums2[r]:
                    res.append(nums2[r])
                r += 1
            else:  # nums1[l] == nums2[r]
                if not res or res[-1] != nums1[l]:
                    res.append(nums1[l])
                l += 1
                r += 1
        
        # Add remaining elements
        while l < len(nums1):
            if not res or res[-1] != nums1[l]:
                res.append(nums1[l])
            l += 1
        while r < len(nums2):
            if not res or res[-1] != nums2[r]:
                res.append(nums2[r])
            r += 1
        
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.union([1,2,6], [1,2,7]))
    