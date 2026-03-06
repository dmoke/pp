Position = {"high": "h", "low": "l"}  # don't change this!


class Warrior:
    def __init__(self, name):
        # each warrior should be created with a name and 100 health points
        self.name = name
        self.health = 100
        # default guard is "", that is unguarded
        self.block = ""
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        # attacking high deals 10 damage, low 5
        # 0 damage if the enemy blocks in the same position
        damage = 0

        if enemy.block != position:
            damage += 10 if position == Position["high"] else 5

        # extra damage if not blocking at all
        if enemy.block == "":
            damage += 5

        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):

        if new_health <= 0:
            if self.deceased:
                self.zombie = True

            self.deceased = True
            self.health = 0
        else:
            self.health = new_health


def main():

    ninja = Warrior("Hanzo Hattori")
    samurai = Warrior("Ryoma Sakamoto")

    samurai.block = "l"
    ninja.attack(samurai, "h")

    print(samurai.health)


if __name__ == "__main__":
    main()