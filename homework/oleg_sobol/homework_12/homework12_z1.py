class Flower:
    def __init__(self, name, color, stem_length, lifespan, price):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.lifespan = lifespan
        self.price = price


class Rose(Flower):
    pass


class Tulip(Flower):
    pass


class Lily(Flower):
    pass


class Daisy(Flower):
    pass


class Sunflower(Flower):
    pass


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def calculate_avg_lifespan(self):
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_lifespan(self):
        self.flowers.sort(key=lambda flower: flower.lifespan)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def find_by_lifespan(self, lifespan):
        return [flower for flower in self.flowers if flower.lifespan == lifespan]


rose = Rose(name="Роза", color="Красный", stem_length=50, lifespan=7, price=100)
tulip = Tulip(name="Тюльпан", color="Желтый", stem_length=40, lifespan=5, price=70)
lily = Lily(name="Лилия", color="Белый", stem_length=60, lifespan=8, price=120)
daisy = Daisy(name="Ромашка", color="Белый", stem_length=30, lifespan=6, price=50)
sunflower = Sunflower(name="Подсолнух", color="Желтый", stem_length=70, lifespan=10, price=150)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(lily)
bouquet.add_flower(daisy)
bouquet.add_flower(sunflower)
