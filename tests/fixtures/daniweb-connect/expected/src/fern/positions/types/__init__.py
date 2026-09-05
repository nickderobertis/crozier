



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .patch_positions_id_request_category import PatchPositionsIdRequestCategory
    from .patch_positions_id_request_organization_size import PatchPositionsIdRequestOrganizationSize
    from .patch_positions_id_request_position import PatchPositionsIdRequestPosition
    from .post_positions_request_category import PostPositionsRequestCategory
    from .post_positions_request_organization_size import PostPositionsRequestOrganizationSize
    from .post_positions_request_position import PostPositionsRequestPosition
_dynamic_imports: typing.Dict[str, str] = {
    "PatchPositionsIdRequestCategory": ".patch_positions_id_request_category",
    "PatchPositionsIdRequestOrganizationSize": ".patch_positions_id_request_organization_size",
    "PatchPositionsIdRequestPosition": ".patch_positions_id_request_position",
    "PostPositionsRequestCategory": ".post_positions_request_category",
    "PostPositionsRequestOrganizationSize": ".post_positions_request_organization_size",
    "PostPositionsRequestPosition": ".post_positions_request_position",
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
    "PatchPositionsIdRequestCategory",
    "PatchPositionsIdRequestOrganizationSize",
    "PatchPositionsIdRequestPosition",
    "PostPositionsRequestCategory",
    "PostPositionsRequestOrganizationSize",
    "PostPositionsRequestPosition",
]
