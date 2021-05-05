# Игра "Civilization 6"

class unit:
    name = "name"
    movement = 0
    health = 0
    status = "Alive"

    def move (self, n):
        if self.movement >= n:
            self.movement -= n

    def check_health(self):
        if self.health <= 0:
            self.status = "Dead"


class military_unit (unit):
    damage = 0
    def set(self, name, movement, health, damage):
        self.name = name
        self.movement = movement
        self.health = health
        self.damage = damage


class close_combat (military_unit):
    def attack(self, enemy):
        if self.status == "Alive" and self.movement >= 0:
            enemy.health -= self.damage
            self.health -= enemy.damage // 2
            self.movement = 0


class long_range_combat (military_unit):
    def attack (self, enemy):
        if self.status == "Alive" and self.movement >= 0:
            enemy.health -= self.damage
            self.movement = 0


class civil_unit(unit):
    def set(self, name, movement, health):
        self.name = name
        self.movement = movement
        self.health = health
    def bild(self, k):
        if self.movement >= k and self.health >= k:
            self.movement -= k
            self.health -= k

bilder = civil_unit ()
bilder.set("Bilder", 3, 3)
bilder.move(3)
bilder.bild(1)
bilder.check_health()


print (bilder.name + " " + str(bilder.movement) + " " + str(bilder.health) + " " + bilder.status)

shooter = long_range_combat()
kopeishik = close_combat()
shooter.set("Shooter", 3, 25, 10)
kopeishik.set("Kopeishik", 4, 20, 15)
shooter.move(1)
shooter.attack (kopeishik)
kopeishik.attack (shooter)
shooter.check_health()
kopeishik.check_health()

print (shooter.name + " " + str(shooter.movement) + " " + str(shooter.health) + " " + shooter.status)
print (kopeishik.name + " " + str(kopeishik.movement) + " " + str(kopeishik.health) + " " + kopeishik.status)

