



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .patch_shelf_entries_request_entries_item import PatchShelfEntriesRequestEntriesItem
    from .patch_shelf_entries_request_entries_item_one import PatchShelfEntriesRequestEntriesItemOne
    from .patch_shelf_entries_request_entries_item_one_operation import PatchShelfEntriesRequestEntriesItemOneOperation
    from .patch_shelf_entries_request_entries_item_payload import PatchShelfEntriesRequestEntriesItemPayload
    from .patch_shelf_entries_request_entries_item_payload_operation import (
        PatchShelfEntriesRequestEntriesItemPayloadOperation,
    )
    from .patch_shelf_entries_request_entries_item_payload_payload import (
        PatchShelfEntriesRequestEntriesItemPayloadPayload,
    )
    from .patch_shelf_entries_request_entries_item_payload_payload_one_item import (
        PatchShelfEntriesRequestEntriesItemPayloadPayloadOneItem,
    )
    from .patch_shelf_entries_request_entries_item_payload_payload_zero import (
        PatchShelfEntriesRequestEntriesItemPayloadPayloadZero,
    )
    from .patch_shelf_notes_request_notes_item import PatchShelfNotesRequestNotesItem
    from .patch_shelf_notes_request_notes_item_payload import PatchShelfNotesRequestNotesItemPayload
    from .patch_shelf_notes_request_notes_item_payload_one_item import PatchShelfNotesRequestNotesItemPayloadOneItem
    from .patch_shelf_notes_request_notes_item_payload_zero import PatchShelfNotesRequestNotesItemPayloadZero
    from .patch_shelf_tags_request_tags_item import PatchShelfTagsRequestTagsItem
    from .patch_shelf_tags_request_tags_item_one import PatchShelfTagsRequestTagsItemOne
    from .patch_shelf_tags_request_tags_item_one_operation import PatchShelfTagsRequestTagsItemOneOperation
    from .patch_shelf_tags_request_tags_item_payload import PatchShelfTagsRequestTagsItemPayload
    from .patch_shelf_tags_request_tags_item_payload_operation import PatchShelfTagsRequestTagsItemPayloadOperation
    from .patch_shelf_tags_request_tags_item_payload_payload import PatchShelfTagsRequestTagsItemPayloadPayload
_dynamic_imports: typing.Dict[str, str] = {
    "PatchShelfEntriesRequestEntriesItem": ".patch_shelf_entries_request_entries_item",
    "PatchShelfEntriesRequestEntriesItemOne": ".patch_shelf_entries_request_entries_item_one",
    "PatchShelfEntriesRequestEntriesItemOneOperation": ".patch_shelf_entries_request_entries_item_one_operation",
    "PatchShelfEntriesRequestEntriesItemPayload": ".patch_shelf_entries_request_entries_item_payload",
    "PatchShelfEntriesRequestEntriesItemPayloadOperation": ".patch_shelf_entries_request_entries_item_payload_operation",
    "PatchShelfEntriesRequestEntriesItemPayloadPayload": ".patch_shelf_entries_request_entries_item_payload_payload",
    "PatchShelfEntriesRequestEntriesItemPayloadPayloadOneItem": ".patch_shelf_entries_request_entries_item_payload_payload_one_item",
    "PatchShelfEntriesRequestEntriesItemPayloadPayloadZero": ".patch_shelf_entries_request_entries_item_payload_payload_zero",
    "PatchShelfNotesRequestNotesItem": ".patch_shelf_notes_request_notes_item",
    "PatchShelfNotesRequestNotesItemPayload": ".patch_shelf_notes_request_notes_item_payload",
    "PatchShelfNotesRequestNotesItemPayloadOneItem": ".patch_shelf_notes_request_notes_item_payload_one_item",
    "PatchShelfNotesRequestNotesItemPayloadZero": ".patch_shelf_notes_request_notes_item_payload_zero",
    "PatchShelfTagsRequestTagsItem": ".patch_shelf_tags_request_tags_item",
    "PatchShelfTagsRequestTagsItemOne": ".patch_shelf_tags_request_tags_item_one",
    "PatchShelfTagsRequestTagsItemOneOperation": ".patch_shelf_tags_request_tags_item_one_operation",
    "PatchShelfTagsRequestTagsItemPayload": ".patch_shelf_tags_request_tags_item_payload",
    "PatchShelfTagsRequestTagsItemPayloadOperation": ".patch_shelf_tags_request_tags_item_payload_operation",
    "PatchShelfTagsRequestTagsItemPayloadPayload": ".patch_shelf_tags_request_tags_item_payload_payload",
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
    "PatchShelfEntriesRequestEntriesItem",
    "PatchShelfEntriesRequestEntriesItemOne",
    "PatchShelfEntriesRequestEntriesItemOneOperation",
    "PatchShelfEntriesRequestEntriesItemPayload",
    "PatchShelfEntriesRequestEntriesItemPayloadOperation",
    "PatchShelfEntriesRequestEntriesItemPayloadPayload",
    "PatchShelfEntriesRequestEntriesItemPayloadPayloadOneItem",
    "PatchShelfEntriesRequestEntriesItemPayloadPayloadZero",
    "PatchShelfNotesRequestNotesItem",
    "PatchShelfNotesRequestNotesItemPayload",
    "PatchShelfNotesRequestNotesItemPayloadOneItem",
    "PatchShelfNotesRequestNotesItemPayloadZero",
    "PatchShelfTagsRequestTagsItem",
    "PatchShelfTagsRequestTagsItemOne",
    "PatchShelfTagsRequestTagsItemOneOperation",
    "PatchShelfTagsRequestTagsItemPayload",
    "PatchShelfTagsRequestTagsItemPayloadOperation",
    "PatchShelfTagsRequestTagsItemPayloadPayload",
]
