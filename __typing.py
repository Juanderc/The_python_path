import math
import inspect
from typing import Dict, List, Tuple, Sequence

# typing allows us to expecified the type value of an args in a function
# def func(arg: arg_type, optarg: arg_type = default) -> return_type:

users_name: List[str] = ["Phenelope", "Daniel", "Heaven"]
users_age: Tuple[int, int, int] = (23, 45, 25)
users_available: Dict[str, bool] = {
    "Daniel": True, "Phenelope": False, "Heaven": False}

likes: Sequence[str] = []  # it take a secuence not matter which
# likes: Secuence[str] = ()
# likes: Secuence[str] = {}


def Returned(name: str, age: int, likes: list) -> str:
    return("Hello {}, you have {} years old and your likes are: {}".format(name, age, likes))


def Root(number: float) -> float:
    return math.sqrt(number)


print(Returned("Jose", 23, ["Sing", "Soccer"]))
print(Root(7))

# use mypy to check the true use of the args
# intall it using pip install mypy

print(inspect.get_annotations(Returned))
