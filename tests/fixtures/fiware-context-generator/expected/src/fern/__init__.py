



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Building,
        BuildingCategoryItem,
        BuildingSeeAlso,
        BuildingType,
        Location,
        LocationLineString,
        LocationMultiLineString,
        LocationMultiPoint,
        LocationMultiPolygon,
        LocationPoint,
        LocationPolygon,
        Location_LineString,
        Location_MultiLineString,
        Location_MultiPoint,
        Location_MultiPolygon,
        Location_Point,
        Location_Polygon,
        Organization,
        OrganizationAggregateRating,
        OrganizationSeeAlso,
        OrganizationType,
        PostalAddress,
    )
    from . import ngsi_ld
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .ngsi_ld import GetNgsiLdV1EntitiesRequestType
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Building": ".types",
    "BuildingCategoryItem": ".types",
    "BuildingSeeAlso": ".types",
    "BuildingType": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "GetNgsiLdV1EntitiesRequestType": ".ngsi_ld",
    "Location": ".types",
    "LocationLineString": ".types",
    "LocationMultiLineString": ".types",
    "LocationMultiPoint": ".types",
    "LocationMultiPolygon": ".types",
    "LocationPoint": ".types",
    "LocationPolygon": ".types",
    "Location_LineString": ".types",
    "Location_MultiLineString": ".types",
    "Location_MultiPoint": ".types",
    "Location_MultiPolygon": ".types",
    "Location_Point": ".types",
    "Location_Polygon": ".types",
    "Organization": ".types",
    "OrganizationAggregateRating": ".types",
    "OrganizationSeeAlso": ".types",
    "OrganizationType": ".types",
    "PostalAddress": ".types",
    "__version__": ".version",
    "ngsi_ld": ".ngsi_ld",
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
    "Building",
    "BuildingCategoryItem",
    "BuildingSeeAlso",
    "BuildingType",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "GetNgsiLdV1EntitiesRequestType",
    "Location",
    "LocationLineString",
    "LocationMultiLineString",
    "LocationMultiPoint",
    "LocationMultiPolygon",
    "LocationPoint",
    "LocationPolygon",
    "Location_LineString",
    "Location_MultiLineString",
    "Location_MultiPoint",
    "Location_MultiPolygon",
    "Location_Point",
    "Location_Polygon",
    "Organization",
    "OrganizationAggregateRating",
    "OrganizationSeeAlso",
    "OrganizationType",
    "PostalAddress",
    "__version__",
    "ngsi_ld",
]
