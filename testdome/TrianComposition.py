### Trian Composition

# 오류 답안 → List를 사용하면 시간 초과


class TrainComposition:
    def __init__(self):
        self.train = []

    def attach_wagon_from_left(self, wagonId):
        # self.train = [wagonId] + self.train
        self.train.insert(0, wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.train.append(wagonId)

    def detach_wagon_from_left(self):
        return self.train.pop(0) if self.train else None

    def detach_wagon_from_right(self):
        return self.train.pop(-1) if self.train else None


## 수정 답안
from collections import deque


class TrainComposition:
    def __init__(self):
        self.train = deque()

    def attach_wagon_from_left(self, wagonId):
        # self.train = [wagonId] + self.train
        self.train.insert(0, wagonId)

    def attach_wagon_from_right(self, wagonId):
        self.train.append(wagonId)

    def detach_wagon_from_left(self):
        return self.train.popleft() if self.train else None

    def detach_wagon_from_right(self):
        return self.train.pop() if self.train else None


if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right())  # should print 7
    print(train.detach_wagon_from_left())  # should print 13
