



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .pipelines_count_pipelines_response import PipelinesCountPipelinesResponse
    from .pipelines_create_pipeline_request_integration_type import PipelinesCreatePipelineRequestIntegrationType
    from .pipelines_create_pipeline_request_producer_config import PipelinesCreatePipelineRequestProducerConfig
    from .pipelines_create_pipeline_request_producer_config_data import PipelinesCreatePipelineRequestProducerConfigData
    from .pipelines_create_pipeline_request_producer_config_data_channels_item import (
        PipelinesCreatePipelineRequestProducerConfigDataChannelsItem,
    )
    from .pipelines_create_pipeline_request_producer_config_type import PipelinesCreatePipelineRequestProducerConfigType
    from .pipelines_create_pipeline_response import PipelinesCreatePipelineResponse
    from .pipelines_create_pipeline_response_pipeline import PipelinesCreatePipelineResponsePipeline
    from .pipelines_create_pipeline_response_pipeline_config import PipelinesCreatePipelineResponsePipelineConfig
    from .pipelines_create_pipeline_response_pipeline_config_data import (
        PipelinesCreatePipelineResponsePipelineConfigData,
    )
    from .pipelines_create_pipeline_response_pipeline_config_data_channels_item import (
        PipelinesCreatePipelineResponsePipelineConfigDataChannelsItem,
    )
    from .pipelines_create_pipeline_response_pipeline_config_type import (
        PipelinesCreatePipelineResponsePipelineConfigType,
    )
    from .pipelines_create_pipeline_response_pipeline_integration_type import (
        PipelinesCreatePipelineResponsePipelineIntegrationType,
    )
    from .pipelines_delete_pipeline_response import PipelinesDeletePipelineResponse
    from .pipelines_get_pipeline_response import PipelinesGetPipelineResponse
    from .pipelines_get_pipeline_response_pipeline import PipelinesGetPipelineResponsePipeline
    from .pipelines_get_pipeline_response_pipeline_config import PipelinesGetPipelineResponsePipelineConfig
    from .pipelines_get_pipeline_response_pipeline_config_data import PipelinesGetPipelineResponsePipelineConfigData
    from .pipelines_get_pipeline_response_pipeline_config_data_channels_item import (
        PipelinesGetPipelineResponsePipelineConfigDataChannelsItem,
    )
    from .pipelines_get_pipeline_response_pipeline_config_type import PipelinesGetPipelineResponsePipelineConfigType
    from .pipelines_get_pipeline_response_pipeline_integration_type import (
        PipelinesGetPipelineResponsePipelineIntegrationType,
    )
    from .pipelines_list_pipeline_sync_history_response import PipelinesListPipelineSyncHistoryResponse
    from .pipelines_list_pipeline_sync_history_response_runs_item import (
        PipelinesListPipelineSyncHistoryResponseRunsItem,
    )
    from .pipelines_list_pipeline_sync_history_response_runs_item_error import (
        PipelinesListPipelineSyncHistoryResponseRunsItemError,
    )
    from .pipelines_list_pipeline_sync_history_response_runs_item_status import (
        PipelinesListPipelineSyncHistoryResponseRunsItemStatus,
    )
    from .pipelines_list_pipelines_response import PipelinesListPipelinesResponse
    from .pipelines_list_pipelines_response_pipelines_item import PipelinesListPipelinesResponsePipelinesItem
    from .pipelines_list_pipelines_response_pipelines_item_config import (
        PipelinesListPipelinesResponsePipelinesItemConfig,
    )
    from .pipelines_list_pipelines_response_pipelines_item_config_data import (
        PipelinesListPipelinesResponsePipelinesItemConfigData,
    )
    from .pipelines_list_pipelines_response_pipelines_item_config_data_channels_item import (
        PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem,
    )
    from .pipelines_list_pipelines_response_pipelines_item_config_type import (
        PipelinesListPipelinesResponsePipelinesItemConfigType,
    )
    from .pipelines_list_pipelines_response_pipelines_item_integration_type import (
        PipelinesListPipelinesResponsePipelinesItemIntegrationType,
    )
    from .pipelines_preview_pipeline_request_integration_type import PipelinesPreviewPipelineRequestIntegrationType
    from .pipelines_preview_pipeline_request_producer_config import PipelinesPreviewPipelineRequestProducerConfig
    from .pipelines_preview_pipeline_request_producer_config_data import (
        PipelinesPreviewPipelineRequestProducerConfigData,
    )
    from .pipelines_preview_pipeline_request_producer_config_data_channels_item import (
        PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem,
    )
    from .pipelines_preview_pipeline_request_producer_config_type import (
        PipelinesPreviewPipelineRequestProducerConfigType,
    )
    from .pipelines_preview_pipeline_response import PipelinesPreviewPipelineResponse
    from .pipelines_sync_pipeline_response import PipelinesSyncPipelineResponse
    from .pipelines_update_pipeline_response import PipelinesUpdatePipelineResponse
    from .pipelines_update_pipeline_response_pipeline import PipelinesUpdatePipelineResponsePipeline
    from .pipelines_update_pipeline_response_pipeline_config import PipelinesUpdatePipelineResponsePipelineConfig
    from .pipelines_update_pipeline_response_pipeline_config_data import (
        PipelinesUpdatePipelineResponsePipelineConfigData,
    )
    from .pipelines_update_pipeline_response_pipeline_config_data_channels_item import (
        PipelinesUpdatePipelineResponsePipelineConfigDataChannelsItem,
    )
    from .pipelines_update_pipeline_response_pipeline_config_type import (
        PipelinesUpdatePipelineResponsePipelineConfigType,
    )
    from .pipelines_update_pipeline_response_pipeline_integration_type import (
        PipelinesUpdatePipelineResponsePipelineIntegrationType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PipelinesCountPipelinesResponse": ".pipelines_count_pipelines_response",
    "PipelinesCreatePipelineRequestIntegrationType": ".pipelines_create_pipeline_request_integration_type",
    "PipelinesCreatePipelineRequestProducerConfig": ".pipelines_create_pipeline_request_producer_config",
    "PipelinesCreatePipelineRequestProducerConfigData": ".pipelines_create_pipeline_request_producer_config_data",
    "PipelinesCreatePipelineRequestProducerConfigDataChannelsItem": ".pipelines_create_pipeline_request_producer_config_data_channels_item",
    "PipelinesCreatePipelineRequestProducerConfigType": ".pipelines_create_pipeline_request_producer_config_type",
    "PipelinesCreatePipelineResponse": ".pipelines_create_pipeline_response",
    "PipelinesCreatePipelineResponsePipeline": ".pipelines_create_pipeline_response_pipeline",
    "PipelinesCreatePipelineResponsePipelineConfig": ".pipelines_create_pipeline_response_pipeline_config",
    "PipelinesCreatePipelineResponsePipelineConfigData": ".pipelines_create_pipeline_response_pipeline_config_data",
    "PipelinesCreatePipelineResponsePipelineConfigDataChannelsItem": ".pipelines_create_pipeline_response_pipeline_config_data_channels_item",
    "PipelinesCreatePipelineResponsePipelineConfigType": ".pipelines_create_pipeline_response_pipeline_config_type",
    "PipelinesCreatePipelineResponsePipelineIntegrationType": ".pipelines_create_pipeline_response_pipeline_integration_type",
    "PipelinesDeletePipelineResponse": ".pipelines_delete_pipeline_response",
    "PipelinesGetPipelineResponse": ".pipelines_get_pipeline_response",
    "PipelinesGetPipelineResponsePipeline": ".pipelines_get_pipeline_response_pipeline",
    "PipelinesGetPipelineResponsePipelineConfig": ".pipelines_get_pipeline_response_pipeline_config",
    "PipelinesGetPipelineResponsePipelineConfigData": ".pipelines_get_pipeline_response_pipeline_config_data",
    "PipelinesGetPipelineResponsePipelineConfigDataChannelsItem": ".pipelines_get_pipeline_response_pipeline_config_data_channels_item",
    "PipelinesGetPipelineResponsePipelineConfigType": ".pipelines_get_pipeline_response_pipeline_config_type",
    "PipelinesGetPipelineResponsePipelineIntegrationType": ".pipelines_get_pipeline_response_pipeline_integration_type",
    "PipelinesListPipelineSyncHistoryResponse": ".pipelines_list_pipeline_sync_history_response",
    "PipelinesListPipelineSyncHistoryResponseRunsItem": ".pipelines_list_pipeline_sync_history_response_runs_item",
    "PipelinesListPipelineSyncHistoryResponseRunsItemError": ".pipelines_list_pipeline_sync_history_response_runs_item_error",
    "PipelinesListPipelineSyncHistoryResponseRunsItemStatus": ".pipelines_list_pipeline_sync_history_response_runs_item_status",
    "PipelinesListPipelinesResponse": ".pipelines_list_pipelines_response",
    "PipelinesListPipelinesResponsePipelinesItem": ".pipelines_list_pipelines_response_pipelines_item",
    "PipelinesListPipelinesResponsePipelinesItemConfig": ".pipelines_list_pipelines_response_pipelines_item_config",
    "PipelinesListPipelinesResponsePipelinesItemConfigData": ".pipelines_list_pipelines_response_pipelines_item_config_data",
    "PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem": ".pipelines_list_pipelines_response_pipelines_item_config_data_channels_item",
    "PipelinesListPipelinesResponsePipelinesItemConfigType": ".pipelines_list_pipelines_response_pipelines_item_config_type",
    "PipelinesListPipelinesResponsePipelinesItemIntegrationType": ".pipelines_list_pipelines_response_pipelines_item_integration_type",
    "PipelinesPreviewPipelineRequestIntegrationType": ".pipelines_preview_pipeline_request_integration_type",
    "PipelinesPreviewPipelineRequestProducerConfig": ".pipelines_preview_pipeline_request_producer_config",
    "PipelinesPreviewPipelineRequestProducerConfigData": ".pipelines_preview_pipeline_request_producer_config_data",
    "PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem": ".pipelines_preview_pipeline_request_producer_config_data_channels_item",
    "PipelinesPreviewPipelineRequestProducerConfigType": ".pipelines_preview_pipeline_request_producer_config_type",
    "PipelinesPreviewPipelineResponse": ".pipelines_preview_pipeline_response",
    "PipelinesSyncPipelineResponse": ".pipelines_sync_pipeline_response",
    "PipelinesUpdatePipelineResponse": ".pipelines_update_pipeline_response",
    "PipelinesUpdatePipelineResponsePipeline": ".pipelines_update_pipeline_response_pipeline",
    "PipelinesUpdatePipelineResponsePipelineConfig": ".pipelines_update_pipeline_response_pipeline_config",
    "PipelinesUpdatePipelineResponsePipelineConfigData": ".pipelines_update_pipeline_response_pipeline_config_data",
    "PipelinesUpdatePipelineResponsePipelineConfigDataChannelsItem": ".pipelines_update_pipeline_response_pipeline_config_data_channels_item",
    "PipelinesUpdatePipelineResponsePipelineConfigType": ".pipelines_update_pipeline_response_pipeline_config_type",
    "PipelinesUpdatePipelineResponsePipelineIntegrationType": ".pipelines_update_pipeline_response_pipeline_integration_type",
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
    "PipelinesCountPipelinesResponse",
    "PipelinesCreatePipelineRequestIntegrationType",
    "PipelinesCreatePipelineRequestProducerConfig",
    "PipelinesCreatePipelineRequestProducerConfigData",
    "PipelinesCreatePipelineRequestProducerConfigDataChannelsItem",
    "PipelinesCreatePipelineRequestProducerConfigType",
    "PipelinesCreatePipelineResponse",
    "PipelinesCreatePipelineResponsePipeline",
    "PipelinesCreatePipelineResponsePipelineConfig",
    "PipelinesCreatePipelineResponsePipelineConfigData",
    "PipelinesCreatePipelineResponsePipelineConfigDataChannelsItem",
    "PipelinesCreatePipelineResponsePipelineConfigType",
    "PipelinesCreatePipelineResponsePipelineIntegrationType",
    "PipelinesDeletePipelineResponse",
    "PipelinesGetPipelineResponse",
    "PipelinesGetPipelineResponsePipeline",
    "PipelinesGetPipelineResponsePipelineConfig",
    "PipelinesGetPipelineResponsePipelineConfigData",
    "PipelinesGetPipelineResponsePipelineConfigDataChannelsItem",
    "PipelinesGetPipelineResponsePipelineConfigType",
    "PipelinesGetPipelineResponsePipelineIntegrationType",
    "PipelinesListPipelineSyncHistoryResponse",
    "PipelinesListPipelineSyncHistoryResponseRunsItem",
    "PipelinesListPipelineSyncHistoryResponseRunsItemError",
    "PipelinesListPipelineSyncHistoryResponseRunsItemStatus",
    "PipelinesListPipelinesResponse",
    "PipelinesListPipelinesResponsePipelinesItem",
    "PipelinesListPipelinesResponsePipelinesItemConfig",
    "PipelinesListPipelinesResponsePipelinesItemConfigData",
    "PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem",
    "PipelinesListPipelinesResponsePipelinesItemConfigType",
    "PipelinesListPipelinesResponsePipelinesItemIntegrationType",
    "PipelinesPreviewPipelineRequestIntegrationType",
    "PipelinesPreviewPipelineRequestProducerConfig",
    "PipelinesPreviewPipelineRequestProducerConfigData",
    "PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem",
    "PipelinesPreviewPipelineRequestProducerConfigType",
    "PipelinesPreviewPipelineResponse",
    "PipelinesSyncPipelineResponse",
    "PipelinesUpdatePipelineResponse",
    "PipelinesUpdatePipelineResponsePipeline",
    "PipelinesUpdatePipelineResponsePipelineConfig",
    "PipelinesUpdatePipelineResponsePipelineConfigData",
    "PipelinesUpdatePipelineResponsePipelineConfigDataChannelsItem",
    "PipelinesUpdatePipelineResponsePipelineConfigType",
    "PipelinesUpdatePipelineResponsePipelineIntegrationType",
]
