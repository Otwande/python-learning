class Food:
    def __init__(self, category, meal_time, cost):
        self.category = category
        self.meal_time = meal_time
        self.cost = cost

    def food_type(self):
        print("The meal is a", self.category, "and it is ideal for", self.meal_time, "and it costs", self.cost)

class Cakes(Food):
    def __init__(self, category, meal_time, cost):
        super().__init__(category, meal_time, cost)

Blackforest = Cakes("snacks", "break_time", 100)
Blackforest.food_type()

class Cookies(Food):
    def __init__(self, category, meal_time, cost):
        super().__init__(category, meal_time, cost)

weed_cookie = Cookies("snack", "anytime", 100)
weed_cookie.food_type()
