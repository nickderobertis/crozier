



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import BuoyMarker, LightMarker, RosterEntry, StoreLine, WatchRota, WatchRotaCadence
    from .errors import NotFoundError
    from . import (
        beacons,
        charts,
        drills,
        galleys,
        harbours,
        ledger,
        manifests,
        markers,
        mirrors,
        passes,
        rosters,
        routes,
        soundings,
        stations,
        voyages,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .charts import (
        SetChartLayersRequestLayersItem,
        SetChartLayersRequestLayersItemMatch,
        SetChartLayersResponse,
        UploadChartResponse,
    )
    from .client import AsyncFernApi, FernApi
    from .drills import StartDrillRequestSettingsValue, StartDrillResponse
    from .harbours import GetBerthResponse
    from .ledger import GetBlockResponse
    from .manifests import ImportManifestRequestTask, ImportManifestResponse
    from .markers import PlaceMarkerRequestMarker, PlaceMarkerResponse
    from .mirrors import AddMirrorResponse
    from .passes import (
        IssueFormPassRequestGrant,
        IssueFormPassRequestTier,
        IssueFormPassResponse,
        IssuePassRequestGrant,
        IssuePassResponse,
    )
    from .routes import PlanRoutesResponse
    from .version import __version__
    from .voyages import PlanVoyageRotaResponse, SetVoyageWatchResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AddMirrorResponse": ".mirrors",
    "AsyncFernApi": ".client",
    "BuoyMarker": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "GetBerthResponse": ".harbours",
    "GetBlockResponse": ".ledger",
    "ImportManifestRequestTask": ".manifests",
    "ImportManifestResponse": ".manifests",
    "IssueFormPassRequestGrant": ".passes",
    "IssueFormPassRequestTier": ".passes",
    "IssueFormPassResponse": ".passes",
    "IssuePassRequestGrant": ".passes",
    "IssuePassResponse": ".passes",
    "LightMarker": ".types",
    "NotFoundError": ".errors",
    "PlaceMarkerRequestMarker": ".markers",
    "PlaceMarkerResponse": ".markers",
    "PlanRoutesResponse": ".routes",
    "PlanVoyageRotaResponse": ".voyages",
    "RosterEntry": ".types",
    "SetChartLayersRequestLayersItem": ".charts",
    "SetChartLayersRequestLayersItemMatch": ".charts",
    "SetChartLayersResponse": ".charts",
    "SetVoyageWatchResponse": ".voyages",
    "StartDrillRequestSettingsValue": ".drills",
    "StartDrillResponse": ".drills",
    "StoreLine": ".types",
    "UploadChartResponse": ".charts",
    "WatchRota": ".types",
    "WatchRotaCadence": ".types",
    "__version__": ".version",
    "beacons": ".beacons",
    "charts": ".charts",
    "drills": ".drills",
    "galleys": ".galleys",
    "harbours": ".harbours",
    "ledger": ".ledger",
    "manifests": ".manifests",
    "markers": ".markers",
    "mirrors": ".mirrors",
    "passes": ".passes",
    "rosters": ".rosters",
    "routes": ".routes",
    "soundings": ".soundings",
    "stations": ".stations",
    "voyages": ".voyages",
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
    "ImportManifestRequestTask",
    "ImportManifestResponse",
    "IssueFormPassRequestGrant",
    "IssueFormPassRequestTier",
    "IssueFormPassResponse",
    "IssuePassRequestGrant",
    "IssuePassResponse",
    "LightMarker",
    "NotFoundError",
    "PlaceMarkerRequestMarker",
    "PlaceMarkerResponse",
    "PlanRoutesResponse",
    "PlanVoyageRotaResponse",
    "RosterEntry",
    "SetChartLayersRequestLayersItem",
    "SetChartLayersRequestLayersItemMatch",
    "SetChartLayersResponse",
    "SetVoyageWatchResponse",
    "StartDrillRequestSettingsValue",
    "StartDrillResponse",
    "StoreLine",
    "UploadChartResponse",
    "WatchRota",
    "WatchRotaCadence",
    "__version__",
    "beacons",
    "charts",
    "drills",
    "galleys",
    "harbours",
    "ledger",
    "manifests",
    "markers",
    "mirrors",
    "passes",
    "rosters",
    "routes",
    "soundings",
    "stations",
    "voyages",
]
