



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .crossing_boarding_notice import CrossingBoardingNotice
    from .crossing_boarding_notice_phase import CrossingBoardingNoticePhase
    from .crossing_delayed_notice import CrossingDelayedNotice
    from .crossing_delayed_notice_phase import CrossingDelayedNoticePhase
    from .crossing_notice import CrossingNotice
    from .crossing_notice_phase import CrossingNoticePhase
    from .crossing_sailed_notice import CrossingSailedNotice
    from .crossing_sailed_notice_phase import CrossingSailedNoticePhase
    from .get_crossing_response import GetCrossingResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CrossingBoardingNotice": ".crossing_boarding_notice",
    "CrossingBoardingNoticePhase": ".crossing_boarding_notice_phase",
    "CrossingDelayedNotice": ".crossing_delayed_notice",
    "CrossingDelayedNoticePhase": ".crossing_delayed_notice_phase",
    "CrossingNotice": ".crossing_notice",
    "CrossingNoticePhase": ".crossing_notice_phase",
    "CrossingSailedNotice": ".crossing_sailed_notice",
    "CrossingSailedNoticePhase": ".crossing_sailed_notice_phase",
    "GetCrossingResponse": ".get_crossing_response",
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
    "CrossingBoardingNotice",
    "CrossingBoardingNoticePhase",
    "CrossingDelayedNotice",
    "CrossingDelayedNoticePhase",
    "CrossingNotice",
    "CrossingNoticePhase",
    "CrossingSailedNotice",
    "CrossingSailedNoticePhase",
    "GetCrossingResponse",
]
