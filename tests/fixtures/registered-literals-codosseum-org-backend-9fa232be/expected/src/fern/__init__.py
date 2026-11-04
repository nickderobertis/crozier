



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        EliminatedEvent,
        Game,
        GameMode,
        GameOverEvent,
        GameSettings,
        GameState,
        GameUpdateEvent,
        Player,
        PlayerCodeRevealEvent,
        PlayerFinishEvent,
        PlayerGameResult,
        PlayerJoinEvent,
        PlayerLeaveEvent,
        PlayerRoundResult,
        PlayerRoundResultScore,
        PlayerSubmitEvent,
        Players,
        Round,
        RoundStartEvent,
        Submission,
        SyncEvent,
        TestResultEvent,
        TestResultEventResult,
    )
    from .errors import BadRequestError, ConflictError, ForbiddenError, NotFoundError, UnauthorizedError
    from . import games
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .games import (
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
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "CreateGameResponse": ".games",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EliminatedEvent": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "Game": ".types",
    "GameMode": ".types",
    "GameOverEvent": ".types",
    "GameSettings": ".types",
    "GameState": ".types",
    "GameUpdateEvent": ".types",
    "JoinGameResponse": ".games",
    "NotFoundError": ".errors",
    "Player": ".types",
    "PlayerCodeRevealEvent": ".types",
    "PlayerFinishEvent": ".types",
    "PlayerGameResult": ".types",
    "PlayerJoinEvent": ".types",
    "PlayerLeaveEvent": ".types",
    "PlayerRoundResult": ".types",
    "PlayerRoundResultScore": ".types",
    "PlayerSubmitEvent": ".types",
    "Players": ".types",
    "Round": ".types",
    "RoundStartEvent": ".types",
    "Submission": ".types",
    "SubscribeToGameEventsResponseItem": ".games",
    "SubscribeToGameEventsResponseItemData": ".games",
    "SubscribeToGameEventsResponseItemDataEvent": ".games",
    "SubscribeToGameEventsResponseItemEight": ".games",
    "SubscribeToGameEventsResponseItemEightEvent": ".games",
    "SubscribeToGameEventsResponseItemFive": ".games",
    "SubscribeToGameEventsResponseItemFiveEvent": ".games",
    "SubscribeToGameEventsResponseItemFour": ".games",
    "SubscribeToGameEventsResponseItemFourEvent": ".games",
    "SubscribeToGameEventsResponseItemNine": ".games",
    "SubscribeToGameEventsResponseItemNineEvent": ".games",
    "SubscribeToGameEventsResponseItemOne": ".games",
    "SubscribeToGameEventsResponseItemOneEvent": ".games",
    "SubscribeToGameEventsResponseItemSeven": ".games",
    "SubscribeToGameEventsResponseItemSevenEvent": ".games",
    "SubscribeToGameEventsResponseItemSix": ".games",
    "SubscribeToGameEventsResponseItemSixEvent": ".games",
    "SubscribeToGameEventsResponseItemTen": ".games",
    "SubscribeToGameEventsResponseItemTenEvent": ".games",
    "SubscribeToGameEventsResponseItemThree": ".games",
    "SubscribeToGameEventsResponseItemThreeEvent": ".games",
    "SubscribeToGameEventsResponseItemTwo": ".games",
    "SubscribeToGameEventsResponseItemTwoEvent": ".games",
    "SubscribeToGameEventsResponseItemZero": ".games",
    "SubscribeToGameEventsResponseItemZeroEvent": ".games",
    "SyncEvent": ".types",
    "TestResultEvent": ".types",
    "TestResultEventResult": ".types",
    "TestSolutionResponse": ".games",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "games": ".games",
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
    "AsyncFernApi",
    "BadRequestError",
    "ConflictError",
    "CreateGameResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EliminatedEvent",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "Game",
    "GameMode",
    "GameOverEvent",
    "GameSettings",
    "GameState",
    "GameUpdateEvent",
    "JoinGameResponse",
    "NotFoundError",
    "Player",
    "PlayerCodeRevealEvent",
    "PlayerFinishEvent",
    "PlayerGameResult",
    "PlayerJoinEvent",
    "PlayerLeaveEvent",
    "PlayerRoundResult",
    "PlayerRoundResultScore",
    "PlayerSubmitEvent",
    "Players",
    "Round",
    "RoundStartEvent",
    "Submission",
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
    "SyncEvent",
    "TestResultEvent",
    "TestResultEventResult",
    "TestSolutionResponse",
    "UnauthorizedError",
    "__version__",
    "games",
]
