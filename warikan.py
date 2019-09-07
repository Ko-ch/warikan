def warikan(amount, number_of_people):
    print(f"一人当たり：{amount // number_of_people}円、 端数：{amount % number_of_people}円")


warikan(int(input('合計金額は？')), int(input("合計人数は？")))
