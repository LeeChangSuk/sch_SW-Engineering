# 간단한 계산기 예제
class Calculator:

    def init():
        result = 0
    # 더하기
    def adder(x, y):
        result = x + y
        return result
    
    def adder(x, y, z):
        result = x + y + z
        return result
    # 빼기
    def substract(x, y):
        result = x - y
        return result
    def substract(x, y, z):
        result = x - y - z
        return result
    # 곱하기(version1에서 추가된 기능)
    def mult(x, y):
        result = x * y
        return result

Calculator.init()
x = 10
y = 20
z = 50
print(Calculator.adder(x, y, z))
