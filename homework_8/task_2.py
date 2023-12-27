def copydeep(obj):
    if isinstance(obj, (str, int, float, bool)):
        return obj
    elif isinstance(obj, list):
        copy_list = []
        for i in obj:
            copy_list.append(copydeep(i))
        return copy_list
    elif isinstance(obj, tuple):
        copy_tuple = ()
        for i in obj:
            copy_tuple += copy_tuple(i)
        return copy_tuple

def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copydeep(lst1)
    lst1[3].append(0)
    print(f"Original obj:\n{lst1[3]}\nCopy:\n{lst2[3]}")


if __name__ == "__main__":
    main()