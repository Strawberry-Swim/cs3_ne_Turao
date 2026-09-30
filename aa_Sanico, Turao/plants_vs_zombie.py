class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)

    def take_damage(self, zombie):
        self.health -= zombie.damage
        print(f"{self.name} took {zombie.damage} damage from {zombie.name}. Its health is now at {self.health}.")

    def attack(self, zombie):
        if self.health > 0 and zombie.health > 0:
            zombie.take_damage(self)
            print(f"{self.name} attacked {zombie.name} for {self.damage} damage.")


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = int(health)
        self.damage = int(damage)
        self.distance = int(distance)

    def take_damage(self, plant):
        self.health -= plant.damage
        print(f"{self.name} took {plant.damage} damage from {plant.name}. Its health is now at {self.health}.")

    def attack(self, plant):
        if plant.health <= 0:
            print(f"{plant.name} is already defeated.")
            return
        if self.distance <= 0:
            plant.take_damage(self)
        else:
            print(f"The zombie is too far away to attack {plant.name}!")

    def move(self):
        self.distance = max(0, self.distance - 1)


plant1 = Plant("Peeshooter", 150, 20)
plant2 = Plant("Wal-deez-nutz", 500, 1)
zombie1 = Zombie("Daddy Joemar", 1000, 30, 20)

turn = 1
while turn >= 1:
    print("\n")
    print(f"===[Turn #{turn}]===")
    plant1.attack(zombie1)
    plant2.attack(zombie1)
    zombie1.attack(plant1)
    if plant1.health <= 0:
        zombie1.attack(plant2)

    if plant1.health <= 0 and plant2.health <= 0:
        print("\n")
        print("---The zombies won!---")
        print("---Game Over---")
        break

    elif zombie1.health <= 0:
        print("\n")
        print("---The plants won!---")
        print("---Game Over---")
        break

    zombie1.move()
    turn += 1