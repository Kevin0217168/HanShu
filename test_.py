import random
import model
import pytest


str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890,.[];'{ }:\"<>+=-/*&^%%$#@!()}~`|?"

charLists = []
for i in range(100):
	charLists.append([str1[random.randint(0, 94)] for i in range(random.randint(1, 100))])


@pytest.mark.parametrize("charList", charLists)
def test_get_Sympol(charList):
	letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	charList = model.get_Symbol("".join(charList))
	for i in charList:
		assert i in letters

	
