result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"
new_result_1 = int(result_1[result_1.index(':') + 2:]) + 10
new_result_2 = int(result_2[result_2.index(':') + 2:]) + 10
new_result_3 = int(result_3[result_3.index(':') + 2:]) + 10
print(new_result_1)
print(new_result_2)
print(new_result_3)
