



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .eliminated_event import EliminatedEvent
    from .game import Game
    from .game_mode import GameMode
    from .game_over_event import GameOverEvent
    from .game_settings import GameSettings
    from .game_state import GameState
    from .game_update_event import GameUpdateEvent
    from .player import Player
    from .player_code_reveal_event import PlayerCodeRevealEvent
    from .player_finish_event import PlayerFinishEvent
    from .player_game_result import PlayerGameResult
    from .player_join_event import PlayerJoinEvent
    from .player_leave_event import PlayerLeaveEvent
    from .player_round_result import PlayerRoundResult
    from .player_round_result_score import PlayerRoundResultScore
    from .player_submit_event import PlayerSubmitEvent
    from .players import Players
    from .round import Round
    from .round_start_event import RoundStartEvent
    from .submission import Submission
    from .sync_event import SyncEvent
    from .test_result_event import TestResultEvent
    from .test_result_event_result import TestResultEventResult
_dynamic_imports: typing.Dict[str, str] = {
    "EliminatedEvent": ".eliminated_event",
    "Game": ".game",
    "GameMode": ".game_mode",
    "GameOverEvent": ".game_over_event",
    "GameSettings": ".game_settings",
    "GameState": ".game_state",
    "GameUpdateEvent": ".game_update_event",
    "Player": ".player",
    "PlayerCodeRevealEvent": ".player_code_reveal_event",
    "PlayerFinishEvent": ".player_finish_event",
    "PlayerGameResult": ".player_game_result",
    "PlayerJoinEvent": ".player_join_event",
    "PlayerLeaveEvent": ".player_leave_event",
    "PlayerRoundResult": ".player_round_result",
    "PlayerRoundResultScore": ".player_round_result_score",
    "PlayerSubmitEvent": ".player_submit_event",
    "Players": ".players",
    "Round": ".round",
    "RoundStartEvent": ".round_start_event",
    "Submission": ".submission",
    "SyncEvent": ".sync_event",
    "TestResultEvent": ".test_result_event",
    "TestResultEventResult": ".test_result_event_result",
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
    "EliminatedEvent",
    "Game",
    "GameMode",
    "GameOverEvent",
    "GameSettings",
    "GameState",
    "GameUpdateEvent",
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
    "SyncEvent",
    "TestResultEvent",
    "TestResultEventResult",
]
