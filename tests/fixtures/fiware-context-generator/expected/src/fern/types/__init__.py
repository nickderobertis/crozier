



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .building import Building
    from .building_category_item import BuildingCategoryItem
    from .building_see_also import BuildingSeeAlso
    from .building_type import BuildingType
    from .location import (
        Location,
        Location_LineString,
        Location_MultiLineString,
        Location_MultiPoint,
        Location_MultiPolygon,
        Location_Point,
        Location_Polygon,
    )
    from .location_line_string import LocationLineString
    from .location_multi_line_string import LocationMultiLineString
    from .location_multi_point import LocationMultiPoint
    from .location_multi_polygon import LocationMultiPolygon
    from .location_point import LocationPoint
    from .location_polygon import LocationPolygon
    from .organization import Organization
    from .organization_aggregate_rating import OrganizationAggregateRating
    from .organization_see_also import OrganizationSeeAlso
    from .organization_type import OrganizationType
    from .postal_address import PostalAddress
_dynamic_imports: typing.Dict[str, str] = {
    "Building": ".building",
    "BuildingCategoryItem": ".building_category_item",
    "BuildingSeeAlso": ".building_see_also",
    "BuildingType": ".building_type",
    "Location": ".location",
    "LocationLineString": ".location_line_string",
    "LocationMultiLineString": ".location_multi_line_string",
    "LocationMultiPoint": ".location_multi_point",
    "LocationMultiPolygon": ".location_multi_polygon",
    "LocationPoint": ".location_point",
    "LocationPolygon": ".location_polygon",
    "Location_LineString": ".location",
    "Location_MultiLineString": ".location",
    "Location_MultiPoint": ".location",
    "Location_MultiPolygon": ".location",
    "Location_Point": ".location",
    "Location_Polygon": ".location",
    "Organization": ".organization",
    "OrganizationAggregateRating": ".organization_aggregate_rating",
    "OrganizationSeeAlso": ".organization_see_also",
    "OrganizationType": ".organization_type",
    "PostalAddress": ".postal_address",
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
    "Building",
    "BuildingCategoryItem",
    "BuildingSeeAlso",
    "BuildingType",
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
]
