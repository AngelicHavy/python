from typing import List, Any, Tuple


def main():
    task1([10, 20, 30, 40, 50, 60])
    A = ['A', 'B', 'C', 'D', 'E', 'Y', 'U', 'O', 'P']
    B = [5, 73, 81, 4, 0, 80, 36, 37, 50]
    C = [10, 30, 22.5, 80, 990, 103, 50, 15, 3]
    task2(A, B, C)
    print(task3())
    print(task4("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
                "labore et dolore magna aliqua.Massa eget egestas purus viverra accumsan.Eu volutpat odio "
                "facilisis mauris sit amet.In metus vulputate eu scelerisque felis imperdiet proin.Velit "
                "euismod in pellentesque massa placerat duis ultricies lacus.", 'a'))
    print(task5("DUT IS GOOD"))

    print(task6([1, 2, 3, 4, 5, 6, 10, 0, -10, -12]))


def task1(my_list):
    my_list.insert(1, -5)
    print(my_list)
    minmax_list = task1findmin(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append("Анжеліка Гаврилюк")
    print(my_list)
    return my_list, minmax_list[0], minmax_list[1], len(my_list)


def task1findmin(my_list) -> list[int]:
    min_num = my_list[0]
    max_num = min_num
    for num in my_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return [min_num, max_num]


def task2(A, B, C):
    total_cost = calculatetotalcost(C)
    average_price = calculateaverage(total_cost, len(C))
    most_stocked_item = A[findmoststocked(B)]
    print(f"Total_cost: {total_cost}, average: {average_price}, most stocked: {most_stocked_item}")
    return total_cost, average_price, most_stocked_item


def calculatetotalcost(C) -> float:
    total = 0
    for price in C:
        total += price
    return total


def calculateaverage(total_cost, size) -> float:
    return total_cost / size


def findmoststocked(B) -> int:
    result = B[0]
    index = 0
    i = 0
    for occurence in B:
        if occurence > result:
            result = occurence
            index = i
        i += 1
    return index


def task3():
    A1 = []
    A2 = []
    for number in range(-25, 25, 1):
        if number < 0:
            A2.append(number)
        elif number > 0:
            A1.append(number)
    return A1, A2


def task4(message, char):
    occurences = 0
    for character in message:
        if character == char:
            occurences += 1
    return occurences


def task5(message) -> tuple[str, int]:
    print(message[:-8])
    modified_str = message.replace("GOOD", "NICE")
    print(modified_str)
    wordcount = len(message.split(" "))
    return modified_str, wordcount


def task6(list) -> float:
    result = 0
    for number in list:
        if 1 <= number <= 5:
            result += number
    return result


main()
