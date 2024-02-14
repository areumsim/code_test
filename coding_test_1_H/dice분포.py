class Dice:
    @staticmethod
    def toss():
        while True:
            t = sum([2**i * Coin.toss() for i in range(3)])
            if t < 7 and t > 0:
                return t


# - 분포 오류
class Dice:
    @staticmethod
    def toss():

        total = 0
        for _ in range(3):
            total = (total << 1) | Coin.toss()

        return total % 6 + 1
