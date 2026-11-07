



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .catalog_message import CatalogMessage
    from .catalog_message_catalog import CatalogMessageCatalog
    from .catalog_message_catalog_streams_item import CatalogMessageCatalogStreamsItem
    from .check_output import CheckOutput, CheckOutput_ConnectionStatus, CheckOutput_Log
    from .connection_status_message import ConnectionStatusMessage
    from .connection_status_message_connection_status import ConnectionStatusMessageConnectionStatus
    from .connection_status_message_connection_status_status import ConnectionStatusMessageConnectionStatusStatus
    from .control_message import ControlMessage
    from .control_message_control import (
        ControlMessageControl,
        ControlMessageControl_DestinationConfig,
        ControlMessageControl_SourceConfig,
    )
    from .control_message_control_destination_config import ControlMessageControlDestinationConfig
    from .control_message_control_destination_config_destination_config import (
        ControlMessageControlDestinationConfigDestinationConfig,
    )
    from .control_message_control_source_config import ControlMessageControlSourceConfig
    from .control_message_control_source_config_source_config import ControlMessageControlSourceConfigSourceConfig
    from .destination_config import (
        DestinationConfig,
        DestinationConfig_GoogleSheets,
        DestinationConfig_Postgres,
        DestinationConfig_Redis,
        DestinationConfig_Stripe,
    )
    from .destination_config_google_sheets import DestinationConfigGoogleSheets
    from .destination_config_postgres import DestinationConfigPostgres
    from .destination_config_redis import DestinationConfigRedis
    from .destination_config_stripe import DestinationConfigStripe
    from .destination_google_sheets_config import DestinationGoogleSheetsConfig
    from .destination_output import DestinationOutput
    from .destination_postgres_config import DestinationPostgresConfig
    from .destination_postgres_config_aws import DestinationPostgresConfigAws
    from .destination_redis_config import DestinationRedisConfig
    from .destination_stripe_config import DestinationStripeConfig
    from .destination_stripe_config_api_version import DestinationStripeConfigApiVersion
    from .destination_stripe_config_object import DestinationStripeConfigObject
    from .destination_stripe_config_streams_value import DestinationStripeConfigStreamsValue
    from .destination_stripe_config_write_mode import DestinationStripeConfigWriteMode
    from .discover_output import DiscoverOutput, DiscoverOutput_Catalog, DiscoverOutput_Log
    from .eof_message import EofMessage
    from .eof_payload import EofPayload
    from .log_message import LogMessage
    from .log_message_log import LogMessageLog
    from .log_message_log_level import LogMessageLogLevel
    from .message import (
        Message,
        Message_Catalog,
        Message_ConnectionStatus,
        Message_Control,
        Message_Eof,
        Message_Log,
        Message_Progress,
        Message_Record,
        Message_SourceInput,
        Message_SourceState,
        Message_Spec,
        Message_StreamStatus,
    )
    from .pipeline_config import PipelineConfig
    from .pipeline_config_streams_item import PipelineConfigStreamsItem
    from .pipeline_config_streams_item_sync_mode import PipelineConfigStreamsItemSyncMode
    from .progress_message import ProgressMessage
    from .progress_payload import ProgressPayload
    from .progress_payload_connection_status import ProgressPayloadConnectionStatus
    from .progress_payload_connection_status_status import ProgressPayloadConnectionStatusStatus
    from .progress_payload_derived import ProgressPayloadDerived
    from .record_message import RecordMessage
    from .record_message_record import RecordMessageRecord
    from .run_status import RunStatus
    from .setup_output import SetupOutput, SetupOutput_Control, SetupOutput_Log
    from .source_config import SourceConfig, SourceConfig_Metronome, SourceConfig_Postgres, SourceConfig_Stripe
    from .source_config_metronome import SourceConfigMetronome
    from .source_config_postgres import SourceConfigPostgres
    from .source_config_stripe import SourceConfigStripe
    from .source_input_message import SourceInputMessage
    from .source_metronome_config import SourceMetronomeConfig
    from .source_postgres_config import SourcePostgresConfig
    from .source_state import SourceState
    from .source_state_message import SourceStateMessage
    from .source_state_message_source_state import (
        SourceStateMessageSourceState,
        SourceStateMessageSourceState_Global,
        SourceStateMessageSourceState_Stream,
    )
    from .source_state_message_source_state_global import SourceStateMessageSourceStateGlobal
    from .source_state_message_source_state_stream import SourceStateMessageSourceStateStream
    from .source_stripe_config import SourceStripeConfig
    from .source_stripe_config_api_version import SourceStripeConfigApiVersion
    from .spec_message import SpecMessage
    from .spec_message_spec import SpecMessageSpec
    from .stream_progress import StreamProgress
    from .stream_progress_completed_ranges_item import StreamProgressCompletedRangesItem
    from .stream_progress_status import StreamProgressStatus
    from .stream_progress_total_range import StreamProgressTotalRange
    from .stream_status_message import StreamStatusMessage
    from .stream_status_message_stream_status import (
        StreamStatusMessageStreamStatus,
        StreamStatusMessageStreamStatus_Complete,
        StreamStatusMessageStreamStatus_Error,
        StreamStatusMessageStreamStatus_RangeComplete,
        StreamStatusMessageStreamStatus_Skip,
        StreamStatusMessageStreamStatus_Start,
    )
    from .stream_status_message_stream_status_complete import StreamStatusMessageStreamStatusComplete
    from .stream_status_message_stream_status_error import StreamStatusMessageStreamStatusError
    from .stream_status_message_stream_status_range_complete import StreamStatusMessageStreamStatusRangeComplete
    from .stream_status_message_stream_status_range_complete_range_complete import (
        StreamStatusMessageStreamStatusRangeCompleteRangeComplete,
    )
    from .stream_status_message_stream_status_skip import StreamStatusMessageStreamStatusSkip
    from .stream_status_message_stream_status_start import StreamStatusMessageStreamStatusStart
    from .stream_status_message_stream_status_start_time_range import StreamStatusMessageStreamStatusStartTimeRange
    from .sync_output import (
        SyncOutput,
        SyncOutput_ConnectionStatus,
        SyncOutput_Control,
        SyncOutput_Eof,
        SyncOutput_Log,
        SyncOutput_Progress,
        SyncOutput_SourceState,
        SyncOutput_StreamStatus,
    )
    from .sync_state import SyncState
    from .sync_state_sync_run import SyncStateSyncRun
    from .teardown_output import TeardownOutput, TeardownOutput_Log
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "CatalogMessage": ".catalog_message",
    "CatalogMessageCatalog": ".catalog_message_catalog",
    "CatalogMessageCatalogStreamsItem": ".catalog_message_catalog_streams_item",
    "CheckOutput": ".check_output",
    "CheckOutput_ConnectionStatus": ".check_output",
    "CheckOutput_Log": ".check_output",
    "ConnectionStatusMessage": ".connection_status_message",
    "ConnectionStatusMessageConnectionStatus": ".connection_status_message_connection_status",
    "ConnectionStatusMessageConnectionStatusStatus": ".connection_status_message_connection_status_status",
    "ControlMessage": ".control_message",
    "ControlMessageControl": ".control_message_control",
    "ControlMessageControlDestinationConfig": ".control_message_control_destination_config",
    "ControlMessageControlDestinationConfigDestinationConfig": ".control_message_control_destination_config_destination_config",
    "ControlMessageControlSourceConfig": ".control_message_control_source_config",
    "ControlMessageControlSourceConfigSourceConfig": ".control_message_control_source_config_source_config",
    "ControlMessageControl_DestinationConfig": ".control_message_control",
    "ControlMessageControl_SourceConfig": ".control_message_control",
    "DestinationConfig": ".destination_config",
    "DestinationConfigGoogleSheets": ".destination_config_google_sheets",
    "DestinationConfigPostgres": ".destination_config_postgres",
    "DestinationConfigRedis": ".destination_config_redis",
    "DestinationConfigStripe": ".destination_config_stripe",
    "DestinationConfig_GoogleSheets": ".destination_config",
    "DestinationConfig_Postgres": ".destination_config",
    "DestinationConfig_Redis": ".destination_config",
    "DestinationConfig_Stripe": ".destination_config",
    "DestinationGoogleSheetsConfig": ".destination_google_sheets_config",
    "DestinationOutput": ".destination_output",
    "DestinationPostgresConfig": ".destination_postgres_config",
    "DestinationPostgresConfigAws": ".destination_postgres_config_aws",
    "DestinationRedisConfig": ".destination_redis_config",
    "DestinationStripeConfig": ".destination_stripe_config",
    "DestinationStripeConfigApiVersion": ".destination_stripe_config_api_version",
    "DestinationStripeConfigObject": ".destination_stripe_config_object",
    "DestinationStripeConfigStreamsValue": ".destination_stripe_config_streams_value",
    "DestinationStripeConfigWriteMode": ".destination_stripe_config_write_mode",
    "DiscoverOutput": ".discover_output",
    "DiscoverOutput_Catalog": ".discover_output",
    "DiscoverOutput_Log": ".discover_output",
    "EofMessage": ".eof_message",
    "EofPayload": ".eof_payload",
    "LogMessage": ".log_message",
    "LogMessageLog": ".log_message_log",
    "LogMessageLogLevel": ".log_message_log_level",
    "Message": ".message",
    "Message_Catalog": ".message",
    "Message_ConnectionStatus": ".message",
    "Message_Control": ".message",
    "Message_Eof": ".message",
    "Message_Log": ".message",
    "Message_Progress": ".message",
    "Message_Record": ".message",
    "Message_SourceInput": ".message",
    "Message_SourceState": ".message",
    "Message_Spec": ".message",
    "Message_StreamStatus": ".message",
    "PipelineConfig": ".pipeline_config",
    "PipelineConfigStreamsItem": ".pipeline_config_streams_item",
    "PipelineConfigStreamsItemSyncMode": ".pipeline_config_streams_item_sync_mode",
    "ProgressMessage": ".progress_message",
    "ProgressPayload": ".progress_payload",
    "ProgressPayloadConnectionStatus": ".progress_payload_connection_status",
    "ProgressPayloadConnectionStatusStatus": ".progress_payload_connection_status_status",
    "ProgressPayloadDerived": ".progress_payload_derived",
    "RecordMessage": ".record_message",
    "RecordMessageRecord": ".record_message_record",
    "RunStatus": ".run_status",
    "SetupOutput": ".setup_output",
    "SetupOutput_Control": ".setup_output",
    "SetupOutput_Log": ".setup_output",
    "SourceConfig": ".source_config",
    "SourceConfigMetronome": ".source_config_metronome",
    "SourceConfigPostgres": ".source_config_postgres",
    "SourceConfigStripe": ".source_config_stripe",
    "SourceConfig_Metronome": ".source_config",
    "SourceConfig_Postgres": ".source_config",
    "SourceConfig_Stripe": ".source_config",
    "SourceInputMessage": ".source_input_message",
    "SourceMetronomeConfig": ".source_metronome_config",
    "SourcePostgresConfig": ".source_postgres_config",
    "SourceState": ".source_state",
    "SourceStateMessage": ".source_state_message",
    "SourceStateMessageSourceState": ".source_state_message_source_state",
    "SourceStateMessageSourceStateGlobal": ".source_state_message_source_state_global",
    "SourceStateMessageSourceStateStream": ".source_state_message_source_state_stream",
    "SourceStateMessageSourceState_Global": ".source_state_message_source_state",
    "SourceStateMessageSourceState_Stream": ".source_state_message_source_state",
    "SourceStripeConfig": ".source_stripe_config",
    "SourceStripeConfigApiVersion": ".source_stripe_config_api_version",
    "SpecMessage": ".spec_message",
    "SpecMessageSpec": ".spec_message_spec",
    "StreamProgress": ".stream_progress",
    "StreamProgressCompletedRangesItem": ".stream_progress_completed_ranges_item",
    "StreamProgressStatus": ".stream_progress_status",
    "StreamProgressTotalRange": ".stream_progress_total_range",
    "StreamStatusMessage": ".stream_status_message",
    "StreamStatusMessageStreamStatus": ".stream_status_message_stream_status",
    "StreamStatusMessageStreamStatusComplete": ".stream_status_message_stream_status_complete",
    "StreamStatusMessageStreamStatusError": ".stream_status_message_stream_status_error",
    "StreamStatusMessageStreamStatusRangeComplete": ".stream_status_message_stream_status_range_complete",
    "StreamStatusMessageStreamStatusRangeCompleteRangeComplete": ".stream_status_message_stream_status_range_complete_range_complete",
    "StreamStatusMessageStreamStatusSkip": ".stream_status_message_stream_status_skip",
    "StreamStatusMessageStreamStatusStart": ".stream_status_message_stream_status_start",
    "StreamStatusMessageStreamStatusStartTimeRange": ".stream_status_message_stream_status_start_time_range",
    "StreamStatusMessageStreamStatus_Complete": ".stream_status_message_stream_status",
    "StreamStatusMessageStreamStatus_Error": ".stream_status_message_stream_status",
    "StreamStatusMessageStreamStatus_RangeComplete": ".stream_status_message_stream_status",
    "StreamStatusMessageStreamStatus_Skip": ".stream_status_message_stream_status",
    "StreamStatusMessageStreamStatus_Start": ".stream_status_message_stream_status",
    "SyncOutput": ".sync_output",
    "SyncOutput_ConnectionStatus": ".sync_output",
    "SyncOutput_Control": ".sync_output",
    "SyncOutput_Eof": ".sync_output",
    "SyncOutput_Log": ".sync_output",
    "SyncOutput_Progress": ".sync_output",
    "SyncOutput_SourceState": ".sync_output",
    "SyncOutput_StreamStatus": ".sync_output",
    "SyncState": ".sync_state",
    "SyncStateSyncRun": ".sync_state_sync_run",
    "TeardownOutput": ".teardown_output",
    "TeardownOutput_Log": ".teardown_output",
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
    "BadRequestErrorBody",
    "CatalogMessage",
    "CatalogMessageCatalog",
    "CatalogMessageCatalogStreamsItem",
    "CheckOutput",
    "CheckOutput_ConnectionStatus",
    "CheckOutput_Log",
    "ConnectionStatusMessage",
    "ConnectionStatusMessageConnectionStatus",
    "ConnectionStatusMessageConnectionStatusStatus",
    "ControlMessage",
    "ControlMessageControl",
    "ControlMessageControlDestinationConfig",
    "ControlMessageControlDestinationConfigDestinationConfig",
    "ControlMessageControlSourceConfig",
    "ControlMessageControlSourceConfigSourceConfig",
    "ControlMessageControl_DestinationConfig",
    "ControlMessageControl_SourceConfig",
    "DestinationConfig",
    "DestinationConfigGoogleSheets",
    "DestinationConfigPostgres",
    "DestinationConfigRedis",
    "DestinationConfigStripe",
    "DestinationConfig_GoogleSheets",
    "DestinationConfig_Postgres",
    "DestinationConfig_Redis",
    "DestinationConfig_Stripe",
    "DestinationGoogleSheetsConfig",
    "DestinationOutput",
    "DestinationPostgresConfig",
    "DestinationPostgresConfigAws",
    "DestinationRedisConfig",
    "DestinationStripeConfig",
    "DestinationStripeConfigApiVersion",
    "DestinationStripeConfigObject",
    "DestinationStripeConfigStreamsValue",
    "DestinationStripeConfigWriteMode",
    "DiscoverOutput",
    "DiscoverOutput_Catalog",
    "DiscoverOutput_Log",
    "EofMessage",
    "EofPayload",
    "LogMessage",
    "LogMessageLog",
    "LogMessageLogLevel",
    "Message",
    "Message_Catalog",
    "Message_ConnectionStatus",
    "Message_Control",
    "Message_Eof",
    "Message_Log",
    "Message_Progress",
    "Message_Record",
    "Message_SourceInput",
    "Message_SourceState",
    "Message_Spec",
    "Message_StreamStatus",
    "PipelineConfig",
    "PipelineConfigStreamsItem",
    "PipelineConfigStreamsItemSyncMode",
    "ProgressMessage",
    "ProgressPayload",
    "ProgressPayloadConnectionStatus",
    "ProgressPayloadConnectionStatusStatus",
    "ProgressPayloadDerived",
    "RecordMessage",
    "RecordMessageRecord",
    "RunStatus",
    "SetupOutput",
    "SetupOutput_Control",
    "SetupOutput_Log",
    "SourceConfig",
    "SourceConfigMetronome",
    "SourceConfigPostgres",
    "SourceConfigStripe",
    "SourceConfig_Metronome",
    "SourceConfig_Postgres",
    "SourceConfig_Stripe",
    "SourceInputMessage",
    "SourceMetronomeConfig",
    "SourcePostgresConfig",
    "SourceState",
    "SourceStateMessage",
    "SourceStateMessageSourceState",
    "SourceStateMessageSourceStateGlobal",
    "SourceStateMessageSourceStateStream",
    "SourceStateMessageSourceState_Global",
    "SourceStateMessageSourceState_Stream",
    "SourceStripeConfig",
    "SourceStripeConfigApiVersion",
    "SpecMessage",
    "SpecMessageSpec",
    "StreamProgress",
    "StreamProgressCompletedRangesItem",
    "StreamProgressStatus",
    "StreamProgressTotalRange",
    "StreamStatusMessage",
    "StreamStatusMessageStreamStatus",
    "StreamStatusMessageStreamStatusComplete",
    "StreamStatusMessageStreamStatusError",
    "StreamStatusMessageStreamStatusRangeComplete",
    "StreamStatusMessageStreamStatusRangeCompleteRangeComplete",
    "StreamStatusMessageStreamStatusSkip",
    "StreamStatusMessageStreamStatusStart",
    "StreamStatusMessageStreamStatusStartTimeRange",
    "StreamStatusMessageStreamStatus_Complete",
    "StreamStatusMessageStreamStatus_Error",
    "StreamStatusMessageStreamStatus_RangeComplete",
    "StreamStatusMessageStreamStatus_Skip",
    "StreamStatusMessageStreamStatus_Start",
    "SyncOutput",
    "SyncOutput_ConnectionStatus",
    "SyncOutput_Control",
    "SyncOutput_Eof",
    "SyncOutput_Log",
    "SyncOutput_Progress",
    "SyncOutput_SourceState",
    "SyncOutput_StreamStatus",
    "SyncState",
    "SyncStateSyncRun",
    "TeardownOutput",
    "TeardownOutput_Log",
]
