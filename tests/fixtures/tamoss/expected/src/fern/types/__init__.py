



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .collection_item import CollectionItem
    from .container_mapping import ContainerMapping
    from .container_mapping_audio_track import ContainerMappingAudioTrack
    from .container_mapping_isobmff_container import ContainerMappingIsobmffContainer
    from .container_mapping_mp2ts_container import ContainerMappingMp2TsContainer
    from .container_mapping_mxf_container import ContainerMappingMxfContainer
    from .content_format import ContentFormat
    from .deletion_request import DeletionRequest
    from .deletion_request_status import DeletionRequestStatus
    from .error import Error
    from .error_payload import ErrorPayload
    from .event_stream_common import EventStreamCommon
    from .flow import Flow
    from .flow_audio import FlowAudio
    from .flow_audio_essence_parameters import FlowAudioEssenceParameters
    from .flow_audio_essence_parameters_codec_parameters import FlowAudioEssenceParametersCodecParameters
    from .flow_audio_essence_parameters_unc_parameters import FlowAudioEssenceParametersUncParameters
    from .flow_audio_essence_parameters_unc_parameters_unc_type import FlowAudioEssenceParametersUncParametersUncType
    from .flow_audio_format import FlowAudioFormat
    from .flow_collection import FlowCollection
    from .flow_collection_item import FlowCollectionItem
    from .flow_core import FlowCore
    from .flow_core_segment_duration import FlowCoreSegmentDuration
    from .flow_data import FlowData
    from .flow_data_essence_parameters import FlowDataEssenceParameters
    from .flow_data_format import FlowDataFormat
    from .flow_image import FlowImage
    from .flow_image_essence_parameters import FlowImageEssenceParameters
    from .flow_image_essence_parameters_aspect_ratio import FlowImageEssenceParametersAspectRatio
    from .flow_image_format import FlowImageFormat
    from .flow_multi import FlowMulti
    from .flow_multi_format import FlowMultiFormat
    from .flow_segment import FlowSegment
    from .flow_segment_bulk_failure import FlowSegmentBulkFailure
    from .flow_segment_bulk_failure_failed_segments_item import FlowSegmentBulkFailureFailedSegmentsItem
    from .flow_segment_post import FlowSegmentPost
    from .flow_segment_post_get_urls_item import FlowSegmentPostGetUrlsItem
    from .flow_storage import FlowStorage
    from .flow_storage_media_objects_item import FlowStorageMediaObjectsItem
    from .flow_video import FlowVideo
    from .flow_video_essence_parameters import FlowVideoEssenceParameters
    from .flow_video_essence_parameters_aspect_ratio import FlowVideoEssenceParametersAspectRatio
    from .flow_video_essence_parameters_avc_parameters import FlowVideoEssenceParametersAvcParameters
    from .flow_video_essence_parameters_colorspace import FlowVideoEssenceParametersColorspace
    from .flow_video_essence_parameters_component_type import FlowVideoEssenceParametersComponentType
    from .flow_video_essence_parameters_frame_rate import FlowVideoEssenceParametersFrameRate
    from .flow_video_essence_parameters_interlace_mode import FlowVideoEssenceParametersInterlaceMode
    from .flow_video_essence_parameters_pixel_aspect_ratio import FlowVideoEssenceParametersPixelAspectRatio
    from .flow_video_essence_parameters_transfer_characteristic import FlowVideoEssenceParametersTransferCharacteristic
    from .flow_video_essence_parameters_unc_parameters import FlowVideoEssenceParametersUncParameters
    from .flow_video_essence_parameters_unc_parameters_unc_type import FlowVideoEssenceParametersUncParametersUncType
    from .flow_video_format import FlowVideoFormat
    from .http_request import HttpRequest
    from .mime_type import MimeType
    from .object import Object
    from .object_core import ObjectCore
    from .object_core_get_urls_item import ObjectCoreGetUrlsItem
    from .objects_instances_post import ObjectsInstancesPost
    from .objects_instances_post_label import ObjectsInstancesPostLabel
    from .objects_instances_post_storage_id import ObjectsInstancesPostStorageId
    from .post_flows_created_payload import PostFlowsCreatedPayload
    from .post_flows_created_payload_event import PostFlowsCreatedPayloadEvent
    from .post_flows_created_payload_event_type import PostFlowsCreatedPayloadEventType
    from .post_flows_deleted_payload import PostFlowsDeletedPayload
    from .post_flows_deleted_payload_event import PostFlowsDeletedPayloadEvent
    from .post_flows_deleted_payload_event_type import PostFlowsDeletedPayloadEventType
    from .post_flows_segments_added_payload import PostFlowsSegmentsAddedPayload
    from .post_flows_segments_added_payload_event import PostFlowsSegmentsAddedPayloadEvent
    from .post_flows_segments_added_payload_event_type import PostFlowsSegmentsAddedPayloadEventType
    from .post_flows_segments_deleted_payload import PostFlowsSegmentsDeletedPayload
    from .post_flows_segments_deleted_payload_event import PostFlowsSegmentsDeletedPayloadEvent
    from .post_flows_segments_deleted_payload_event_type import PostFlowsSegmentsDeletedPayloadEventType
    from .post_flows_updated_payload import PostFlowsUpdatedPayload
    from .post_flows_updated_payload_event import PostFlowsUpdatedPayloadEvent
    from .post_flows_updated_payload_event_type import PostFlowsUpdatedPayloadEventType
    from .post_sources_created_payload import PostSourcesCreatedPayload
    from .post_sources_created_payload_event import PostSourcesCreatedPayloadEvent
    from .post_sources_created_payload_event_type import PostSourcesCreatedPayloadEventType
    from .post_sources_deleted_payload import PostSourcesDeletedPayload
    from .post_sources_deleted_payload_event import PostSourcesDeletedPayloadEvent
    from .post_sources_deleted_payload_event_type import PostSourcesDeletedPayloadEventType
    from .post_sources_updated_payload import PostSourcesUpdatedPayload
    from .post_sources_updated_payload_event import PostSourcesUpdatedPayloadEvent
    from .post_sources_updated_payload_event_type import PostSourcesUpdatedPayloadEventType
    from .service import Service
    from .source import Source
    from .storage_backend import StorageBackend
    from .storage_backend_store_type import StorageBackendStoreType
    from .storage_backends_list import StorageBackendsList
    from .storage_backends_list_item import StorageBackendsListItem
    from .tags import Tags
    from .tags_value import TagsValue
    from .timerange import Timerange
    from .timestamp import Timestamp
    from .url_label_list import UrlLabelList
    from .url_tag_list import UrlTagList
    from .uuid_ import Uuid
    from .uuid_list import UuidList
    from .webhook import Webhook
    from .webhook_events_item import WebhookEventsItem
    from .webhook_get import WebhookGet
    from .webhook_get_status import WebhookGetStatus
    from .webhook_with_id import WebhookWithId
_dynamic_imports: typing.Dict[str, str] = {
    "CollectionItem": ".collection_item",
    "ContainerMapping": ".container_mapping",
    "ContainerMappingAudioTrack": ".container_mapping_audio_track",
    "ContainerMappingIsobmffContainer": ".container_mapping_isobmff_container",
    "ContainerMappingMp2TsContainer": ".container_mapping_mp2ts_container",
    "ContainerMappingMxfContainer": ".container_mapping_mxf_container",
    "ContentFormat": ".content_format",
    "DeletionRequest": ".deletion_request",
    "DeletionRequestStatus": ".deletion_request_status",
    "Error": ".error",
    "ErrorPayload": ".error_payload",
    "EventStreamCommon": ".event_stream_common",
    "Flow": ".flow",
    "FlowAudio": ".flow_audio",
    "FlowAudioEssenceParameters": ".flow_audio_essence_parameters",
    "FlowAudioEssenceParametersCodecParameters": ".flow_audio_essence_parameters_codec_parameters",
    "FlowAudioEssenceParametersUncParameters": ".flow_audio_essence_parameters_unc_parameters",
    "FlowAudioEssenceParametersUncParametersUncType": ".flow_audio_essence_parameters_unc_parameters_unc_type",
    "FlowAudioFormat": ".flow_audio_format",
    "FlowCollection": ".flow_collection",
    "FlowCollectionItem": ".flow_collection_item",
    "FlowCore": ".flow_core",
    "FlowCoreSegmentDuration": ".flow_core_segment_duration",
    "FlowData": ".flow_data",
    "FlowDataEssenceParameters": ".flow_data_essence_parameters",
    "FlowDataFormat": ".flow_data_format",
    "FlowImage": ".flow_image",
    "FlowImageEssenceParameters": ".flow_image_essence_parameters",
    "FlowImageEssenceParametersAspectRatio": ".flow_image_essence_parameters_aspect_ratio",
    "FlowImageFormat": ".flow_image_format",
    "FlowMulti": ".flow_multi",
    "FlowMultiFormat": ".flow_multi_format",
    "FlowSegment": ".flow_segment",
    "FlowSegmentBulkFailure": ".flow_segment_bulk_failure",
    "FlowSegmentBulkFailureFailedSegmentsItem": ".flow_segment_bulk_failure_failed_segments_item",
    "FlowSegmentPost": ".flow_segment_post",
    "FlowSegmentPostGetUrlsItem": ".flow_segment_post_get_urls_item",
    "FlowStorage": ".flow_storage",
    "FlowStorageMediaObjectsItem": ".flow_storage_media_objects_item",
    "FlowVideo": ".flow_video",
    "FlowVideoEssenceParameters": ".flow_video_essence_parameters",
    "FlowVideoEssenceParametersAspectRatio": ".flow_video_essence_parameters_aspect_ratio",
    "FlowVideoEssenceParametersAvcParameters": ".flow_video_essence_parameters_avc_parameters",
    "FlowVideoEssenceParametersColorspace": ".flow_video_essence_parameters_colorspace",
    "FlowVideoEssenceParametersComponentType": ".flow_video_essence_parameters_component_type",
    "FlowVideoEssenceParametersFrameRate": ".flow_video_essence_parameters_frame_rate",
    "FlowVideoEssenceParametersInterlaceMode": ".flow_video_essence_parameters_interlace_mode",
    "FlowVideoEssenceParametersPixelAspectRatio": ".flow_video_essence_parameters_pixel_aspect_ratio",
    "FlowVideoEssenceParametersTransferCharacteristic": ".flow_video_essence_parameters_transfer_characteristic",
    "FlowVideoEssenceParametersUncParameters": ".flow_video_essence_parameters_unc_parameters",
    "FlowVideoEssenceParametersUncParametersUncType": ".flow_video_essence_parameters_unc_parameters_unc_type",
    "FlowVideoFormat": ".flow_video_format",
    "HttpRequest": ".http_request",
    "MimeType": ".mime_type",
    "Object": ".object",
    "ObjectCore": ".object_core",
    "ObjectCoreGetUrlsItem": ".object_core_get_urls_item",
    "ObjectsInstancesPost": ".objects_instances_post",
    "ObjectsInstancesPostLabel": ".objects_instances_post_label",
    "ObjectsInstancesPostStorageId": ".objects_instances_post_storage_id",
    "PostFlowsCreatedPayload": ".post_flows_created_payload",
    "PostFlowsCreatedPayloadEvent": ".post_flows_created_payload_event",
    "PostFlowsCreatedPayloadEventType": ".post_flows_created_payload_event_type",
    "PostFlowsDeletedPayload": ".post_flows_deleted_payload",
    "PostFlowsDeletedPayloadEvent": ".post_flows_deleted_payload_event",
    "PostFlowsDeletedPayloadEventType": ".post_flows_deleted_payload_event_type",
    "PostFlowsSegmentsAddedPayload": ".post_flows_segments_added_payload",
    "PostFlowsSegmentsAddedPayloadEvent": ".post_flows_segments_added_payload_event",
    "PostFlowsSegmentsAddedPayloadEventType": ".post_flows_segments_added_payload_event_type",
    "PostFlowsSegmentsDeletedPayload": ".post_flows_segments_deleted_payload",
    "PostFlowsSegmentsDeletedPayloadEvent": ".post_flows_segments_deleted_payload_event",
    "PostFlowsSegmentsDeletedPayloadEventType": ".post_flows_segments_deleted_payload_event_type",
    "PostFlowsUpdatedPayload": ".post_flows_updated_payload",
    "PostFlowsUpdatedPayloadEvent": ".post_flows_updated_payload_event",
    "PostFlowsUpdatedPayloadEventType": ".post_flows_updated_payload_event_type",
    "PostSourcesCreatedPayload": ".post_sources_created_payload",
    "PostSourcesCreatedPayloadEvent": ".post_sources_created_payload_event",
    "PostSourcesCreatedPayloadEventType": ".post_sources_created_payload_event_type",
    "PostSourcesDeletedPayload": ".post_sources_deleted_payload",
    "PostSourcesDeletedPayloadEvent": ".post_sources_deleted_payload_event",
    "PostSourcesDeletedPayloadEventType": ".post_sources_deleted_payload_event_type",
    "PostSourcesUpdatedPayload": ".post_sources_updated_payload",
    "PostSourcesUpdatedPayloadEvent": ".post_sources_updated_payload_event",
    "PostSourcesUpdatedPayloadEventType": ".post_sources_updated_payload_event_type",
    "Service": ".service",
    "Source": ".source",
    "StorageBackend": ".storage_backend",
    "StorageBackendStoreType": ".storage_backend_store_type",
    "StorageBackendsList": ".storage_backends_list",
    "StorageBackendsListItem": ".storage_backends_list_item",
    "Tags": ".tags",
    "TagsValue": ".tags_value",
    "Timerange": ".timerange",
    "Timestamp": ".timestamp",
    "UrlLabelList": ".url_label_list",
    "UrlTagList": ".url_tag_list",
    "Uuid": ".uuid_",
    "UuidList": ".uuid_list",
    "Webhook": ".webhook",
    "WebhookEventsItem": ".webhook_events_item",
    "WebhookGet": ".webhook_get",
    "WebhookGetStatus": ".webhook_get_status",
    "WebhookWithId": ".webhook_with_id",
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
    "CollectionItem",
    "ContainerMapping",
    "ContainerMappingAudioTrack",
    "ContainerMappingIsobmffContainer",
    "ContainerMappingMp2TsContainer",
    "ContainerMappingMxfContainer",
    "ContentFormat",
    "DeletionRequest",
    "DeletionRequestStatus",
    "Error",
    "ErrorPayload",
    "EventStreamCommon",
    "Flow",
    "FlowAudio",
    "FlowAudioEssenceParameters",
    "FlowAudioEssenceParametersCodecParameters",
    "FlowAudioEssenceParametersUncParameters",
    "FlowAudioEssenceParametersUncParametersUncType",
    "FlowAudioFormat",
    "FlowCollection",
    "FlowCollectionItem",
    "FlowCore",
    "FlowCoreSegmentDuration",
    "FlowData",
    "FlowDataEssenceParameters",
    "FlowDataFormat",
    "FlowImage",
    "FlowImageEssenceParameters",
    "FlowImageEssenceParametersAspectRatio",
    "FlowImageFormat",
    "FlowMulti",
    "FlowMultiFormat",
    "FlowSegment",
    "FlowSegmentBulkFailure",
    "FlowSegmentBulkFailureFailedSegmentsItem",
    "FlowSegmentPost",
    "FlowSegmentPostGetUrlsItem",
    "FlowStorage",
    "FlowStorageMediaObjectsItem",
    "FlowVideo",
    "FlowVideoEssenceParameters",
    "FlowVideoEssenceParametersAspectRatio",
    "FlowVideoEssenceParametersAvcParameters",
    "FlowVideoEssenceParametersColorspace",
    "FlowVideoEssenceParametersComponentType",
    "FlowVideoEssenceParametersFrameRate",
    "FlowVideoEssenceParametersInterlaceMode",
    "FlowVideoEssenceParametersPixelAspectRatio",
    "FlowVideoEssenceParametersTransferCharacteristic",
    "FlowVideoEssenceParametersUncParameters",
    "FlowVideoEssenceParametersUncParametersUncType",
    "FlowVideoFormat",
    "HttpRequest",
    "MimeType",
    "Object",
    "ObjectCore",
    "ObjectCoreGetUrlsItem",
    "ObjectsInstancesPost",
    "ObjectsInstancesPostLabel",
    "ObjectsInstancesPostStorageId",
    "PostFlowsCreatedPayload",
    "PostFlowsCreatedPayloadEvent",
    "PostFlowsCreatedPayloadEventType",
    "PostFlowsDeletedPayload",
    "PostFlowsDeletedPayloadEvent",
    "PostFlowsDeletedPayloadEventType",
    "PostFlowsSegmentsAddedPayload",
    "PostFlowsSegmentsAddedPayloadEvent",
    "PostFlowsSegmentsAddedPayloadEventType",
    "PostFlowsSegmentsDeletedPayload",
    "PostFlowsSegmentsDeletedPayloadEvent",
    "PostFlowsSegmentsDeletedPayloadEventType",
    "PostFlowsUpdatedPayload",
    "PostFlowsUpdatedPayloadEvent",
    "PostFlowsUpdatedPayloadEventType",
    "PostSourcesCreatedPayload",
    "PostSourcesCreatedPayloadEvent",
    "PostSourcesCreatedPayloadEventType",
    "PostSourcesDeletedPayload",
    "PostSourcesDeletedPayloadEvent",
    "PostSourcesDeletedPayloadEventType",
    "PostSourcesUpdatedPayload",
    "PostSourcesUpdatedPayloadEvent",
    "PostSourcesUpdatedPayloadEventType",
    "Service",
    "Source",
    "StorageBackend",
    "StorageBackendStoreType",
    "StorageBackendsList",
    "StorageBackendsListItem",
    "Tags",
    "TagsValue",
    "Timerange",
    "Timestamp",
    "UrlLabelList",
    "UrlTagList",
    "Uuid",
    "UuidList",
    "Webhook",
    "WebhookEventsItem",
    "WebhookGet",
    "WebhookGetStatus",
    "WebhookWithId",
]
