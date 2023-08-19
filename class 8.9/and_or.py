import datetime

# 获取今天的日期
current_date = datetime.datetime.now()
current_month = current_date.month
current_day = current_date.day


# 获取用户输入的出生年份、月份和日期
birth_year = int(input("请输入您的出生年份："))
birth_month = int(input("请输入您的出生月份："))
birth_day = int(input("请输入您的出生日期："))

# 根据日期给出不同的祝福
if birth_month == current_month and birth_day == current_day:
    print("生日快乐！今天是您的生日，愿您的一年更加美好、充满幸福！")
elif birth_month == 1 and birth_day == 1:
    print("新年伊始，愿您在新的一年里充满希望和喜悦！")
# elif birth_month == 2 and birth_day == 14:
#     print("情人节快乐！愿您与心爱的人共度美好时光！")
elif birth_month == 4 and birth_day == 1:
    print("愚人节快乐！不要被愚弄哦！")
elif birth_month == 5 and birth_day == 1:
    print("五一劳动节，愿您的辛勤努力获得丰硕的成果！")
elif birth_month == 12 and birth_day == 25:
    print("圣诞节快乐！愿您与家人朋友共度温馨时光！")
elif birth_month == 8 or birth_month == 2:
    print("祝你天天开心！！！！")
else:
    print("愿您的每一天都充满快乐、幸福和美好！")
