class Hero:
def init(self, name, health, attack_power, defense):
self.name = name
self.health = health
self._initial_health = health # Початкове здоров'я
self.attack_power = attack_power
self.defense = defense
print(f"Герой {self.name} створений!")

# Атака іншого героя
def attack(self, target):
    damage = max(0, self.attack_power - target.defense)
    print(f"{self.name} атакує {target.name} і завдає {damage} урону!")
    target.take_damage(damage)

# Отримання урону
def take_damage(self, amount):
    self.health -= amount
    print(f"{self.name} отримує {amount} урону. Залишилось здоров'я: {self.health}")
    if not self.is_alive():
        print(f"{self.name} переможений!")

# Перевірка, чи герой живий
def is_alive(self):
    return self.health > 0

# Вивід характеристик героя
def get_stats(self):
    print(f"=== {self.name} ===")
    print(f"HP: {max(0, self.health)}/{self._initial_health}")
    print(f"Атака: {self.attack_power}")
    print(f"Захист: {self.defense}")

# Приватний метод лікування
def _heal(self, amount):
    self.health = min(self._initial_health, self.health + amount)
    print(f"{self.name} лікується на {amount}. Поточне здоров'я: {self.health}")
