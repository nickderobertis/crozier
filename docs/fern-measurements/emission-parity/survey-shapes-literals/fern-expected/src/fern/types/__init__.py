



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .deep import Deep
    from .flat import Flat
    from .marker import Marker
    from .marker_at import MarkerAt
    from .marker_kind import MarkerKind
    from .note import Note
    from .quadrats import Quadrats
    from .quadrats_cells_item_item_item import QuadratsCellsItemItemItem
    from .quadrats_kind import QuadratsKind
    from .site import Site
    from .site_batch import SiteBatch
    from .site_outline import SiteOutline, SiteOutline_Marker, SiteOutline_Quadrats, SiteOutline_Transect
    from .site_patch import SitePatch
    from .site_patch_kind import SitePatchKind
    from .site_type import SiteType
    from .transect import Transect
    from .transect_kind import TransectKind
    from .transect_legs_item_item import TransectLegsItemItem
_dynamic_imports: typing.Dict[str, str] = {
    "Deep": ".deep",
    "Flat": ".flat",
    "Marker": ".marker",
    "MarkerAt": ".marker_at",
    "MarkerKind": ".marker_kind",
    "Note": ".note",
    "Quadrats": ".quadrats",
    "QuadratsCellsItemItemItem": ".quadrats_cells_item_item_item",
    "QuadratsKind": ".quadrats_kind",
    "Site": ".site",
    "SiteBatch": ".site_batch",
    "SiteOutline": ".site_outline",
    "SiteOutline_Marker": ".site_outline",
    "SiteOutline_Quadrats": ".site_outline",
    "SiteOutline_Transect": ".site_outline",
    "SitePatch": ".site_patch",
    "SitePatchKind": ".site_patch_kind",
    "SiteType": ".site_type",
    "Transect": ".transect",
    "TransectKind": ".transect_kind",
    "TransectLegsItemItem": ".transect_legs_item_item",
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
    "Deep",
    "Flat",
    "Marker",
    "MarkerAt",
    "MarkerKind",
    "Note",
    "Quadrats",
    "QuadratsCellsItemItemItem",
    "QuadratsKind",
    "Site",
    "SiteBatch",
    "SiteOutline",
    "SiteOutline_Marker",
    "SiteOutline_Quadrats",
    "SiteOutline_Transect",
    "SitePatch",
    "SitePatchKind",
    "SiteType",
    "Transect",
    "TransectKind",
    "TransectLegsItemItem",
]
