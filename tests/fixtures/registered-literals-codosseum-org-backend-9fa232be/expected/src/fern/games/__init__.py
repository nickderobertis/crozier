



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateGameResponse,
        JoinGameResponse,
        SubscribeToGameEventsResponseItem,
        SubscribeToGameEventsResponseItemData,
        SubscribeToGameEventsResponseItemDataEvent,
        SubscribeToGameEventsResponseItemEight,
        SubscribeToGameEventsResponseItemEightEvent,
        SubscribeToGameEventsResponseItemFive,
        SubscribeToGameEventsResponseItemFiveEvent,
        SubscribeToGameEventsResponseItemFour,
        SubscribeToGameEventsResponseItemFourEvent,
        SubscribeToGameEventsResponseItemNine,
        SubscribeToGameEventsResponseItemNineEvent,
        SubscribeToGameEventsResponseItemOne,
        SubscribeToGameEventsResponseItemOneEvent,
        SubscribeToGameEventsResponseItemSeven,
        SubscribeToGameEventsResponseItemSevenEvent,
        SubscribeToGameEventsResponseItemSix,
        SubscribeToGameEventsResponseItemSixEvent,
        SubscribeToGameEventsResponseItemTen,
        SubscribeToGameEventsResponseItemTenEvent,
        SubscribeToGameEventsResponseItemThree,
        SubscribeToGameEventsResponseItemThreeEvent,
        SubscribeToGameEventsResponseItemTwo,
        SubscribeToGameEventsResponseItemTwoEvent,
        SubscribeToGameEventsResponseItemZero,
        SubscribeToGameEventsResponseItemZeroEvent,
        TestSolutionResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateGameResponse": ".types",
    "JoinGameResponse": ".types",
    "SubscribeToGameEventsResponseItem": ".types",
    "SubscribeToGameEventsResponseItemData": ".types",
    "SubscribeToGameEventsResponseItemDataEvent": ".types",
    "SubscribeToGameEventsResponseItemEight": ".types",
    "SubscribeToGameEventsResponseItemEightEvent": ".types",
    "SubscribeToGameEventsResponseItemFive": ".types",
    "SubscribeToGameEventsResponseItemFiveEvent": ".types",
    "SubscribeToGameEventsResponseItemFour": ".types",
    "SubscribeToGameEventsResponseItemFourEvent": ".types",
    "SubscribeToGameEventsResponseItemNine": ".types",
    "SubscribeToGameEventsResponseItemNineEvent": ".types",
    "SubscribeToGameEventsResponseItemOne": ".types",
    "SubscribeToGameEventsResponseItemOneEvent": ".types",
    "SubscribeToGameEventsResponseItemSeven": ".types",
    "SubscribeToGameEventsResponseItemSevenEvent": ".types",
    "SubscribeToGameEventsResponseItemSix": ".types",
    "SubscribeToGameEventsResponseItemSixEvent": ".types",
    "SubscribeToGameEventsResponseItemTen": ".types",
    "SubscribeToGameEventsResponseItemTenEvent": ".types",
    "SubscribeToGameEventsResponseItemThree": ".types",
    "SubscribeToGameEventsResponseItemThreeEvent": ".types",
    "SubscribeToGameEventsResponseItemTwo": ".types",
    "SubscribeToGameEventsResponseItemTwoEvent": ".types",
    "SubscribeToGameEventsResponseItemZero": ".types",
    "SubscribeToGameEventsResponseItemZeroEvent": ".types",
    "TestSolutionResponse": ".types",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CreateGameResponse",
    "JoinGameResponse",
    "SubscribeToGameEventsResponseItem",
    "SubscribeToGameEventsResponseItemData",
    "SubscribeToGameEventsResponseItemDataEvent",
    "SubscribeToGameEventsResponseItemEight",
    "SubscribeToGameEventsResponseItemEightEvent",
    "SubscribeToGameEventsResponseItemFive",
    "SubscribeToGameEventsResponseItemFiveEvent",
    "SubscribeToGameEventsResponseItemFour",
    "SubscribeToGameEventsResponseItemFourEvent",
    "SubscribeToGameEventsResponseItemNine",
    "SubscribeToGameEventsResponseItemNineEvent",
    "SubscribeToGameEventsResponseItemOne",
    "SubscribeToGameEventsResponseItemOneEvent",
    "SubscribeToGameEventsResponseItemSeven",
    "SubscribeToGameEventsResponseItemSevenEvent",
    "SubscribeToGameEventsResponseItemSix",
    "SubscribeToGameEventsResponseItemSixEvent",
    "SubscribeToGameEventsResponseItemTen",
    "SubscribeToGameEventsResponseItemTenEvent",
    "SubscribeToGameEventsResponseItemThree",
    "SubscribeToGameEventsResponseItemThreeEvent",
    "SubscribeToGameEventsResponseItemTwo",
    "SubscribeToGameEventsResponseItemTwoEvent",
    "SubscribeToGameEventsResponseItemZero",
    "SubscribeToGameEventsResponseItemZeroEvent",
    "TestSolutionResponse",
]
