



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .collection_item_changed_payload import CollectionItemChangedPayload
    from .collection_item_changed_payload_payload import CollectionItemChangedPayloadPayload
    from .collection_item_changed_payload_payload_field_data import CollectionItemChangedPayloadPayloadFieldData
    from .collection_item_changed_payload_trigger_type import CollectionItemChangedPayloadTriggerType
    from .collection_item_created_payload import CollectionItemCreatedPayload
    from .collection_item_created_payload_payload import CollectionItemCreatedPayloadPayload
    from .collection_item_created_payload_payload_field_data import CollectionItemCreatedPayloadPayloadFieldData
    from .collection_item_created_payload_trigger_type import CollectionItemCreatedPayloadTriggerType
    from .collection_item_deleted_payload import CollectionItemDeletedPayload
    from .collection_item_deleted_payload_payload import CollectionItemDeletedPayloadPayload
    from .collection_item_deleted_payload_payload_field_data import CollectionItemDeletedPayloadPayloadFieldData
    from .collection_item_published_payload import CollectionItemPublishedPayload
    from .collection_item_published_payload_payload import CollectionItemPublishedPayloadPayload
    from .collection_item_published_payload_payload_field_data import CollectionItemPublishedPayloadPayloadFieldData
    from .collection_item_unpublished_payload import CollectionItemUnpublishedPayload
    from .collection_item_unpublished_payload_payload import CollectionItemUnpublishedPayloadPayload
    from .collection_item_unpublished_payload_payload_field_data import CollectionItemUnpublishedPayloadPayloadFieldData
_dynamic_imports: typing.Dict[str, str] = {
    "CollectionItemChangedPayload": ".collection_item_changed_payload",
    "CollectionItemChangedPayloadPayload": ".collection_item_changed_payload_payload",
    "CollectionItemChangedPayloadPayloadFieldData": ".collection_item_changed_payload_payload_field_data",
    "CollectionItemChangedPayloadTriggerType": ".collection_item_changed_payload_trigger_type",
    "CollectionItemCreatedPayload": ".collection_item_created_payload",
    "CollectionItemCreatedPayloadPayload": ".collection_item_created_payload_payload",
    "CollectionItemCreatedPayloadPayloadFieldData": ".collection_item_created_payload_payload_field_data",
    "CollectionItemCreatedPayloadTriggerType": ".collection_item_created_payload_trigger_type",
    "CollectionItemDeletedPayload": ".collection_item_deleted_payload",
    "CollectionItemDeletedPayloadPayload": ".collection_item_deleted_payload_payload",
    "CollectionItemDeletedPayloadPayloadFieldData": ".collection_item_deleted_payload_payload_field_data",
    "CollectionItemPublishedPayload": ".collection_item_published_payload",
    "CollectionItemPublishedPayloadPayload": ".collection_item_published_payload_payload",
    "CollectionItemPublishedPayloadPayloadFieldData": ".collection_item_published_payload_payload_field_data",
    "CollectionItemUnpublishedPayload": ".collection_item_unpublished_payload",
    "CollectionItemUnpublishedPayloadPayload": ".collection_item_unpublished_payload_payload",
    "CollectionItemUnpublishedPayloadPayloadFieldData": ".collection_item_unpublished_payload_payload_field_data",
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
    "CollectionItemChangedPayload",
    "CollectionItemChangedPayloadPayload",
    "CollectionItemChangedPayloadPayloadFieldData",
    "CollectionItemChangedPayloadTriggerType",
    "CollectionItemCreatedPayload",
    "CollectionItemCreatedPayloadPayload",
    "CollectionItemCreatedPayloadPayloadFieldData",
    "CollectionItemCreatedPayloadTriggerType",
    "CollectionItemDeletedPayload",
    "CollectionItemDeletedPayloadPayload",
    "CollectionItemDeletedPayloadPayloadFieldData",
    "CollectionItemPublishedPayload",
    "CollectionItemPublishedPayloadPayload",
    "CollectionItemPublishedPayloadPayloadFieldData",
    "CollectionItemUnpublishedPayload",
    "CollectionItemUnpublishedPayloadPayload",
    "CollectionItemUnpublishedPayloadPayloadFieldData",
]
