def calculate_sum(numbers):

total = 0
  for number in numbers:
    total += number
  return total

my_list = [5, 45, 70, 2]
sum_result = calculate_sum(my_list)

print(f"リスト {my_list} の合計値は: {sum_result} です。")

empty_list = []
sum_empty = calculate_sum(empty_list)
print(f"リスト {empty_list} の合計値は: {sum_empty} です。")