import java.util.Arrays;
import java.util.Stack;

public class Sort {
    public Sort() {
    }

    public void bubbleSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j < nums.length - i; j++) {
                if (nums[j - 1] > nums[j]) {
                    int temp = nums[j];
                    nums[j] = nums[j - 1];
                    nums[j - 1] = temp;
                }
            }
        }
    }

    public void selectSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
    }

    public void insertSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int temp = nums[i];
            int j = i - 1;
            while (j >= 0 && nums[j] > temp) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = temp;
        }
    }

    public void quickSort(int[] nums, int l, int r) {
        if (nums == null || l >= r)
            return;
        int i = l;
        int j = r;
        int temp = nums[l];
        while (i < j) {
            while (nums[j] >= temp && i < j) {
                j--;
            }
            if (i < j) {
                nums[i++] = nums[j];
            }
            while (nums[i] <= temp && i < j) {
                i++;
            }
            if (i < j) {
                nums[j--] = nums[i];
            }
        }
        nums[i] = temp;
        quickSort(nums, l, i - 1);
        quickSort(nums, i + 1, r);
    }

    //非递归
    public void quickSort2(int[] nums, int l, int r) {
        Stack<Integer> stack = new Stack<Integer>();
        if (l < r) {
            stack.push(r);
            stack.push(l);
            while (!stack.isEmpty()) {
                int start = stack.pop();
                int end = stack.pop();
                int i = start;
                int j = end;
                int temp = nums[i];
                while (i < j) {
                    while (i < j && nums[j] >= temp) {
                        j--;
                    }
                    if (i < j) {
                        nums[i++] = nums[j];
                    }
                    while ((i < j && nums[i] <= temp)) {
                        i++;
                    }
                    if (i < j) {
                        nums[j--] = nums[i];
                    }
                }
                nums[i] = temp;
                if (i - 1 > start) {
                    stack.push(i - 1);
                    stack.push(start);
                }
                if (i + 1 < end) {
                    stack.push(end);
                    stack.push(i + 1);
                }
            }
        }
    }

    public void shellSort(int[] nums) {
        for (int i = nums.length / 2; i > 0; i /= 2) {
            //控制步长
            for (int j = 0; j + i < nums.length; j++) {
                //控制位置
                if (nums[j] > nums[j + i]) {
                    int temp = nums[j];
                    nums[j] = nums[j + i];
                    nums[j + i] = temp;
                }
            }
        }
    }

    private void merge(int[] nums, int l, int m, int r) {
        int[] temp = new int[r - l + 1];
        int i = l;
        int j = m + 1;
        int k = 0;
        while (i <= m && j <= r) {
            if (nums[i] < nums[j]) {
                temp[k++] = nums[i++];
            } else {
                temp[k++] = nums[j++];
            }
        }
        //左侧剩余
        while (i <= m) {
            temp[k++] = nums[i++];
        }
        //右侧剩余
        while (j <= r) {
            temp[k++] = nums[j++];
        }
        //拷贝到原数组
        for (int kk = 0; kk < temp.length; kk++) {
            nums[kk + l] = temp[kk];
        }
    }

    public void mergeSort(int[] nums, int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            mergeSort(nums, l, m);
            mergeSort(nums, m + 1, r);
            merge(nums, l, m, r);
        }
    }

    public void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

    public void headAdjust(int[] nums, int i, int len) {
        //2i+1左子节点
        int temp = nums[i];
        for (int k = i * 2 + 1; k < len; k = 2 * k + 1) {
            int swapIndex = k;
            if (k + 1 < len && nums[k] < nums[k + 1]) {
                //如果左子节点小于右子节点，swapIndex指向右子节点
                k++;
            }
            if (nums[k] > temp) {
                //如果子节点大于父节点，子节点的值给父节点，i指向交换后的节点
                nums[i] = nums[k];
                i = k;
            } else {
                break;
            }
        }
        nums[i] = temp;
    }

    public void heapSort(int[] nums) {
        for (int i = nums.length / 2 - 1; i >= 0; i--) {
            headAdjust(nums, i, nums.length);
        }
        //System.out.println(Arrays.toString(nums));
        for (int j = nums.length - 1; j > 0; j--) {
            swap(nums, 0, j);
            headAdjust(nums, 0, j);
        }
    }


    public static void main(String[] args) {
        int[] nums = new int[10];
        for (int i = 0; i < nums.length; i++)
            nums[i] = (int) (Math.random() * 20-10);
        System.out.println(Arrays.toString(nums));
        Sort sort = new Sort();
//        sort.bubbleSort(nums);
//        sort.selectSort(nums);
//        sort.insertSort(nums);
//        sort.quickSort(nums,0,nums.length-1);
//        sort.quickSort2(nums, 0, nums.length - 1);
//        sort.mergeSort(nums, 0, nums.length - 1);
        sort.heapSort(nums);
        System.out.println(Arrays.toString(nums));

    }
}
