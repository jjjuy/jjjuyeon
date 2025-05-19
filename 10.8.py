class Counter:
    def __init__(self, number=0):
        if number >= 100 or number <= -1:
            self.__number = 0
        else:
            self.__number = number
            
    def reset(self):
        self.__number = 0
    
    def inc(self):
        self.__number += 1
        if self.__number >= 100:
            self.__number = 0

    def dec(self):
        self.__number -= 1
        if self.__number <= -1:
            self.__number = 0

    def __add__(self, other):
        if isinstance(other, Counter):
            result = self.__number + other.__number
            if result >= 100:
                result = 0
            return Counter.__from_number(result)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Counter):
            result = self.__number - other.__number
            return Counter.__from_number(result, bypass_limit=True)
        return NotImplemented

    def __str__(self):
        return f"C({self.__number})"

    @classmethod
    def __from_number(cls, number, bypass_limit=False):
        obj = cls()
        if bypass_limit:
            obj.__number = number
        else:
            if number >= 100 or number <= -1:
                obj.__number = 0
            else:
                obj.__number = number
        return obj


# 테스트 코드
c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2

print("c3 =", c3)  # C(30)
print("c4 =", c4)  # C(-10)
