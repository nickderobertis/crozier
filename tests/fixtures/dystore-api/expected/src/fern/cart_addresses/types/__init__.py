



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .attach_shipping_option_action_request_data import AttachShippingOptionActionRequestData
    from .attach_shipping_option_action_request_data_attributes import AttachShippingOptionActionRequestDataAttributes
    from .continuous_update_action_request_data import ContinuousUpdateActionRequestData
    from .continuous_update_action_request_data_attributes import ContinuousUpdateActionRequestDataAttributes
    from .continuous_update_action_request_data_relationships import ContinuousUpdateActionRequestDataRelationships
    from .continuous_update_action_request_data_relationships_cart import (
        ContinuousUpdateActionRequestDataRelationshipsCart,
    )
    from .continuous_update_action_request_data_relationships_cart_data import (
        ContinuousUpdateActionRequestDataRelationshipsCartData,
    )
    from .create_cart_address_request_data import CreateCartAddressRequestData
    from .create_cart_address_request_data_attributes import CreateCartAddressRequestDataAttributes
    from .create_cart_address_request_data_relationships import CreateCartAddressRequestDataRelationships
    from .create_cart_address_request_data_relationships_cart import CreateCartAddressRequestDataRelationshipsCart
    from .create_cart_address_request_data_relationships_cart_data import (
        CreateCartAddressRequestDataRelationshipsCartData,
    )
    from .create_cart_address_request_data_relationships_country import CreateCartAddressRequestDataRelationshipsCountry
    from .create_cart_address_request_data_relationships_country_data import (
        CreateCartAddressRequestDataRelationshipsCountryData,
    )
    from .detach_shipping_option_action_request_data import DetachShippingOptionActionRequestData
    from .detach_shipping_option_action_request_data_attributes import DetachShippingOptionActionRequestDataAttributes
    from .update_cart_address_country_action_request_data import UpdateCartAddressCountryActionRequestData
    from .update_cart_address_country_action_request_data_relationships import (
        UpdateCartAddressCountryActionRequestDataRelationships,
    )
    from .update_cart_address_country_action_request_data_relationships_country import (
        UpdateCartAddressCountryActionRequestDataRelationshipsCountry,
    )
    from .update_cart_address_country_action_request_data_relationships_country_data import (
        UpdateCartAddressCountryActionRequestDataRelationshipsCountryData,
    )
    from .update_cart_address_request_data import UpdateCartAddressRequestData
    from .update_cart_address_request_data_attributes import UpdateCartAddressRequestDataAttributes
    from .update_cart_address_request_data_relationships import UpdateCartAddressRequestDataRelationships
    from .update_cart_address_request_data_relationships_cart import UpdateCartAddressRequestDataRelationshipsCart
    from .update_cart_address_request_data_relationships_cart_data import (
        UpdateCartAddressRequestDataRelationshipsCartData,
    )
    from .update_cart_address_request_data_relationships_country import UpdateCartAddressRequestDataRelationshipsCountry
    from .update_cart_address_request_data_relationships_country_data import (
        UpdateCartAddressRequestDataRelationshipsCountryData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AttachShippingOptionActionRequestData": ".attach_shipping_option_action_request_data",
    "AttachShippingOptionActionRequestDataAttributes": ".attach_shipping_option_action_request_data_attributes",
    "ContinuousUpdateActionRequestData": ".continuous_update_action_request_data",
    "ContinuousUpdateActionRequestDataAttributes": ".continuous_update_action_request_data_attributes",
    "ContinuousUpdateActionRequestDataRelationships": ".continuous_update_action_request_data_relationships",
    "ContinuousUpdateActionRequestDataRelationshipsCart": ".continuous_update_action_request_data_relationships_cart",
    "ContinuousUpdateActionRequestDataRelationshipsCartData": ".continuous_update_action_request_data_relationships_cart_data",
    "CreateCartAddressRequestData": ".create_cart_address_request_data",
    "CreateCartAddressRequestDataAttributes": ".create_cart_address_request_data_attributes",
    "CreateCartAddressRequestDataRelationships": ".create_cart_address_request_data_relationships",
    "CreateCartAddressRequestDataRelationshipsCart": ".create_cart_address_request_data_relationships_cart",
    "CreateCartAddressRequestDataRelationshipsCartData": ".create_cart_address_request_data_relationships_cart_data",
    "CreateCartAddressRequestDataRelationshipsCountry": ".create_cart_address_request_data_relationships_country",
    "CreateCartAddressRequestDataRelationshipsCountryData": ".create_cart_address_request_data_relationships_country_data",
    "DetachShippingOptionActionRequestData": ".detach_shipping_option_action_request_data",
    "DetachShippingOptionActionRequestDataAttributes": ".detach_shipping_option_action_request_data_attributes",
    "UpdateCartAddressCountryActionRequestData": ".update_cart_address_country_action_request_data",
    "UpdateCartAddressCountryActionRequestDataRelationships": ".update_cart_address_country_action_request_data_relationships",
    "UpdateCartAddressCountryActionRequestDataRelationshipsCountry": ".update_cart_address_country_action_request_data_relationships_country",
    "UpdateCartAddressCountryActionRequestDataRelationshipsCountryData": ".update_cart_address_country_action_request_data_relationships_country_data",
    "UpdateCartAddressRequestData": ".update_cart_address_request_data",
    "UpdateCartAddressRequestDataAttributes": ".update_cart_address_request_data_attributes",
    "UpdateCartAddressRequestDataRelationships": ".update_cart_address_request_data_relationships",
    "UpdateCartAddressRequestDataRelationshipsCart": ".update_cart_address_request_data_relationships_cart",
    "UpdateCartAddressRequestDataRelationshipsCartData": ".update_cart_address_request_data_relationships_cart_data",
    "UpdateCartAddressRequestDataRelationshipsCountry": ".update_cart_address_request_data_relationships_country",
    "UpdateCartAddressRequestDataRelationshipsCountryData": ".update_cart_address_request_data_relationships_country_data",
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
