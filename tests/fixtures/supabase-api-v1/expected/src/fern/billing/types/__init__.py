



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apply_project_addon_body_addon_type import ApplyProjectAddonBodyAddonType
    from .apply_project_addon_body_addon_variant import ApplyProjectAddonBodyAddonVariant
    from .apply_project_addon_body_addon_variant_one import ApplyProjectAddonBodyAddonVariantOne
    from .apply_project_addon_body_addon_variant_three import ApplyProjectAddonBodyAddonVariantThree
    from .apply_project_addon_body_addon_variant_two import ApplyProjectAddonBodyAddonVariantTwo
    from .apply_project_addon_body_addon_variant_zero import ApplyProjectAddonBodyAddonVariantZero
    from .v1remove_project_addon_request_addon_variant import V1RemoveProjectAddonRequestAddonVariant
    from .v1remove_project_addon_request_addon_variant_one import V1RemoveProjectAddonRequestAddonVariantOne
    from .v1remove_project_addon_request_addon_variant_three import V1RemoveProjectAddonRequestAddonVariantThree
    from .v1remove_project_addon_request_addon_variant_two import V1RemoveProjectAddonRequestAddonVariantTwo
    from .v1remove_project_addon_request_addon_variant_zero import V1RemoveProjectAddonRequestAddonVariantZero
_dynamic_imports: typing.Dict[str, str] = {
    "ApplyProjectAddonBodyAddonType": ".apply_project_addon_body_addon_type",
    "ApplyProjectAddonBodyAddonVariant": ".apply_project_addon_body_addon_variant",
    "ApplyProjectAddonBodyAddonVariantOne": ".apply_project_addon_body_addon_variant_one",
    "ApplyProjectAddonBodyAddonVariantThree": ".apply_project_addon_body_addon_variant_three",
    "ApplyProjectAddonBodyAddonVariantTwo": ".apply_project_addon_body_addon_variant_two",
    "ApplyProjectAddonBodyAddonVariantZero": ".apply_project_addon_body_addon_variant_zero",
    "V1RemoveProjectAddonRequestAddonVariant": ".v1remove_project_addon_request_addon_variant",
    "V1RemoveProjectAddonRequestAddonVariantOne": ".v1remove_project_addon_request_addon_variant_one",
    "V1RemoveProjectAddonRequestAddonVariantThree": ".v1remove_project_addon_request_addon_variant_three",
    "V1RemoveProjectAddonRequestAddonVariantTwo": ".v1remove_project_addon_request_addon_variant_two",
    "V1RemoveProjectAddonRequestAddonVariantZero": ".v1remove_project_addon_request_addon_variant_zero",
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
    "ApplyProjectAddonBodyAddonType",
    "ApplyProjectAddonBodyAddonVariant",
    "ApplyProjectAddonBodyAddonVariantOne",
    "ApplyProjectAddonBodyAddonVariantThree",
    "ApplyProjectAddonBodyAddonVariantTwo",
    "ApplyProjectAddonBodyAddonVariantZero",
    "V1RemoveProjectAddonRequestAddonVariant",
    "V1RemoveProjectAddonRequestAddonVariantOne",
    "V1RemoveProjectAddonRequestAddonVariantThree",
    "V1RemoveProjectAddonRequestAddonVariantTwo",
    "V1RemoveProjectAddonRequestAddonVariantZero",
]
