import random

choices = ["石头", "剪刀", "布"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == 0 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 0):
        return "玩家胜利"
    else:
        return "电脑胜利"

def main():
    print("石头、剪刀、布游戏")
    print("0. 石头")
    print("1. 剪刀")
    print("2. 布")
    
    user_choice = int(input("请选择（0/1/2）: "))
    if user_choice < 0 or user_choice > 2:
        print("无效选择，请重新选择。")
        return
    
    computer_choice = random.randint(0, 2)

    print(f"你选择了：{choices[user_choice]}")
    print(f"电脑选择了：{choices[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print("结果：", result)

if __name__ == "__main__":
    main()
