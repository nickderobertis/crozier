



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .pipelines_check_request_only import PipelinesCheckRequestOnly
    from .pipelines_create_request_streams_item import PipelinesCreateRequestStreamsItem
    from .pipelines_create_request_streams_item_sync_mode import PipelinesCreateRequestStreamsItemSyncMode
    from .pipelines_delete_response import PipelinesDeleteResponse
    from .pipelines_list_response import PipelinesListResponse
    from .pipelines_setup_request_only import PipelinesSetupRequestOnly
    from .pipelines_sync_batch_request_streams_item import PipelinesSyncBatchRequestStreamsItem
    from .pipelines_sync_batch_request_streams_item_sync_mode import PipelinesSyncBatchRequestStreamsItemSyncMode
    from .pipelines_sync_request_streams_item import PipelinesSyncRequestStreamsItem
    from .pipelines_sync_request_streams_item_sync_mode import PipelinesSyncRequestStreamsItemSyncMode
    from .pipelines_sync_workflow_test_response import PipelinesSyncWorkflowTestResponse
    from .pipelines_teardown_request_only import PipelinesTeardownRequestOnly
    from .pipelines_update_request_desired_status import PipelinesUpdateRequestDesiredStatus
    from .pipelines_update_request_streams_item import PipelinesUpdateRequestStreamsItem
    from .pipelines_update_request_streams_item_sync_mode import PipelinesUpdateRequestStreamsItemSyncMode
_dynamic_imports: typing.Dict[str, str] = {
    "PipelinesCheckRequestOnly": ".pipelines_check_request_only",
    "PipelinesCreateRequestStreamsItem": ".pipelines_create_request_streams_item",
    "PipelinesCreateRequestStreamsItemSyncMode": ".pipelines_create_request_streams_item_sync_mode",
    "PipelinesDeleteResponse": ".pipelines_delete_response",
    "PipelinesListResponse": ".pipelines_list_response",
    "PipelinesSetupRequestOnly": ".pipelines_setup_request_only",
    "PipelinesSyncBatchRequestStreamsItem": ".pipelines_sync_batch_request_streams_item",
    "PipelinesSyncBatchRequestStreamsItemSyncMode": ".pipelines_sync_batch_request_streams_item_sync_mode",
    "PipelinesSyncRequestStreamsItem": ".pipelines_sync_request_streams_item",
    "PipelinesSyncRequestStreamsItemSyncMode": ".pipelines_sync_request_streams_item_sync_mode",
    "PipelinesSyncWorkflowTestResponse": ".pipelines_sync_workflow_test_response",
    "PipelinesTeardownRequestOnly": ".pipelines_teardown_request_only",
    "PipelinesUpdateRequestDesiredStatus": ".pipelines_update_request_desired_status",
    "PipelinesUpdateRequestStreamsItem": ".pipelines_update_request_streams_item",
    "PipelinesUpdateRequestStreamsItemSyncMode": ".pipelines_update_request_streams_item_sync_mode",
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
    "PipelinesCheckRequestOnly",
    "PipelinesCreateRequestStreamsItem",
    "PipelinesCreateRequestStreamsItemSyncMode",
    "PipelinesDeleteResponse",
    "PipelinesListResponse",
    "PipelinesSetupRequestOnly",
    "PipelinesSyncBatchRequestStreamsItem",
    "PipelinesSyncBatchRequestStreamsItemSyncMode",
    "PipelinesSyncRequestStreamsItem",
    "PipelinesSyncRequestStreamsItemSyncMode",
    "PipelinesSyncWorkflowTestResponse",
    "PipelinesTeardownRequestOnly",
    "PipelinesUpdateRequestDesiredStatus",
    "PipelinesUpdateRequestStreamsItem",
    "PipelinesUpdateRequestStreamsItemSyncMode",
]
