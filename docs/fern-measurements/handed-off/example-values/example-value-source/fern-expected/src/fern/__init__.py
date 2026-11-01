



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import BuoyMarker, LightMarker, RosterEntry
    from .errors import NotFoundError
    from . import charts, drills, harbours, ledger, markers, mirrors, passes, rosters, routes, soundings, stations
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .charts import UploadChartResponse
    from .client import AsyncFernApi, FernApi
    from .drills import StartDrillRequestSettingsValue, StartDrillResponse
    from .harbours import GetBerthResponse
    from .ledger import GetBlockResponse
    from .markers import PlaceMarkerRequestMarker, PlaceMarkerResponse
    from .mirrors import AddMirrorResponse
    from .passes import IssuePassRequestGrant, IssuePassResponse
    from .routes import PlanRoutesResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AddMirrorResponse": ".mirrors",
    "AsyncFernApi": ".client",
    "BuoyMarker": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "GetBerthResponse": ".harbours",
    "GetBlockResponse": ".ledger",
    "IssuePassRequestGrant": ".passes",
    "IssuePassResponse": ".passes",
    "LightMarker": ".types",
    "NotFoundError": ".errors",
    "PlaceMarkerRequestMarker": ".markers",
    "PlaceMarkerResponse": ".markers",
    "PlanRoutesResponse": ".routes",
    "RosterEntry": ".types",
    "StartDrillRequestSettingsValue": ".drills",
    "StartDrillResponse": ".drills",
    "UploadChartResponse": ".charts",
    "__version__": ".version",
    "charts": ".charts",
    "drills": ".drills",
    "harbours": ".harbours",
    "ledger": ".ledger",
    "markers": ".markers",
    "mirrors": ".mirrors",
    "passes": ".passes",
    "rosters": ".rosters",
    "routes": ".routes",
    "soundings": ".soundings",
    "stations": ".stations",
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
    "AddMirrorResponse",
    "AsyncFernApi",
    "BuoyMarker",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "GetBerthResponse",
    "GetBlockResponse",
    "IssuePassRequestGrant",
    "IssuePassResponse",
    "LightMarker",
    "NotFoundError",
    "PlaceMarkerRequestMarker",
    "PlaceMarkerResponse",
    "PlanRoutesResponse",
    "RosterEntry",
    "StartDrillRequestSettingsValue",
    "StartDrillResponse",
    "UploadChartResponse",
    "__version__",
    "charts",
    "drills",
    "harbours",
    "ledger",
    "markers",
    "mirrors",
    "passes",
    "rosters",
    "routes",
    "soundings",
    "stations",
]
