#클래스

class Unit:
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

m1=Unit("마린", 40, 5)
m2=Unit("마린", 40, 5)
tank1= Unit("탱크", 150, 35)