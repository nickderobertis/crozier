



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_address_request_data import CreateAddressRequestData
    from .create_address_request_data_attributes import CreateAddressRequestDataAttributes
    from .create_address_request_data_relationships import CreateAddressRequestDataRelationships
    from .create_address_request_data_relationships_country import CreateAddressRequestDataRelationshipsCountry
    from .create_address_request_data_relationships_country_data import CreateAddressRequestDataRelationshipsCountryData
    from .create_address_request_data_relationships_customer import CreateAddressRequestDataRelationshipsCustomer
    from .create_address_request_data_relationships_customer_data import (
        CreateAddressRequestDataRelationshipsCustomerData,
    )
    from .update_address_request_data import UpdateAddressRequestData
    from .update_address_request_data_attributes import UpdateAddressRequestDataAttributes
    from .update_address_request_data_relationships import UpdateAddressRequestDataRelationships
    from .update_address_request_data_relationships_country import UpdateAddressRequestDataRelationshipsCountry
    from .update_address_request_data_relationships_country_data import UpdateAddressRequestDataRelationshipsCountryData
    from .update_address_request_data_relationships_customer import UpdateAddressRequestDataRelationshipsCustomer
    from .update_address_request_data_relationships_customer_data import (
        UpdateAddressRequestDataRelationshipsCustomerData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAddressRequestData": ".create_address_request_data",
    "CreateAddressRequestDataAttributes": ".create_address_request_data_attributes",
    "CreateAddressRequestDataRelationships": ".create_address_request_data_relationships",
    "CreateAddressRequestDataRelationshipsCountry": ".create_address_request_data_relationships_country",
    "CreateAddressRequestDataRelationshipsCountryData": ".create_address_request_data_relationships_country_data",
    "CreateAddressRequestDataRelationshipsCustomer": ".create_address_request_data_relationships_customer",
    "CreateAddressRequestDataRelationshipsCustomerData": ".create_address_request_data_relationships_customer_data",
    "UpdateAddressRequestData": ".update_address_request_data",
    "UpdateAddressRequestDataAttributes": ".update_address_request_data_attributes",
    "UpdateAddressRequestDataRelationships": ".update_address_request_data_relationships",
    "UpdateAddressRequestDataRelationshipsCountry": ".update_address_request_data_relationships_country",
    "UpdateAddressRequestDataRelationshipsCountryData": ".update_address_request_data_relationships_country_data",
    "UpdateAddressRequestDataRelationshipsCustomer": ".update_address_request_data_relationships_customer",
    "UpdateAddressRequestDataRelationshipsCustomerData": ".update_address_request_data_relationships_customer_data",
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
    "CreateAddressRequestData",
    "CreateAddressRequestDataAttributes",
    "CreateAddressRequestDataRelationships",
    "CreateAddressRequestDataRelationshipsCountry",
    "CreateAddressRequestDataRelationshipsCountryData",
    "CreateAddressRequestDataRelationshipsCustomer",
    "CreateAddressRequestDataRelationshipsCustomerData",
    "UpdateAddressRequestData",
    "UpdateAddressRequestDataAttributes",
    "UpdateAddressRequestDataRelationships",
    "UpdateAddressRequestDataRelationshipsCountry",
    "UpdateAddressRequestDataRelationshipsCountryData",
    "UpdateAddressRequestDataRelationshipsCustomer",
    "UpdateAddressRequestDataRelationshipsCustomerData",
]
