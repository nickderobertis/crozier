



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Deep,
        Flat,
        Marker,
        MarkerAt,
        MarkerKind,
        Note,
        Quadrats,
        QuadratsCellsItemItemItem,
        QuadratsKind,
        Site,
        SiteBatch,
        SiteOutline,
        SiteOutline_Marker,
        SiteOutline_Quadrats,
        SiteOutline_Transect,
        SitePatch,
        SitePatchKind,
        SiteType,
        Transect,
        TransectKind,
        TransectLegsItemItem,
    )
    from . import sites, survey
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .sites import SiteSearchWithin
    from .survey import (
        AmendSiteRequestBody,
        AmendSiteRequestBodyKind,
        RecordSitesRequest,
        RecordSitesRequest_Site,
        RecordSitesRequest_SiteBatch,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AmendSiteRequestBody": ".survey",
    "AmendSiteRequestBodyKind": ".survey",
    "AsyncFernApi": ".client",
    "Deep": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "Flat": ".types",
    "Marker": ".types",
    "MarkerAt": ".types",
    "MarkerKind": ".types",
    "Note": ".types",
    "Quadrats": ".types",
    "QuadratsCellsItemItemItem": ".types",
    "QuadratsKind": ".types",
    "RecordSitesRequest": ".survey",
    "RecordSitesRequest_Site": ".survey",
    "RecordSitesRequest_SiteBatch": ".survey",
    "Site": ".types",
    "SiteBatch": ".types",
    "SiteOutline": ".types",
    "SiteOutline_Marker": ".types",
    "SiteOutline_Quadrats": ".types",
    "SiteOutline_Transect": ".types",
    "SitePatch": ".types",
    "SitePatchKind": ".types",
    "SiteSearchWithin": ".sites",
    "SiteType": ".types",
    "Transect": ".types",
    "TransectKind": ".types",
    "TransectLegsItemItem": ".types",
    "__version__": ".version",
    "sites": ".sites",
    "survey": ".survey",
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
    "AmendSiteRequestBody",
    "AmendSiteRequestBodyKind",
    "AsyncFernApi",
    "Deep",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "Flat",
    "Marker",
    "MarkerAt",
    "MarkerKind",
    "Note",
    "Quadrats",
    "QuadratsCellsItemItemItem",
    "QuadratsKind",
    "RecordSitesRequest",
    "RecordSitesRequest_Site",
    "RecordSitesRequest_SiteBatch",
    "Site",
    "SiteBatch",
    "SiteOutline",
    "SiteOutline_Marker",
    "SiteOutline_Quadrats",
    "SiteOutline_Transect",
    "SitePatch",
    "SitePatchKind",
    "SiteSearchWithin",
    "SiteType",
    "Transect",
    "TransectKind",
    "TransectLegsItemItem",
    "__version__",
    "sites",
    "survey",
]
