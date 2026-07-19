



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PipelinesCountPipelinesResponse,
        PipelinesCreatePipelineRequestIntegrationType,
        PipelinesCreatePipelineRequestProducerConfig,
        PipelinesCreatePipelineRequestProducerConfigData,
        PipelinesCreatePipelineRequestProducerConfigDataChannelsItem,
        PipelinesCreatePipelineRequestProducerConfigType,
        PipelinesCreatePipelineResponse,
        PipelinesCreatePipelineResponsePipeline,
        PipelinesCreatePipelineResponsePipelineConfig,
        PipelinesCreatePipelineResponsePipelineConfigData,
        PipelinesCreatePipelineResponsePipelineConfigDataChannelsItem,
        PipelinesCreatePipelineResponsePipelineConfigType,
        PipelinesCreatePipelineResponsePipelineIntegrationType,
        PipelinesDeletePipelineResponse,
        PipelinesGetPipelineResponse,
        PipelinesGetPipelineResponsePipeline,
        PipelinesGetPipelineResponsePipelineConfig,
        PipelinesGetPipelineResponsePipelineConfigData,
        PipelinesGetPipelineResponsePipelineConfigDataChannelsItem,
        PipelinesGetPipelineResponsePipelineConfigType,
        PipelinesGetPipelineResponsePipelineIntegrationType,
        PipelinesListPipelineSyncHistoryResponse,
        PipelinesListPipelineSyncHistoryResponseRunsItem,
        PipelinesListPipelineSyncHistoryResponseRunsItemError,
        PipelinesListPipelineSyncHistoryResponseRunsItemStatus,
        PipelinesListPipelinesResponse,
        PipelinesListPipelinesResponsePipelinesItem,
        PipelinesListPipelinesResponsePipelinesItemConfig,
        PipelinesListPipelinesResponsePipelinesItemConfigData,
        PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem,
        PipelinesListPipelinesResponsePipelinesItemConfigType,
        PipelinesListPipelinesResponsePipelinesItemIntegrationType,
        PipelinesPreviewPipelineRequestIntegrationType,
        PipelinesPreviewPipelineRequestProducerConfig,
        PipelinesPreviewPipelineRequestProducerConfigData,
        PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem,
        PipelinesPreviewPipelineRequestProducerConfigType,
        PipelinesPreviewPipelineResponse,
        PipelinesSyncPipelineResponse,
        PipelinesUpdatePipelineResponse,
        PipelinesUpdatePipelineResponsePipeline,
        PipelinesUpdatePipelineResponsePipelineConfig,
        PipelinesUpdatePipelineResponsePipelineConfigData,
        PipelinesUpdatePipelineResponsePipelineConfigDataChannelsItem,
        PipelinesUpdatePipelineResponsePipelineConfigType,
        PipelinesUpdatePipelineResponsePipelineIntegrationType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PipelinesCountPipelinesResponse": ".types",
    "PipelinesCreatePipelineRequestIntegrationType": ".types",
    "PipelinesCreatePipelineRequestProducerConfig": ".types",
    "PipelinesCreatePipelineRequestProducerConfigData": ".types",
    "PipelinesCreatePipelineRequestProducerConfigDataChannelsItem": ".types",
    "PipelinesCreatePipelineRequestProducerConfigType": ".types",
    "PipelinesCreatePipelineResponse": ".types",
    "PipelinesCreatePipelineResponsePipeline": ".types",
    "PipelinesCreatePipelineResponsePipelineConfig": ".types",
    "PipelinesCreatePipelineResponsePipelineConfigData": ".types",
    "PipelinesCreatePipelineResponsePipelineConfigDataChannelsItem": ".types",
    "PipelinesCreatePipelineResponsePipelineConfigType": ".types",
    "PipelinesCreatePipelineResponsePipelineIntegrationType": ".types",
    "PipelinesDeletePipelineResponse": ".types",
    "PipelinesGetPipelineResponse": ".types",
    "PipelinesGetPipelineResponsePipeline": ".types",
    "PipelinesGetPipelineResponsePipelineConfig": ".types",
    "PipelinesGetPipelineResponsePipelineConfigData": ".types",
    "PipelinesGetPipelineResponsePipelineConfigDataChannelsItem": ".types",
    "PipelinesGetPipelineResponsePipelineConfigType": ".types",
    "PipelinesGetPipelineResponsePipelineIntegrationType": ".types",
    "PipelinesListPipelineSyncHistoryResponse": ".types",
    "PipelinesListPipelineSyncHistoryResponseRunsItem": ".types",
    "PipelinesListPipelineSyncHistoryResponseRunsItemError": ".types",
    "PipelinesListPipelineSyncHistoryResponseRunsItemStatus": ".types",
    "PipelinesListPipelinesResponse": ".types",
    "PipelinesListPipelinesResponsePipelinesItem": ".types",
    "PipelinesListPipelinesResponsePipelinesItemConfig": ".types",
    "PipelinesListPipelinesResponsePipelinesItemConfigData": ".types",
    "PipelinesListPipelinesResponsePipelinesItemConfigDataChannelsItem": ".types",
    "PipelinesListPipelinesResponsePipelinesItemConfigType": ".types",
    "PipelinesListPipelinesResponsePipelinesItemIntegrationType": ".types",
    "PipelinesPreviewPipelineRequestIntegrationType": ".types",
    "PipelinesPreviewPipelineRequestProducerConfig": ".types",
    "PipelinesPreviewPipelineRequestProducerConfigData": ".types",
    "PipelinesPreviewPipelineRequestProducerConfigDataChannelsItem": ".types",
    "PipelinesPreviewPipelineRequestProducerConfigType": ".types",
    "PipelinesPreviewPipelineResponse": ".types",
    "PipelinesSyncPipelineResponse": ".types",
    "PipelinesUpdatePipelineResponse": ".types",
    "PipelinesUpdatePipelineResponsePipeline": ".types",
    "PipelinesUpdatePipelineResponsePipelineConfig": ".types",
    "PipelinesUpdatePipelineResponsePipelineConfigData": ".types",
    "PipelinesUpdatePipelineResponsePipelineConfigDataChannelsItem": ".types",
    "PipelinesUpdatePipelineResponsePipelineConfigType": ".types",
    "PipelinesUpdatePipelineResponsePipelineIntegrationType": ".types",
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
