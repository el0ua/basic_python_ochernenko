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
    elif isinstance(obj, dict):
        copy_dict = {}
        for key, value in obj.items():
            copy_dict[copydeep(key)] = copydeep(value)
        return copy_dict

def main():
    dict1 = {1: 'a', 2: 1, 3: 2.0, 4: ['b']}
    dict2 = copydeep(dict1)
    dict1[3] = 9
    print(f"Original obj:\n{dict1}\nCopy:\n{dict2}")


if __name__ == "__main__":
    main()