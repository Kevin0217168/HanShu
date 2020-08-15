# 一次函数辅助程序

版本：0.2.1    最后更新：2020/8/15 18:50

全部由python编写，不依赖外部库的核心模块，实现对一次函数的辅助计算
具有解多元方程、坐标和函数补全、求解析式、求相交坐标等功能

> 注意：此程序仅用于验算，请勿依赖

## 更新项目
- 解决github上的问题
    - 对带有分数的函数，计算结果输出进行优化
    - 在所有方法内添加算式转换计算机标准函数
    
## 目前功能
- 解多元方程
- 方程移项
- 字母带入
- 求一函数与x、y轴的交点坐标
- 判断函数所经的象限
- 计算两函数的交点坐标
- 求解函数表达式
- 补全函数表达式
- 补全坐标

## 示例代码
```python
# 判断函数所经的象限
print(judgeQuadrant("y=x-2"))
# return: [0, [1, 0], [1, 3, 4]]

# 计算函数在x,y轴的交点坐标
print(coordinatesOnTheXY("y=x-2"))
# return: [(2, 0), (0, -2)]

# 计算两函数的交点坐标
print(computingIntersection("y=-x+3", "y=3x-5"))
# return: (2, 1)

# 求解函数表达式
print(evalExpression((2, 4), (4, 3)))
# return: y = -1/2x + 5

# 补全函数表达式
print(completionExpression("y = 2x + b", (3, -2)))
# return: y = 2x - 8

# 补全坐标
print(completionCoordinate("y = 2x+5", (-2, None)))
# return: (-2, 1)

```
