



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_fields_request_body import CreateFieldsRequestBody
    from .create_fields_response import CreateFieldsResponse
    from .option_field import OptionField
    from .option_field_metadata import OptionFieldMetadata
    from .option_field_metadata_options_item import OptionFieldMetadataOptionsItem
    from .option_field_type import OptionFieldType
    from .reference_field import ReferenceField
    from .reference_field_metadata import ReferenceFieldMetadata
    from .reference_field_type import ReferenceFieldType
    from .static_field import StaticField
    from .static_field_type import StaticFieldType
    from .update_fields_response import UpdateFieldsResponse
    from .update_fields_response_type import UpdateFieldsResponseType
    from .update_fields_response_validations import UpdateFieldsResponseValidations
    from .update_fields_response_validations_additional_properties import (
        UpdateFieldsResponseValidationsAdditionalProperties,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateFieldsRequestBody": ".create_fields_request_body",
    "CreateFieldsResponse": ".create_fields_response",
    "OptionField": ".option_field",
    "OptionFieldMetadata": ".option_field_metadata",
    "OptionFieldMetadataOptionsItem": ".option_field_metadata_options_item",
    "OptionFieldType": ".option_field_type",
    "ReferenceField": ".reference_field",
    "ReferenceFieldMetadata": ".reference_field_metadata",
    "ReferenceFieldType": ".reference_field_type",
    "StaticField": ".static_field",
    "StaticFieldType": ".static_field_type",
    "UpdateFieldsResponse": ".update_fields_response",
    "UpdateFieldsResponseType": ".update_fields_response_type",
    "UpdateFieldsResponseValidations": ".update_fields_response_validations",
    "UpdateFieldsResponseValidationsAdditionalProperties": ".update_fields_response_validations_additional_properties",
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
    "CreateFieldsRequestBody",
    "CreateFieldsResponse",
    "OptionField",
    "OptionFieldMetadata",
    "OptionFieldMetadataOptionsItem",
    "OptionFieldType",
    "ReferenceField",
    "ReferenceFieldMetadata",
    "ReferenceFieldType",
    "StaticField",
    "StaticFieldType",
    "UpdateFieldsResponse",
    "UpdateFieldsResponseType",
    "UpdateFieldsResponseValidations",
    "UpdateFieldsResponseValidationsAdditionalProperties",
]
