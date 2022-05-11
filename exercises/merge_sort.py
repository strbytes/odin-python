def merge_sort(lst):
    if len(lst) == 1:
        return lst
    return merge(merge_sort(lst[:len(lst)//2]), merge_sort(lst[len(lst)//2:]))

def merge(a, b):
    if not a: return b
    elif not b: return a
    i, j = 0, 0
    solution = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            solution.append(a[i])
            i += 1
        else:
            solution.append(b[j])
            j += 1
    if a[i:]: solution.extend(a[i:])
    elif b[j:]: solution.extend(b[j:])
    return solution

if __name__ == "__main__":
    import random
    print(merge_sort([random.randint(0, 99) for i in range(100)]))

