



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .closed_accepted_choice import ClosedAcceptedChoice
    from .closed_accepted_choice_window import ClosedAcceptedChoiceWindow
    from .closed_accepted_choice_window_window import ClosedAcceptedChoiceWindowWindow
    from .closed_accepted_choice_window_window_lookback import ClosedAcceptedChoiceWindowWindowLookback
    from .closed_accepted_plan import ClosedAcceptedPlan
    from .closed_rejected_choice import ClosedRejectedChoice
    from .closed_rejected_choice_window import ClosedRejectedChoiceWindow
    from .closed_rejected_choice_window_window import ClosedRejectedChoiceWindowWindow
    from .closed_rejected_choice_window_window_lookback import ClosedRejectedChoiceWindowWindowLookback
    from .closed_rejected_plan import ClosedRejectedPlan
    from .map_accepted_choice import MapAcceptedChoice
    from .map_accepted_choice_window import MapAcceptedChoiceWindow
    from .map_accepted_choice_window_window import MapAcceptedChoiceWindowWindow
    from .map_accepted_plan import MapAcceptedPlan
    from .map_rejected_choice import MapRejectedChoice
    from .map_rejected_choice_window import MapRejectedChoiceWindow
    from .map_rejected_choice_window_window import MapRejectedChoiceWindowWindow
    from .map_rejected_plan import MapRejectedPlan
    from .null_allowed_choice import NullAllowedChoice
    from .null_allowed_choice_window import NullAllowedChoiceWindow
    from .null_allowed_choice_window_window import NullAllowedChoiceWindowWindow
    from .null_allowed_plan import NullAllowedPlan
    from .null_disallowed_choice import NullDisallowedChoice
    from .null_disallowed_choice_window import NullDisallowedChoiceWindow
    from .null_disallowed_choice_window_window import NullDisallowedChoiceWindowWindow
    from .null_disallowed_plan import NullDisallowedPlan
_dynamic_imports: typing.Dict[str, str] = {
    "ClosedAcceptedChoice": ".closed_accepted_choice",
    "ClosedAcceptedChoiceWindow": ".closed_accepted_choice_window",
    "ClosedAcceptedChoiceWindowWindow": ".closed_accepted_choice_window_window",
    "ClosedAcceptedChoiceWindowWindowLookback": ".closed_accepted_choice_window_window_lookback",
    "ClosedAcceptedPlan": ".closed_accepted_plan",
    "ClosedRejectedChoice": ".closed_rejected_choice",
    "ClosedRejectedChoiceWindow": ".closed_rejected_choice_window",
    "ClosedRejectedChoiceWindowWindow": ".closed_rejected_choice_window_window",
    "ClosedRejectedChoiceWindowWindowLookback": ".closed_rejected_choice_window_window_lookback",
    "ClosedRejectedPlan": ".closed_rejected_plan",
    "MapAcceptedChoice": ".map_accepted_choice",
    "MapAcceptedChoiceWindow": ".map_accepted_choice_window",
    "MapAcceptedChoiceWindowWindow": ".map_accepted_choice_window_window",
    "MapAcceptedPlan": ".map_accepted_plan",
    "MapRejectedChoice": ".map_rejected_choice",
    "MapRejectedChoiceWindow": ".map_rejected_choice_window",
    "MapRejectedChoiceWindowWindow": ".map_rejected_choice_window_window",
    "MapRejectedPlan": ".map_rejected_plan",
    "NullAllowedChoice": ".null_allowed_choice",
    "NullAllowedChoiceWindow": ".null_allowed_choice_window",
    "NullAllowedChoiceWindowWindow": ".null_allowed_choice_window_window",
    "NullAllowedPlan": ".null_allowed_plan",
    "NullDisallowedChoice": ".null_disallowed_choice",
    "NullDisallowedChoiceWindow": ".null_disallowed_choice_window",
    "NullDisallowedChoiceWindowWindow": ".null_disallowed_choice_window_window",
    "NullDisallowedPlan": ".null_disallowed_plan",
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
    "ClosedAcceptedChoice",
    "ClosedAcceptedChoiceWindow",
    "ClosedAcceptedChoiceWindowWindow",
    "ClosedAcceptedChoiceWindowWindowLookback",
    "ClosedAcceptedPlan",
    "ClosedRejectedChoice",
    "ClosedRejectedChoiceWindow",
    "ClosedRejectedChoiceWindowWindow",
    "ClosedRejectedChoiceWindowWindowLookback",
    "ClosedRejectedPlan",
    "MapAcceptedChoice",
    "MapAcceptedChoiceWindow",
    "MapAcceptedChoiceWindowWindow",
    "MapAcceptedPlan",
    "MapRejectedChoice",
    "MapRejectedChoiceWindow",
    "MapRejectedChoiceWindowWindow",
    "MapRejectedPlan",
    "NullAllowedChoice",
    "NullAllowedChoiceWindow",
    "NullAllowedChoiceWindowWindow",
    "NullAllowedPlan",
    "NullDisallowedChoice",
    "NullDisallowedChoiceWindow",
    "NullDisallowedChoiceWindowWindow",
    "NullDisallowedPlan",
]
