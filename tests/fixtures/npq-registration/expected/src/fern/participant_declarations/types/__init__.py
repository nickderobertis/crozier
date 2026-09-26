



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .participant_declaration_change_delivery_partner_request_data import (
        ParticipantDeclarationChangeDeliveryPartnerRequestData,
    )
    from .participant_declaration_change_delivery_partner_request_data_attributes import (
        ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes,
    )
    from .participant_declaration_change_delivery_partner_request_data_attributes_declaration_type import (
        ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType,
    )
    from .participant_declaration_change_delivery_partner_request_data_type import (
        ParticipantDeclarationChangeDeliveryPartnerRequestDataType,
    )
    from .participant_declaration_request_data import ParticipantDeclarationRequestData
    from .participant_declaration_request_data_attributes import ParticipantDeclarationRequestDataAttributes
    from .participant_declaration_request_data_type import ParticipantDeclarationRequestDataType
_dynamic_imports: typing.Dict[str, str] = {
    "ParticipantDeclarationChangeDeliveryPartnerRequestData": ".participant_declaration_change_delivery_partner_request_data",
    "ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes": ".participant_declaration_change_delivery_partner_request_data_attributes",
    "ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType": ".participant_declaration_change_delivery_partner_request_data_attributes_declaration_type",
    "ParticipantDeclarationChangeDeliveryPartnerRequestDataType": ".participant_declaration_change_delivery_partner_request_data_type",
    "ParticipantDeclarationRequestData": ".participant_declaration_request_data",
    "ParticipantDeclarationRequestDataAttributes": ".participant_declaration_request_data_attributes",
    "ParticipantDeclarationRequestDataType": ".participant_declaration_request_data_type",
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
    "ParticipantDeclarationChangeDeliveryPartnerRequestData",
    "ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes",
    "ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType",
    "ParticipantDeclarationChangeDeliveryPartnerRequestDataType",
    "ParticipantDeclarationRequestData",
    "ParticipantDeclarationRequestDataAttributes",
    "ParticipantDeclarationRequestDataType",
]
