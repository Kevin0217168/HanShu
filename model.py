import sympy


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
		return expression[-2:]
	else:
		# 提取等号后部分加括号移至右侧
		eqPos = expression.find('=') + 1
		rightExpression = expression[eqPos:]
		expression = expression.replace(rightExpression, "")
		expression = expression[:eqPos - 1] + '-(' + rightExpression + ')'
	
	return expression


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
	exec(letter.replace(" ", ", ") + " = sympy.Symbol('" + letter + "')")
	
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


if __name__ == "__main__":
	print(coordinatesOnTheXY("y=x-2"))
