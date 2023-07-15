from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    mozzarella_cheese = Ingredient("queijo mussarela")
    flour = Ingredient("farinha")

    assert mozzarella_cheese == Ingredient("queijo mussarela")
    assert isinstance(mozzarella_cheese, Ingredient)
    assert mozzarella_cheese.name == "queijo mussarela"
    assert hash(mozzarella_cheese) != hash(flour)
    assert hash(mozzarella_cheese) == hash(mozzarella_cheese)
    assert mozzarella_cheese.__repr__() == "Ingredient('queijo mussarela')"
    assert mozzarella_cheese.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
