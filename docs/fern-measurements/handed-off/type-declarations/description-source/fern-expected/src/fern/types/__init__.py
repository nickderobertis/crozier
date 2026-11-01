



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apprentice import Apprentice
    from .digest import Digest
    from .get_firing_response import GetFiringResponse
    from .get_firing_response_outcome import GetFiringResponseOutcome
    from .glassblower import Glassblower
    from .glaze_kind import GlazeKind
    from .maker import Maker
    from .piece import Piece
    from .piece_id import PieceId
    from .piece_links import PieceLinks
_dynamic_imports: typing.Dict[str, str] = {
    "Apprentice": ".apprentice",
    "Digest": ".digest",
    "GetFiringResponse": ".get_firing_response",
    "GetFiringResponseOutcome": ".get_firing_response_outcome",
    "Glassblower": ".glassblower",
    "GlazeKind": ".glaze_kind",
    "Maker": ".maker",
    "Piece": ".piece",
    "PieceId": ".piece_id",
    "PieceLinks": ".piece_links",
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
    "Apprentice",
    "Digest",
    "GetFiringResponse",
    "GetFiringResponseOutcome",
    "Glassblower",
    "GlazeKind",
    "Maker",
    "Piece",
    "PieceId",
    "PieceLinks",
]
