



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AttachShippingOptionActionRequestData,
        AttachShippingOptionActionRequestDataAttributes,
        ContinuousUpdateActionRequestData,
        ContinuousUpdateActionRequestDataAttributes,
        ContinuousUpdateActionRequestDataRelationships,
        ContinuousUpdateActionRequestDataRelationshipsCart,
        ContinuousUpdateActionRequestDataRelationshipsCartData,
        CreateCartAddressRequestData,
        CreateCartAddressRequestDataAttributes,
        CreateCartAddressRequestDataRelationships,
        CreateCartAddressRequestDataRelationshipsCart,
        CreateCartAddressRequestDataRelationshipsCartData,
        CreateCartAddressRequestDataRelationshipsCountry,
        CreateCartAddressRequestDataRelationshipsCountryData,
        DetachShippingOptionActionRequestData,
        DetachShippingOptionActionRequestDataAttributes,
        UpdateCartAddressCountryActionRequestData,
        UpdateCartAddressCountryActionRequestDataRelationships,
        UpdateCartAddressCountryActionRequestDataRelationshipsCountry,
        UpdateCartAddressCountryActionRequestDataRelationshipsCountryData,
        UpdateCartAddressRequestData,
        UpdateCartAddressRequestDataAttributes,
        UpdateCartAddressRequestDataRelationships,
        UpdateCartAddressRequestDataRelationshipsCart,
        UpdateCartAddressRequestDataRelationshipsCartData,
        UpdateCartAddressRequestDataRelationshipsCountry,
        UpdateCartAddressRequestDataRelationshipsCountryData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AttachShippingOptionActionRequestData": ".types",
    "AttachShippingOptionActionRequestDataAttributes": ".types",
    "ContinuousUpdateActionRequestData": ".types",
    "ContinuousUpdateActionRequestDataAttributes": ".types",
    "ContinuousUpdateActionRequestDataRelationships": ".types",
    "ContinuousUpdateActionRequestDataRelationshipsCart": ".types",
    "ContinuousUpdateActionRequestDataRelationshipsCartData": ".types",
    "CreateCartAddressRequestData": ".types",
    "CreateCartAddressRequestDataAttributes": ".types",
    "CreateCartAddressRequestDataRelationships": ".types",
    "CreateCartAddressRequestDataRelationshipsCart": ".types",
    "CreateCartAddressRequestDataRelationshipsCartData": ".types",
    "CreateCartAddressRequestDataRelationshipsCountry": ".types",
    "CreateCartAddressRequestDataRelationshipsCountryData": ".types",
    "DetachShippingOptionActionRequestData": ".types",
    "DetachShippingOptionActionRequestDataAttributes": ".types",
    "UpdateCartAddressCountryActionRequestData": ".types",
    "UpdateCartAddressCountryActionRequestDataRelationships": ".types",
    "UpdateCartAddressCountryActionRequestDataRelationshipsCountry": ".types",
    "UpdateCartAddressCountryActionRequestDataRelationshipsCountryData": ".types",
    "UpdateCartAddressRequestData": ".types",
    "UpdateCartAddressRequestDataAttributes": ".types",
    "UpdateCartAddressRequestDataRelationships": ".types",
    "UpdateCartAddressRequestDataRelationshipsCart": ".types",
    "UpdateCartAddressRequestDataRelationshipsCartData": ".types",
    "UpdateCartAddressRequestDataRelationshipsCountry": ".types",
    "UpdateCartAddressRequestDataRelationshipsCountryData": ".types",
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
    "AttachShippingOptionActionRequestData",
    "AttachShippingOptionActionRequestDataAttributes",
    "ContinuousUpdateActionRequestData",
    "ContinuousUpdateActionRequestDataAttributes",
    "ContinuousUpdateActionRequestDataRelationships",
    "ContinuousUpdateActionRequestDataRelationshipsCart",
    "ContinuousUpdateActionRequestDataRelationshipsCartData",
    "CreateCartAddressRequestData",
    "CreateCartAddressRequestDataAttributes",
    "CreateCartAddressRequestDataRelationships",
    "CreateCartAddressRequestDataRelationshipsCart",
    "CreateCartAddressRequestDataRelationshipsCartData",
    "CreateCartAddressRequestDataRelationshipsCountry",
    "CreateCartAddressRequestDataRelationshipsCountryData",
    "DetachShippingOptionActionRequestData",
    "DetachShippingOptionActionRequestDataAttributes",
    "UpdateCartAddressCountryActionRequestData",
    "UpdateCartAddressCountryActionRequestDataRelationships",
    "UpdateCartAddressCountryActionRequestDataRelationshipsCountry",
    "UpdateCartAddressCountryActionRequestDataRelationshipsCountryData",
    "UpdateCartAddressRequestData",
    "UpdateCartAddressRequestDataAttributes",
    "UpdateCartAddressRequestDataRelationships",
    "UpdateCartAddressRequestDataRelationshipsCart",
    "UpdateCartAddressRequestDataRelationshipsCartData",
    "UpdateCartAddressRequestDataRelationshipsCountry",
    "UpdateCartAddressRequestDataRelationshipsCountryData",
]
