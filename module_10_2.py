from threading import Thread
from time import sleep


class Knight(Thread):
    count_of_days = 0

    def __init__(self, name, power, warrior_num: int = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.warrior_num = warrior_num


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warrior_num > 0:
            self.warrior_num = self.warrior_num - self.power
            self.count_of_days += 1
            sleep(1)
            print(f'{self.name} сражается {self.count_of_days} дней, осталось {self.warrior_num} воинов.\n')
        print(f'{self.name} одержал победу спустя {self.count_of_days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20, 180)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
