



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_game_response import CreateGameResponse
    from .join_game_response import JoinGameResponse
    from .subscribe_to_game_events_response_item import SubscribeToGameEventsResponseItem
    from .subscribe_to_game_events_response_item_data import SubscribeToGameEventsResponseItemData
    from .subscribe_to_game_events_response_item_data_event import SubscribeToGameEventsResponseItemDataEvent
    from .subscribe_to_game_events_response_item_eight import SubscribeToGameEventsResponseItemEight
    from .subscribe_to_game_events_response_item_eight_event import SubscribeToGameEventsResponseItemEightEvent
    from .subscribe_to_game_events_response_item_five import SubscribeToGameEventsResponseItemFive
    from .subscribe_to_game_events_response_item_five_event import SubscribeToGameEventsResponseItemFiveEvent
    from .subscribe_to_game_events_response_item_four import SubscribeToGameEventsResponseItemFour
    from .subscribe_to_game_events_response_item_four_event import SubscribeToGameEventsResponseItemFourEvent
    from .subscribe_to_game_events_response_item_nine import SubscribeToGameEventsResponseItemNine
    from .subscribe_to_game_events_response_item_nine_event import SubscribeToGameEventsResponseItemNineEvent
    from .subscribe_to_game_events_response_item_one import SubscribeToGameEventsResponseItemOne
    from .subscribe_to_game_events_response_item_one_event import SubscribeToGameEventsResponseItemOneEvent
    from .subscribe_to_game_events_response_item_seven import SubscribeToGameEventsResponseItemSeven
    from .subscribe_to_game_events_response_item_seven_event import SubscribeToGameEventsResponseItemSevenEvent
    from .subscribe_to_game_events_response_item_six import SubscribeToGameEventsResponseItemSix
    from .subscribe_to_game_events_response_item_six_event import SubscribeToGameEventsResponseItemSixEvent
    from .subscribe_to_game_events_response_item_ten import SubscribeToGameEventsResponseItemTen
    from .subscribe_to_game_events_response_item_ten_event import SubscribeToGameEventsResponseItemTenEvent
    from .subscribe_to_game_events_response_item_three import SubscribeToGameEventsResponseItemThree
    from .subscribe_to_game_events_response_item_three_event import SubscribeToGameEventsResponseItemThreeEvent
    from .subscribe_to_game_events_response_item_two import SubscribeToGameEventsResponseItemTwo
    from .subscribe_to_game_events_response_item_two_event import SubscribeToGameEventsResponseItemTwoEvent
    from .subscribe_to_game_events_response_item_zero import SubscribeToGameEventsResponseItemZero
    from .subscribe_to_game_events_response_item_zero_event import SubscribeToGameEventsResponseItemZeroEvent
    from .test_solution_response import TestSolutionResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateGameResponse": ".create_game_response",
    "JoinGameResponse": ".join_game_response",
    "SubscribeToGameEventsResponseItem": ".subscribe_to_game_events_response_item",
    "SubscribeToGameEventsResponseItemData": ".subscribe_to_game_events_response_item_data",
    "SubscribeToGameEventsResponseItemDataEvent": ".subscribe_to_game_events_response_item_data_event",
    "SubscribeToGameEventsResponseItemEight": ".subscribe_to_game_events_response_item_eight",
    "SubscribeToGameEventsResponseItemEightEvent": ".subscribe_to_game_events_response_item_eight_event",
    "SubscribeToGameEventsResponseItemFive": ".subscribe_to_game_events_response_item_five",
    "SubscribeToGameEventsResponseItemFiveEvent": ".subscribe_to_game_events_response_item_five_event",
    "SubscribeToGameEventsResponseItemFour": ".subscribe_to_game_events_response_item_four",
    "SubscribeToGameEventsResponseItemFourEvent": ".subscribe_to_game_events_response_item_four_event",
    "SubscribeToGameEventsResponseItemNine": ".subscribe_to_game_events_response_item_nine",
    "SubscribeToGameEventsResponseItemNineEvent": ".subscribe_to_game_events_response_item_nine_event",
    "SubscribeToGameEventsResponseItemOne": ".subscribe_to_game_events_response_item_one",
    "SubscribeToGameEventsResponseItemOneEvent": ".subscribe_to_game_events_response_item_one_event",
    "SubscribeToGameEventsResponseItemSeven": ".subscribe_to_game_events_response_item_seven",
    "SubscribeToGameEventsResponseItemSevenEvent": ".subscribe_to_game_events_response_item_seven_event",
    "SubscribeToGameEventsResponseItemSix": ".subscribe_to_game_events_response_item_six",
    "SubscribeToGameEventsResponseItemSixEvent": ".subscribe_to_game_events_response_item_six_event",
    "SubscribeToGameEventsResponseItemTen": ".subscribe_to_game_events_response_item_ten",
    "SubscribeToGameEventsResponseItemTenEvent": ".subscribe_to_game_events_response_item_ten_event",
    "SubscribeToGameEventsResponseItemThree": ".subscribe_to_game_events_response_item_three",
    "SubscribeToGameEventsResponseItemThreeEvent": ".subscribe_to_game_events_response_item_three_event",
    "SubscribeToGameEventsResponseItemTwo": ".subscribe_to_game_events_response_item_two",
    "SubscribeToGameEventsResponseItemTwoEvent": ".subscribe_to_game_events_response_item_two_event",
    "SubscribeToGameEventsResponseItemZero": ".subscribe_to_game_events_response_item_zero",
    "SubscribeToGameEventsResponseItemZeroEvent": ".subscribe_to_game_events_response_item_zero_event",
    "TestSolutionResponse": ".test_solution_response",
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
