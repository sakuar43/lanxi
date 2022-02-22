import json


class Student(object):
    def __init__(self, name, age, score):
        self.score = score
        self.name = name
        self.age = age


def exchange(self):
    return {
        'name': self.name,
        'age': self.age,
        'score': self.score
    }


s = Student('zs', 80, 90)
print(json.dumps(s, default=exchange))
print(json.dumps(s,default=lambda obj:obj.__dict__))
#序列化从而符合web标准，json模块 dumps（）和loads（）函数接口