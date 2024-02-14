# list 점수 구하기 (3개씩)


class MovingTotal:
    def __init__(self):
        self.sumLst = set()
        self.lst = []

    def append(self, numbers):
        for num in numbers:
            self.lst.append(num)

            if len(self.lst) == 3:
                self.sumLst.add(sum(self.lst))
                self.lst.pop(0)

    def contains(self, total):
        if total in self.sumLst:
            return True
        else:
            return False


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
