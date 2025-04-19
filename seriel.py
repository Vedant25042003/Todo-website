def del_num(list, num):
        if num in list:
            list.remove(num)
            list = [n if n <= num else n - 1 for n in list]
        else:
            print(f"Number {num} not found in the list.")

        return list

list1 = [5,6,7,8]
num = 6
print(del_num(list1, num))