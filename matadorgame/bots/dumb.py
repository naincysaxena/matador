import random
from base import Bot

class DumbBot(Bot):
    def guess(self, game):
        number = ''
        rand = random.Random()
        for i in range(4):
            number += str(rand.randint(0, 9))
        return number