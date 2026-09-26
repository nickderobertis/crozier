



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .contact_channel_verify_response import ContactChannelVerifyResponse
    from .contact_channel_verify_response_channel import ContactChannelVerifyResponseChannel
    from .contacts_prompt_submit_response import ContactsPromptSubmitResponse
    from .contacts_record_submit_request_expected_channels_item import ContactsRecordSubmitRequestExpectedChannelsItem
    from .contacts_record_submit_request_operation import ContactsRecordSubmitRequestOperation
    from .contacts_record_submit_response import ContactsRecordSubmitResponse
    from .contacts_upsert_request_assistant_metadata import ContactsUpsertRequestAssistantMetadata
    from .contacts_upsert_request_auto_approve_threshold import ContactsUpsertRequestAutoApproveThreshold
    from .contacts_upsert_request_channels_item import ContactsUpsertRequestChannelsItem
    from .contacts_upsert_response import ContactsUpsertResponse
    from .contacts_upsert_response_contact import ContactsUpsertResponseContact
    from .contacts_upsert_response_contact_assistant_metadata import ContactsUpsertResponseContactAssistantMetadata
    from .contacts_upsert_response_contact_auto_approve_threshold import (
        ContactsUpsertResponseContactAutoApproveThreshold,
    )
    from .contacts_upsert_response_contact_channels_item import ContactsUpsertResponseContactChannelsItem
_dynamic_imports: typing.Dict[str, str] = {
    "ContactChannelVerifyResponse": ".contact_channel_verify_response",
    "ContactChannelVerifyResponseChannel": ".contact_channel_verify_response_channel",
    "ContactsPromptSubmitResponse": ".contacts_prompt_submit_response",
    "ContactsRecordSubmitRequestExpectedChannelsItem": ".contacts_record_submit_request_expected_channels_item",
    "ContactsRecordSubmitRequestOperation": ".contacts_record_submit_request_operation",
    "ContactsRecordSubmitResponse": ".contacts_record_submit_response",
    "ContactsUpsertRequestAssistantMetadata": ".contacts_upsert_request_assistant_metadata",
    "ContactsUpsertRequestAutoApproveThreshold": ".contacts_upsert_request_auto_approve_threshold",
    "ContactsUpsertRequestChannelsItem": ".contacts_upsert_request_channels_item",
    "ContactsUpsertResponse": ".contacts_upsert_response",
    "ContactsUpsertResponseContact": ".contacts_upsert_response_contact",
    "ContactsUpsertResponseContactAssistantMetadata": ".contacts_upsert_response_contact_assistant_metadata",
    "ContactsUpsertResponseContactAutoApproveThreshold": ".contacts_upsert_response_contact_auto_approve_threshold",
    "ContactsUpsertResponseContactChannelsItem": ".contacts_upsert_response_contact_channels_item",
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
    "ContactChannelVerifyResponse",
    "ContactChannelVerifyResponseChannel",
    "ContactsPromptSubmitResponse",
    "ContactsRecordSubmitRequestExpectedChannelsItem",
    "ContactsRecordSubmitRequestOperation",
    "ContactsRecordSubmitResponse",
    "ContactsUpsertRequestAssistantMetadata",
    "ContactsUpsertRequestAutoApproveThreshold",
    "ContactsUpsertRequestChannelsItem",
    "ContactsUpsertResponse",
    "ContactsUpsertResponseContact",
    "ContactsUpsertResponseContactAssistantMetadata",
    "ContactsUpsertResponseContactAutoApproveThreshold",
    "ContactsUpsertResponseContactChannelsItem",
]
