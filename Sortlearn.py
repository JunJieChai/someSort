import time
class Sort():
    def __init__(self, data):
        self.data = data
    #冒泡排序
    def bubble_sort(self):
        for i in range(len(self.data)):
            for j in range(1, len(self.data) - i):
                if self.data[j-1] > self.data[j]:
                    temp = self.data[j-1]
                    self.data[j-1] = self.data[j]
                    self.data[j] = temp
        return self.data
    #选择排序
    def select_sort(self):
        for i in range(len(self.data)):
            for j in range(i, len(self.data)):
                if self.data[i] > self.data[j]:
                    temp = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = temp
        return self.data
    #插入排序
    def insertion_sort(self):
        for i in range(len(self.data)):
            temp = self.data[i]
            j = i - 1
            while j >= 0 and  temp < self.data[j]:
                self.data[j+1] = self.data[j]
                j -= 1
            self.data[j+1] = temp
        return self.data
    #Shell排序
    def shell_sort(self):
        r = len(self.data) // 2
        while r >= 1:
            for i in range(r, len(self.data)):
                temp = self.data[i]
                j = i - r
                while j >= 0 and temp < self.data[j]:
                    self.data[j+r] = self.data[j]
                    j -= r
                self.data[j+r] = temp
            r = r // 2
        return self.data
    #快速排序
    def quick_sort(self, left, right):
        ltemp = left
        rtemp = right
        f_value = self.data[(left + right) // 2]
        while ltemp < rtemp:
            while self.data[ltemp] < f_value:
                ltemp += 1
            while self.data[rtemp] > f_value:
                rtemp -= 1
            if ltemp <= rtemp:
                temp = self.data[rtemp]
                self.data[rtemp] = self.data[ltemp]
                self.data[ltemp] = temp
                rtemp -= 1
                ltemp += 1
        if ltemp == rtemp:
            ltemp += 1
        if ltemp < right:
            self.quick_sort(rtemp+1, right)
        if rtemp > left:
            self.quick_sort(left, ltemp-1)
        return self.data
    # 堆排序
    def heap_sort(self, n):
        # creat heap, i is the number of node
        i = n // 2 - 1
        while i >= 0:
            while 2*i+1 < n:
                j = 2*i+1
                # If the left subtree is existed and smaller than the right subtree
                if j+1 < n and self.data[j] < self.data[j + 1]:
                    j += 1
                # swap the father node and the right subtree node
                if self.data[i] < self.data[j]:
                    temp = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = temp
                    i = j
                else:
                    break
            i -= 1
        # out
        end = n - 1
        while end > 0:
            temp = self.data[0]
            self.data[0] = self.data[end]
            self.data[end] = temp
            k = 0
            while 2*k+1 < end:
                j = 2*k+1
                if j+1 < end and self.data[j] < self.data[j + 1]:
                    j += 1
                if self.data[k] < self.data[j]:
                    temp = self.data[j]
                    self.data[j] = self.data[k]
                    self.data[k] = temp
                    k = j
                else:
                    break
            end -= 1
        return self.data

    def merge_one(self, a, b):
        c = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        if i == len(a):
            for val in b[j:]:
                c.append(val)
        else:
            for val in a[i:]:
                c.append(val)
        return c

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        middle = len(data) // 2
        left = self.merge_sort(data[:middle])
        right = self.merge_sort(data[middle:])
        return self.merge_one(left, right)

if __name__ == "__main__":
    a = [1, 9, 3, 6, 4]
    ss = Sort(a)
    print(ss.bubble_sort())
    print(ss.select_sort())
    print(ss.insertion_sort())
    print(ss.shell_sort())
    print(ss.quick_sort(0,len(a)-1))
    print(ss.heap_sort(len(a)))
    print(ss.merge_sort(a))
