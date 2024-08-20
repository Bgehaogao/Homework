def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "错误"
    return x / y

def calculator():

    choice = input("请输入你的选择(add/minus/multiply/divide): ")

    if choice in ["add", "minus", "multiply", "divide"]:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))

        if choice == "add":
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == "minus":
            print(f"{num1} - {num2} = {minus(num1, num2)}")

        elif choice == "multiply":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == "divide":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("无效输入")

# 运行计算器
calculator()
