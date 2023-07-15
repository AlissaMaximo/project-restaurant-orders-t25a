from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    cheese_ball = Dish("bolinha de queijo", 1.05)
    coxinha = Dish("coxinha", 1.50)
    mozzarella_cheese = Ingredient("queijo mussarela")
    flour = Ingredient("farinha")

    cheese_ball.add_ingredient_dependency(mozzarella_cheese, 1)
    cheese_ball.add_ingredient_dependency(flour, 1)
    assert isinstance(cheese_ball, Dish)
    assert hash(cheese_ball) == hash(cheese_ball)
    assert hash(cheese_ball) != hash(coxinha)
    assert cheese_ball.__repr__() == "Dish('bolinha de queijo', R$1.05)"
    assert cheese_ball == Dish("bolinha de queijo", 1.05)
    assert coxinha != Dish("bolinha de queijo", 1.05)
    assert cheese_ball.get_ingredients() == {mozzarella_cheese, flour}
    assert cheese_ball.name == "bolinha de queijo"
    assert cheese_ball.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN,
        Restriction.LACTOSE,
    }
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("bolinha de queijo", -1.05)
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("bolinha de queijo", "fail type")
