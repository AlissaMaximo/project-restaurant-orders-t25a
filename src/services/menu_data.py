# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        self.process_base_data(source_path)

    def process_base_data(self, source_path):
        with open(source_path, encoding="utf-8") as file:
            current_dish = ""
            processed_dishes = []

            for attribute in csv.DictReader(file):
                # https://docs.python.org/3/library/csv.html
                # dish,price,ingredient,recipe_amount
                # lasanha presunto,25.90,queijo mussarela,15
                if current_dish == attribute["dish"]:
                    processed_dishes[-1].add_ingredient_dependency(
                        Ingredient(attribute["ingredient"]),
                        int(attribute["recipe_amount"]),
                    )

                else:
                    current_dish = attribute["dish"]
                    new_current_dish = Dish(
                        attribute["dish"], float(attribute["price"])
                    )
                    new_current_dish.add_ingredient_dependency(
                        Ingredient(attribute["ingredient"]),
                        int(attribute["recipe_amount"]),
                    )

                    processed_dishes.append(new_current_dish)

                for processed_dish in processed_dishes:
                    self.dishes.add(processed_dish)
