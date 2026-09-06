



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_collections_request_fields_item import CreateCollectionsRequestFieldsItem
    from .create_collections_response import CreateCollectionsResponse
    from .create_collections_response_field_groups_item import CreateCollectionsResponseFieldGroupsItem
    from .create_collections_response_fields_item import CreateCollectionsResponseFieldsItem
    from .create_collections_response_fields_item_type import CreateCollectionsResponseFieldsItemType
    from .create_collections_response_fields_item_validations import CreateCollectionsResponseFieldsItemValidations
    from .create_collections_response_fields_item_validations_additional_properties import (
        CreateCollectionsResponseFieldsItemValidationsAdditionalProperties,
    )
    from .get_collections_response import GetCollectionsResponse
    from .get_collections_response_field_groups_item import GetCollectionsResponseFieldGroupsItem
    from .get_collections_response_fields_item import GetCollectionsResponseFieldsItem
    from .get_collections_response_fields_item_type import GetCollectionsResponseFieldsItemType
    from .get_collections_response_fields_item_validations import GetCollectionsResponseFieldsItemValidations
    from .get_collections_response_fields_item_validations_additional_properties import (
        GetCollectionsResponseFieldsItemValidationsAdditionalProperties,
    )
    from .list_collections_response import ListCollectionsResponse
    from .list_collections_response_collections_item import ListCollectionsResponseCollectionsItem
    from .option_field import OptionField
    from .option_field_metadata import OptionFieldMetadata
    from .option_field_metadata_options_item import OptionFieldMetadataOptionsItem
    from .option_field_type import OptionFieldType
    from .patch_collections_request_field_groups_item import PatchCollectionsRequestFieldGroupsItem
    from .patch_collections_response import PatchCollectionsResponse
    from .patch_collections_response_field_groups_item import PatchCollectionsResponseFieldGroupsItem
    from .patch_collections_response_fields_item import PatchCollectionsResponseFieldsItem
    from .patch_collections_response_fields_item_type import PatchCollectionsResponseFieldsItemType
    from .patch_collections_response_fields_item_validations import PatchCollectionsResponseFieldsItemValidations
    from .patch_collections_response_fields_item_validations_additional_properties import (
        PatchCollectionsResponseFieldsItemValidationsAdditionalProperties,
    )
    from .reference_field import ReferenceField
    from .reference_field_metadata import ReferenceFieldMetadata
    from .reference_field_type import ReferenceFieldType
    from .static_field import StaticField
    from .static_field_type import StaticFieldType
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCollectionsRequestFieldsItem": ".create_collections_request_fields_item",
    "CreateCollectionsResponse": ".create_collections_response",
    "CreateCollectionsResponseFieldGroupsItem": ".create_collections_response_field_groups_item",
    "CreateCollectionsResponseFieldsItem": ".create_collections_response_fields_item",
    "CreateCollectionsResponseFieldsItemType": ".create_collections_response_fields_item_type",
    "CreateCollectionsResponseFieldsItemValidations": ".create_collections_response_fields_item_validations",
    "CreateCollectionsResponseFieldsItemValidationsAdditionalProperties": ".create_collections_response_fields_item_validations_additional_properties",
    "GetCollectionsResponse": ".get_collections_response",
    "GetCollectionsResponseFieldGroupsItem": ".get_collections_response_field_groups_item",
    "GetCollectionsResponseFieldsItem": ".get_collections_response_fields_item",
    "GetCollectionsResponseFieldsItemType": ".get_collections_response_fields_item_type",
    "GetCollectionsResponseFieldsItemValidations": ".get_collections_response_fields_item_validations",
    "GetCollectionsResponseFieldsItemValidationsAdditionalProperties": ".get_collections_response_fields_item_validations_additional_properties",
    "ListCollectionsResponse": ".list_collections_response",
    "ListCollectionsResponseCollectionsItem": ".list_collections_response_collections_item",
    "OptionField": ".option_field",
    "OptionFieldMetadata": ".option_field_metadata",
    "OptionFieldMetadataOptionsItem": ".option_field_metadata_options_item",
    "OptionFieldType": ".option_field_type",
    "PatchCollectionsRequestFieldGroupsItem": ".patch_collections_request_field_groups_item",
    "PatchCollectionsResponse": ".patch_collections_response",
    "PatchCollectionsResponseFieldGroupsItem": ".patch_collections_response_field_groups_item",
    "PatchCollectionsResponseFieldsItem": ".patch_collections_response_fields_item",
    "PatchCollectionsResponseFieldsItemType": ".patch_collections_response_fields_item_type",
    "PatchCollectionsResponseFieldsItemValidations": ".patch_collections_response_fields_item_validations",
    "PatchCollectionsResponseFieldsItemValidationsAdditionalProperties": ".patch_collections_response_fields_item_validations_additional_properties",
    "ReferenceField": ".reference_field",
    "ReferenceFieldMetadata": ".reference_field_metadata",
    "ReferenceFieldType": ".reference_field_type",
    "StaticField": ".static_field",
    "StaticFieldType": ".static_field_type",
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
    "CreateCollectionsRequestFieldsItem",
    "CreateCollectionsResponse",
    "CreateCollectionsResponseFieldGroupsItem",
    "CreateCollectionsResponseFieldsItem",
    "CreateCollectionsResponseFieldsItemType",
    "CreateCollectionsResponseFieldsItemValidations",
    "CreateCollectionsResponseFieldsItemValidationsAdditionalProperties",
    "GetCollectionsResponse",
    "GetCollectionsResponseFieldGroupsItem",
    "GetCollectionsResponseFieldsItem",
    "GetCollectionsResponseFieldsItemType",
    "GetCollectionsResponseFieldsItemValidations",
    "GetCollectionsResponseFieldsItemValidationsAdditionalProperties",
    "ListCollectionsResponse",
    "ListCollectionsResponseCollectionsItem",
    "OptionField",
    "OptionFieldMetadata",
    "OptionFieldMetadataOptionsItem",
    "OptionFieldType",
    "PatchCollectionsRequestFieldGroupsItem",
    "PatchCollectionsResponse",
    "PatchCollectionsResponseFieldGroupsItem",
    "PatchCollectionsResponseFieldsItem",
    "PatchCollectionsResponseFieldsItemType",
    "PatchCollectionsResponseFieldsItemValidations",
    "PatchCollectionsResponseFieldsItemValidationsAdditionalProperties",
    "ReferenceField",
    "ReferenceFieldMetadata",
    "ReferenceFieldType",
    "StaticField",
    "StaticFieldType",
]
