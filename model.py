import re

import sympy


def to_Standard_algebraic_expression(string, sub='^'):
	"""
	计算机形式转标准形式
	:param string: 传入计算机形式字符串算式
	:param sub: 要替换的上标符号(可省略)
	:return: 返回省略乘号后的标准字符串算式
	前：2*x+(-1)*3*x*(2+(-1)*2*x+2*x**2)
	后：2x-3x(2-2x+2x**2)
	前：(x+(-1)*2)*(x+(-1)*3)+(-1)*2*(x+5)*(x+(-1)*3)
	后：(x-2)(x-3)-2(x+5)(x-3)
	"""
	
	# 清除空格
	string = string.replace(' ', '')
	if sub != '**':
		# 省略乘号
		string = re.sub(r'(?<=[A-Za-z0-9\)])\*(?=[\(A-Za-z0-9])', '', string)
	# 将+(-1),转为-
	# string = re.sub(r'(?<=[A-Za-z0-9\)])\+\(\-1\)(?=[\(A-Za-z0-9])', '-', string)
	# 替换上标
	string = re.sub(r'(?<=[A-Za-z0-9\)])\*\*(?=[\(A-Za-z0-9])', sub, string)
	# 符号间添加空格
	string = re.sub(r'(?<=[\+\-\*=])(?=[\(A-Za-z0-9])', ' ', string)
	string = re.sub(r'(?<=[A-Za-z0-9\)])(?=[\+\-\*=])', ' ', string)
	string = re.sub(r'(?<==)- ', ' -', string)
	# string = re.sub(r'(?<=\()(?=[A-Za-z0-9\-])', ' ', string)
	# string = re.sub(r'(?<=[A-Za-z0-9])(?=\))', ' ', string)
	return string


def to_Computational_expressions(string):
	"""
	标准形式转计算机形式
	:param string: 传入标准形式字符串算式
	:return: 返回补充乘号后的字符串算式
	前：2x-3x(2-2x+2x**2)
	后：2*x+(-1)*3*x*(2+(-1)*2*x+2*x**2)
	前：(x-2)(x-3)-2(x+5)(x-3)
	后：(x+(-1)*2)*(x+(-1)*3)+(-1)*2*(x+5)*(x+(-1)*3)
	"""
	# 清除空格
	string = string.replace(' ', '')
	# 将-,转为+(-1)
	# string = re.sub(r'(?<=[A-Za-z0-9\)])-(?=[\(A-Za-z0-9])', '+(-1)', string)
	# 补充乘号
	string = re.sub(r'(?<=[A-Za-z0-9\)])(?=[\(A-Za-z0-9])', '*', string)
	# 将脱字符转换为乘方号
	string = re.sub(r'(?<=[A-Za-z0-9\)])\^(?=[\(A-Za-z0-9])', '**', string)
	return string


def get_Symbol(string):
	a = re.findall(r'[a-zA-z]', string)
	if a is not None:
		return list(set(a))
	else:
		return None


def subOfNumForLetter(expression: str, letter: str, num):
	"""
	对表达式中的字母带入数字
	:param expression: 被带入的表达式
	:param letter: 被带入的字母
	:param num: 要带入的数
	:return: 新表达式
	"""
	# 判断是否是有符号数
	if num < 0:
		# 给负数加括号
		num = '(' + str(num) + ')'
	
	expression = expression.replace(letter, str(num))
	return expression


def transposition(expression: str):
	"""
	# 移项，将方程一边变为‘=0’(不保留'=0')
	:param expression: 待移项表达式
	:return: 标准表达式
	"""
	if expression[-2:] == '=0':
		return expression[:-2]
	else:
		# 提取等号后部分加括号移至右侧
		eqPos = expression.find('=') + 1
		rightExpression = expression[eqPos:]
		expression = expression.replace(rightExpression, "")
		expression = expression[:eqPos - 1] + '-(' + rightExpression + ')'
	
	return expression


def getSymbol(string):
	a = re.findall(r'[a-zA-z]', string)
	if a is not None:
		return list(set(a))
	else:
		return None


def solveQuestions(expressions: list, letter: str):
	"""
	解方程
	:param expressions: 待解表达式列表
	:param letter: 未知字母，多个字母空一格
	:return: 字典解
	"""
	# 将方程转换为标准形式(移项)
	for n in range(len(expressions)):
		expressions[n] = transposition(expressions[n])
	
	# 声明未知数
	letter_l = getSymbol(letter)
	for i in letter_l:
		exec('' + i + ' = sympy.Symbol(\'' + i + '\')')
	
	# 字符串计算
	ex = []
	for n in range(len(expressions)):
		ex.append(eval(expressions[n]))
	
	le = []
	lel = letter.split(" ")
	for n in range(len(lel)):
		le.append(eval(lel[n]))
	
	# return sympy.solve([eval(expressions[0])], [eval(letter.split())])
	return sympy.solve(ex, le)


def coordinatesOnTheXY(expression: str):
	"""
	求一函数与x、y轴的交点坐标
	:param expression: 函数表达式 y=kx+b(y!=0)
	:return: [x轴交点：(x1, y1), y轴交点：(x2, y2)]
	"""
	pos_list = []
	# 求x轴交点，则y坐标为零
	expression1 = subOfNumForLetter(expression, 'y', 0)
	# 解方程，取x的解
	x1 = list(solveQuestions([expression1], 'x').items())[0][1]
	pos_list.append((x1, 0))
	
	# 求y轴交点，则x坐标为零
	expression2 = subOfNumForLetter(expression, 'x', 0)
	# 解方程，取y的解
	y2 = list(solveQuestions([expression2], 'y').items())[0][1]
	pos_list.append((0, y2))
	
	return pos_list


def judgeQuadrant(expression):
	"""
	判断一个函数的象限，(必须为标准形式)
	:param expression: 函数表达式
	:return: [是否为正比例函数, [k是否大于零, b是否大于零], [函数所经过的象限(数字表达)]]
	eg:[0, [1, 0] [1, 3, 4]]
	"""
	result = [0, [None, None], []]
	# 判断k是否大于零
	if expression[expression.find("=") + 1] == "-":
		result[1][0] = 0
	else:
		result[1][0] = 1
	
	# 判断关于k所经象限
	if result[1][0]:
		result[2].extend([1, 3])
	else:
		result[2].extend([2, 4])
	
	# 判断是否是正比例函数
	if expression.find("+") - expression.find("-") == 0:
		# 不含有+-号，为正比例函数
		result[0] = 1
	else:
		# 判断b是否大于零
		if expression[expression.find("x") + 1] == "-":
			result[1][1] = 0
		else:
			result[1][1] = 1
		
		# 判断关于b所经象限
		if result[1][1]:
			result[2].extend([1, 2])
		else:
			result[2].extend([3, 4])
	
	result[2] = list(set(result[2]))
	result[2].sort()
	return result


def computingIntersection(exp1, exp2):
	"""
	求两函数的交点
	:param exp1: 一次函数表达式1
	:param exp2: 一次函数表达式2
	:return: 交点坐标(x, y)
	"""
	# 解二元方程
	result = list(solveQuestions([exp1, exp2], "x y").items())
	return result[0][1], result[1][1]


def evalExpression(pos1, pos2=None):
	"""
	计算函数解析式
	:param pos1: 坐标一
	:param pos2: 坐标二(当函数为正比例函数时可不填)
	:return: 函数解析式
	"""
	# 判断是否为正比例函数
	if pos2 is None:
		# 构造方程
		exp1 = str(pos1[0]) + "*k=" + str(pos1[1])
		# 解一元方程
		return "y = " + str(list(solveQuestions([exp1], "k").items())[0][1]) + "x"
	else:
		# 构造方程1
		exp1 = str(pos1[0]) + "*k+b=" + str(pos1[1])
		# 构造方程2
		exp2 = str(pos2[0]) + "*k+b=" + str(pos2[1])
		# 解二元方程
		result = list(solveQuestions([exp1, exp2], "k b").items())
		return to_Standard_algebraic_expression("y = " + str(result[0][1]) + (
			("x " + str(result[1][1])) if str(result[1][1])[0] == "-" else ("x + " + str(result[1][1]))))


def completionExpression(exp, pos):
	"""
	补全函数表达式
	:param exp: 只有一个未知数的函数表达式 eg: y=2x+b
	:param pos: 一个在此函数上的完整坐标点
	:return: 完整表达式
	"""
	# 获得除x,y之外的未知数
	sym = get_Symbol(exp)
	sym.remove("x")
	sym.remove("y")
	sym = sym[0]
	
	# 将坐标分别带入表达式中的x,y
	exp1 = subOfNumForLetter(subOfNumForLetter(to_Computational_expressions(exp), "x", pos[0]), "y", pos[1])
	# 解一元方程
	result = list(solveQuestions([exp1], sym).items())[0][1]
	# 将未知数的解替换到原式中
	exp = to_Computational_expressions(exp.replace(sym, "(" + str(result) + ")"))
	# 化简(变号)后返回
	x = sympy.Symbol("x")
	return to_Standard_algebraic_expression("y = " + str(sympy.expand(eval(exp[exp.find("=") + 1:]))))


def completionCoordinate(exp, pos):
	"""
	补全坐标
	:param exp: 完整函数表达式
	:param pos: 只有一个未知数的坐标(未知数用None表示) eg: (2, None)
	:return: 完整坐标
	"""
	# 判断未知数是否在x坐标上
	if pos[0] is None:
		# 将x坐标带入表达式x中
		exp = subOfNumForLetter(to_Computational_expressions(exp), "y", pos[1])
		# 解一元方程
		return list(solveQuestions([exp], "x").items())[0][1], pos[1]
	else:
		# 将y坐标带入表达式y中
		exp = subOfNumForLetter(to_Computational_expressions(exp), "x", pos[0])
		# 解一元方程
		return pos[0], list(solveQuestions([exp], "y").items())[0][1]
		

if __name__ == "__main__":
	# 判断函数所经的象限
	print(judgeQuadrant("y=x-2"))
	# 计算函数在x,y轴的交点坐标
	print(coordinatesOnTheXY("y=x-2"))
	# 计算两函数的交点坐标
	print(computingIntersection("y=-x+3", to_Computational_expressions("y=3x-5")))
	# 求解函数表达式
	print(evalExpression((2, 4), (4, 3)))
	# 补全函数表达式
	print(completionExpression("y = 2x + b", (3, -2)))
	# 补全坐标
	print(completionCoordinate("y = 2x+5", (-2, None)))
