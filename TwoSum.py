def twoSum(a, b):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == b:
                print("Hasil TwoSum dari", b,
                      ": (", i, ",", j, ")")


nums = [2, 6, 7, 15]
target = 9

twoSum(nums, target)
