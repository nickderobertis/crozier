



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accepted_response import AcceptedResponse
    from .ballot import Ballot
    from .ballot_tallies_item import BallotTalliesItem
    from .base_response import BaseResponse
    from .portal import Portal
    from .portal_settings import PortalSettings
    from .portal_tallies_item import PortalTalliesItem
    from .scan_response import ScanResponse
    from .seamless_link import SeamlessLink
    from .vote_list import VoteList
    from .vote_list_item import VoteListItem
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptedResponse": ".accepted_response",
    "Ballot": ".ballot",
    "BallotTalliesItem": ".ballot_tallies_item",
    "BaseResponse": ".base_response",
    "Portal": ".portal",
    "PortalSettings": ".portal_settings",
    "PortalTalliesItem": ".portal_tallies_item",
    "ScanResponse": ".scan_response",
    "SeamlessLink": ".seamless_link",
    "VoteList": ".vote_list",
    "VoteListItem": ".vote_list_item",
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
    "AcceptedResponse",
    "Ballot",
    "BallotTalliesItem",
    "BaseResponse",
    "Portal",
    "PortalSettings",
    "PortalTalliesItem",
    "ScanResponse",
    "SeamlessLink",
    "VoteList",
    "VoteListItem",
]
