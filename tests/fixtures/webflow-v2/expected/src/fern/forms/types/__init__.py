



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .form_submission_payload import FormSubmissionPayload
    from .form_submission_payload_payload import FormSubmissionPayloadPayload
    from .form_submission_payload_payload_schema_item import FormSubmissionPayloadPayloadSchemaItem
    from .form_submission_payload_payload_schema_item_field_type import FormSubmissionPayloadPayloadSchemaItemFieldType
    from .get_forms_response import GetFormsResponse
    from .get_forms_response_fields_value import GetFormsResponseFieldsValue
    from .get_forms_response_fields_value_type import GetFormsResponseFieldsValueType
    from .get_forms_response_response_settings import GetFormsResponseResponseSettings
    from .get_submission_forms_response import GetSubmissionFormsResponse
    from .list_forms_response import ListFormsResponse
    from .list_forms_response_forms_item import ListFormsResponseFormsItem
    from .list_forms_response_forms_item_fields_value import ListFormsResponseFormsItemFieldsValue
    from .list_forms_response_forms_item_fields_value_type import ListFormsResponseFormsItemFieldsValueType
    from .list_forms_response_forms_item_response_settings import ListFormsResponseFormsItemResponseSettings
    from .list_forms_response_pagination import ListFormsResponsePagination
    from .list_submissions_forms_response import ListSubmissionsFormsResponse
    from .list_submissions_forms_response_form_submissions_item import ListSubmissionsFormsResponseFormSubmissionsItem
    from .list_submissions_forms_response_pagination import ListSubmissionsFormsResponsePagination
    from .update_submission_forms_response import UpdateSubmissionFormsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "FormSubmissionPayload": ".form_submission_payload",
    "FormSubmissionPayloadPayload": ".form_submission_payload_payload",
    "FormSubmissionPayloadPayloadSchemaItem": ".form_submission_payload_payload_schema_item",
    "FormSubmissionPayloadPayloadSchemaItemFieldType": ".form_submission_payload_payload_schema_item_field_type",
    "GetFormsResponse": ".get_forms_response",
    "GetFormsResponseFieldsValue": ".get_forms_response_fields_value",
    "GetFormsResponseFieldsValueType": ".get_forms_response_fields_value_type",
    "GetFormsResponseResponseSettings": ".get_forms_response_response_settings",
    "GetSubmissionFormsResponse": ".get_submission_forms_response",
    "ListFormsResponse": ".list_forms_response",
    "ListFormsResponseFormsItem": ".list_forms_response_forms_item",
    "ListFormsResponseFormsItemFieldsValue": ".list_forms_response_forms_item_fields_value",
    "ListFormsResponseFormsItemFieldsValueType": ".list_forms_response_forms_item_fields_value_type",
    "ListFormsResponseFormsItemResponseSettings": ".list_forms_response_forms_item_response_settings",
    "ListFormsResponsePagination": ".list_forms_response_pagination",
    "ListSubmissionsFormsResponse": ".list_submissions_forms_response",
    "ListSubmissionsFormsResponseFormSubmissionsItem": ".list_submissions_forms_response_form_submissions_item",
    "ListSubmissionsFormsResponsePagination": ".list_submissions_forms_response_pagination",
    "UpdateSubmissionFormsResponse": ".update_submission_forms_response",
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
    "FormSubmissionPayload",
    "FormSubmissionPayloadPayload",
    "FormSubmissionPayloadPayloadSchemaItem",
    "FormSubmissionPayloadPayloadSchemaItemFieldType",
    "GetFormsResponse",
    "GetFormsResponseFieldsValue",
    "GetFormsResponseFieldsValueType",
    "GetFormsResponseResponseSettings",
    "GetSubmissionFormsResponse",
    "ListFormsResponse",
    "ListFormsResponseFormsItem",
    "ListFormsResponseFormsItemFieldsValue",
    "ListFormsResponseFormsItemFieldsValueType",
    "ListFormsResponseFormsItemResponseSettings",
    "ListFormsResponsePagination",
    "ListSubmissionsFormsResponse",
    "ListSubmissionsFormsResponseFormSubmissionsItem",
    "ListSubmissionsFormsResponsePagination",
    "UpdateSubmissionFormsResponse",
]
