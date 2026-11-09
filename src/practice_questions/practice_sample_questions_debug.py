# Q1
spam = [19, 34, 88, 98, 3]
for i in range(len(spam)):
    try:
        result = spam[i]
        assert result > 10, "spam value can not be less 10"
    except Exception as e:
        print(e)


# Q2
try:
    eggs = "HELLo"
    bacon = "hello"
    assert eggs.lower() != bacon.lower(), "eggs and bacon is equal"
except Exception as e:
    print(e)


# Q3
try:
    assert True == False, "True is never equal to False"
except Exception as e:
    print(e)


# Q4
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s -  %(message)s"
)
