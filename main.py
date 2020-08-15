import model

welcome_text = """---功能有：
    1. 解多元方程
    2. 求一函数与x、y轴的交点坐标
    3. 判断函数所经的象限
    4. 计算两函数的交点坐标
    5. 求解函数表达式
    6. 补全函数表达式
    7. 补全坐标
    0. 显示此帮助信息
    """

if __name__ == "__main__":
    print("-----------------------叮！欢迎来到一次函数计算辅助系统")
    print(welcome_text)

    while True:
        command = input("\n键入命令>>>")

        if command == "1":
            print("\n------解多元方程")
            print("---输入的方程数请与未知数数量对应哦！")

            n = 1
            expressions = []
            letters = ""
            while True:
                expressions.append(input("---请输入方程组中的第" + str(n) + "个方程(输入0结束):"))
                if expressions[-1] == "0":
                    expressions = expressions[:-1]
                    break
                n += 1

            letters = input("---请输入未知数字母(多个请用空格隔开)：")
            print("\n---结果：" + str(model.solveQuestions(expressions, letters)))

        elif command == "2":
            print("\n------求一函数与x、y轴的交点坐标")
            expression = input("---请输入一次函数表达式eg:y=kx+b(k!=0)：")
            result = model.coordinatesOnTheXY(expression)
            print("\n---结果：与x轴交点坐标：" + str(result[0]) + "\n　　     与y轴交点坐标：" + str(result[1]))

        elif command == "3":
            print("\n------判断函数所经的象限")
            expression = input("---请输入一次函数表达式eg:y=kx+b(k!=0)：")
            result = model.judgeQuadrant(expression)
            if result[0]:
                print("\n---结果：此函数是正比例函数")
            else:
                print("\n---结果：此函数是一次函数")

            if result[1][0]:
                print("   　　　k > 0; ", end="")
                if result[1][1]:
                    print("b > 0")
                elif result[1][1] is not None:
                    print("b < 0")
                else:
                    print()
            else:
                print("   　　　k < 0; ", end="")
                if result[1][1]:
                    print("b > 0")
                elif result[1][1] is not None:
                    print("b < 0")
                else:
                    print()
            print("   　　　此函数经过第" + ", ".join(map(lambda x: str(x), result[2])) + "象限")

        elif command == "4":
            print("\n------计算两函数的交点坐标")
            exp1 = input("---请输入第1个一次函数表达式:")
            exp2 = input("---请输入第2个一次函数表达式:")
            print("\n---结果:交点坐标为：" + str(model.computingIntersection(exp1, exp2)))

        elif command == "5":
            print("\n------求解函数表达式")
            pos1 = list(map(lambda x: int(x), input("请输入第1个坐标点(x、y用空格隔开)eg:2 4：").split(" ")))
            pos2 = list(map(lambda x: int(x), input("请输入第2个坐标点(x、y用空格隔开)eg:4 3：").split(" ")))
            print("\n---结果：此函数的表达式为：" + str(model.evalExpression(pos1, pos2)))

        elif command == "6":
            print("\n------补全函数表达式")
            exp = input("---请输入仅有一个未知数的一次函数表达式 eg: y=kx+1：")
            pos = list(map(lambda x: int(x), input("---请输入此函数经过的一个完整坐标(x、y用空格隔开)eg:1 2：").split(" ")))
            print("\n---结果：此函数的表达式为：" + str(model.completionExpression(exp, pos)))

        elif command == "7":
            print("\n------补全坐标")
            exp = input("---请输入一个完整的一次函数表达式 eg: y=2x+4：")
            pos = input("---请输入仅含有一个未知数的坐标(未知数用x表示，x、y用空格隔开) eg:2 x：").split(" ")
            if pos[0] == "x":
                pos = (None, int(pos[1]))
            else:
                pos = (int(pos[0]), None)
            print("\n---结果：完整坐标为：" + str(model.completionCoordinate(exp, pos)))

        elif command == "0":
            print("\n" + welcome_text)

        else:
            print("\n---您输入的命令未能识别，请查阅功能表后再试")
            print(welcome_text)





















