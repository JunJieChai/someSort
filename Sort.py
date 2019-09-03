import random
class Sort():
    def __init__(self):
        pass

    def bubbleSort(self, nums):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]

    def selectSort(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

    def insertSort(self, nums):
        for i in range(len(nums)):
            temp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > temp:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp

    def quickSort(self, nums, l, r):
        if l >= r:
            return
        i = l
        j = r
        temp = nums[i]
        while i < j:
            while j > 0 and nums[j] > temp:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < r and nums[i] < temp:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = temp
        self.quickSort(nums, l, i - 1)
        self.quickSort(nums, i + 1, r)

    def quickSort2(self, nums, l, r):
        # 模拟栈
        lr = []
        lr.append(r)
        lr.append(l)
        while lr:
            l = lr.pop()
            r = lr.pop()
            i = l
            j = r
            temp = nums[i]
            while i < j:
                while j > 0 and nums[j] > temp:
                    j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1
                while i < r and nums[i] < temp:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = temp
            if i - 1 > l:
                lr.append(i - 1)
                lr.append(l)
            if i + 1 < r:
                lr.append(r)
                lr.append(i + 1)

    def shellSort(self, nums):
        i = len(nums) // 2
        while i > 0:
            for j in range(len(nums) - i):
                if j + i <= len(nums) - 1 and nums[j + i] < nums[j]:
                    nums[j], nums[j + i] = nums[j + i], nums[j]
            i = i // 2

    def mergeone(self, nums, l, m, r):
        temp = [0] * (r - l + 1)
        i = l
        j = m + 1
        k = 0
        while i <= m and j <= r:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                k += 1
                j += 1
        while i <= m:
            temp[k] = nums[i]
            k += 1
            i += 1
        while j <= r:
            temp[k] = nums[j]
            k += 1
            j += 1
        nums[l:r + 1] = temp

    def mergeSort(self, nums, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        self.mergeone(nums, l, m, r)

    def headadjust(self, nums, i, nlen):
        temp = nums[i]
        k = 2 * i + 1
        while k < nlen:
            if k + 1 < nlen and nums[k + 1] > nums[k]:
                k += 1
            if nums[k] > temp:
                nums[i] = nums[k]
                i = k
            k = 2 * k + 1
        nums[i] = temp

    def heapSort(self, nums):
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.headadjust(nums, i, len(nums))
        for j in range(len(nums)-1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.headadjust(nums, 0, j)


if __name__ == '__main__':
    nums = [random.randint(0, 10) for i in range(10)]
    print(nums)
    sort = Sort()
    # sort.bubbleSort(nums)
    # sort.selectSort(nums)
    # sort.insertSort(nums)
    # sort.quickSort2(nums, 0, len(nums) - 1)
    # sort.shellSort(nums)
    # sort.mergeSort(nums, 0, len(nums)-1)
    sort.heapSort(nums)
    print(nums)
