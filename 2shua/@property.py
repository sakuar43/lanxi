class Student(object):
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score mst between 1 and 100')
        self.score = value
class Student(object):
 @property
 def score(self):
    return self._score
 @score.setter
 def score(self, value):
    if not isinstance(value, int):
        raise ValueError('score must be an integer!')
    if value < 0 or value > 100:
        raise ValueError('score must between 0 ~ 100!')
    self._score = value
s = Student(60)
print(s.set_score(9999))
s.get_score()
