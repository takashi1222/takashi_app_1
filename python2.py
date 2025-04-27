def calculate_sum(numbers):

  total = 0
  for number in numbers:
    total += number
  return total

my_list = [10, 25, 5, 15]
sum_result = calculate_sum(my_list)

print(f"リスト {my_list} の合計値は: {sum_result} です。")

empty_list = []
sum_empty = calculate_sum(empty_list)
print(f"リスト {empty_list} の合計値は: {sum_empty} です。")

  def __init__(self, name, age):

    self.name = name
    self.age = age

  def introduce(self):

    print(f"こんにちは、私の名前は {self.name} です。年齢は {self.age} 歳です。")

person1 = Person("山田 太郎", 30)
person2 = Person("佐藤 花子", 25)

person1.introduce()
person2.introduce()

print(f"{person1.name}さんの年齢は {person1.age} 歳です。")