



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .conflict_error_body import ConflictErrorBody
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
    from .destination_postgres_config import DestinationPostgresConfig
    from .destination_postgres_config_aws import DestinationPostgresConfigAws
    from .destination_redis_config import DestinationRedisConfig
    from .destination_stripe_config import DestinationStripeConfig
    from .destination_stripe_config_api_version import DestinationStripeConfigApiVersion
    from .destination_stripe_config_object import DestinationStripeConfigObject
    from .destination_stripe_config_streams_value import DestinationStripeConfigStreamsValue
    from .destination_stripe_config_write_mode import DestinationStripeConfigWriteMode
    from .eof_payload import EofPayload
    from .not_found_error_body import NotFoundErrorBody
    from .pipeline import Pipeline
    from .pipeline_desired_status import PipelineDesiredStatus
    from .pipeline_status import PipelineStatus
    from .pipeline_streams_item import PipelineStreamsItem
    from .pipeline_streams_item_sync_mode import PipelineStreamsItemSyncMode
    from .progress_payload import ProgressPayload
    from .progress_payload_connection_status import ProgressPayloadConnectionStatus
    from .progress_payload_connection_status_status import ProgressPayloadConnectionStatusStatus
    from .progress_payload_derived import ProgressPayloadDerived
    from .run_status import RunStatus
    from .source_config import SourceConfig, SourceConfig_Metronome, SourceConfig_Postgres, SourceConfig_Stripe
    from .source_config_metronome import SourceConfigMetronome
    from .source_config_postgres import SourceConfigPostgres
    from .source_config_stripe import SourceConfigStripe
    from .source_metronome_config import SourceMetronomeConfig
    from .source_postgres_config import SourcePostgresConfig
    from .source_state import SourceState
    from .source_stripe_config import SourceStripeConfig
    from .source_stripe_config_api_version import SourceStripeConfigApiVersion
    from .stream_progress import StreamProgress
    from .stream_progress_completed_ranges_item import StreamProgressCompletedRangesItem
    from .stream_progress_status import StreamProgressStatus
    from .stream_progress_total_range import StreamProgressTotalRange
    from .sync_state import SyncState
    from .sync_state_sync_run import SyncStateSyncRun
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "ConflictErrorBody": ".conflict_error_body",
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
    "DestinationPostgresConfig": ".destination_postgres_config",
    "DestinationPostgresConfigAws": ".destination_postgres_config_aws",
    "DestinationRedisConfig": ".destination_redis_config",
    "DestinationStripeConfig": ".destination_stripe_config",
    "DestinationStripeConfigApiVersion": ".destination_stripe_config_api_version",
    "DestinationStripeConfigObject": ".destination_stripe_config_object",
    "DestinationStripeConfigStreamsValue": ".destination_stripe_config_streams_value",
    "DestinationStripeConfigWriteMode": ".destination_stripe_config_write_mode",
    "EofPayload": ".eof_payload",
    "NotFoundErrorBody": ".not_found_error_body",
    "Pipeline": ".pipeline",
    "PipelineDesiredStatus": ".pipeline_desired_status",
    "PipelineStatus": ".pipeline_status",
    "PipelineStreamsItem": ".pipeline_streams_item",
    "PipelineStreamsItemSyncMode": ".pipeline_streams_item_sync_mode",
    "ProgressPayload": ".progress_payload",
    "ProgressPayloadConnectionStatus": ".progress_payload_connection_status",
    "ProgressPayloadConnectionStatusStatus": ".progress_payload_connection_status_status",
    "ProgressPayloadDerived": ".progress_payload_derived",
    "RunStatus": ".run_status",
    "SourceConfig": ".source_config",
    "SourceConfigMetronome": ".source_config_metronome",
    "SourceConfigPostgres": ".source_config_postgres",
    "SourceConfigStripe": ".source_config_stripe",
    "SourceConfig_Metronome": ".source_config",
    "SourceConfig_Postgres": ".source_config",
    "SourceConfig_Stripe": ".source_config",
    "SourceMetronomeConfig": ".source_metronome_config",
    "SourcePostgresConfig": ".source_postgres_config",
    "SourceState": ".source_state",
    "SourceStripeConfig": ".source_stripe_config",
    "SourceStripeConfigApiVersion": ".source_stripe_config_api_version",
    "StreamProgress": ".stream_progress",
    "StreamProgressCompletedRangesItem": ".stream_progress_completed_ranges_item",
    "StreamProgressStatus": ".stream_progress_status",
    "StreamProgressTotalRange": ".stream_progress_total_range",
    "SyncState": ".sync_state",
    "SyncStateSyncRun": ".sync_state_sync_run",
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
    "ConflictErrorBody",
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
    "DestinationPostgresConfig",
    "DestinationPostgresConfigAws",
    "DestinationRedisConfig",
    "DestinationStripeConfig",
    "DestinationStripeConfigApiVersion",
    "DestinationStripeConfigObject",
    "DestinationStripeConfigStreamsValue",
    "DestinationStripeConfigWriteMode",
    "EofPayload",
    "NotFoundErrorBody",
    "Pipeline",
    "PipelineDesiredStatus",
    "PipelineStatus",
    "PipelineStreamsItem",
    "PipelineStreamsItemSyncMode",
    "ProgressPayload",
    "ProgressPayloadConnectionStatus",
    "ProgressPayloadConnectionStatusStatus",
    "ProgressPayloadDerived",
    "RunStatus",
    "SourceConfig",
    "SourceConfigMetronome",
    "SourceConfigPostgres",
    "SourceConfigStripe",
    "SourceConfig_Metronome",
    "SourceConfig_Postgres",
    "SourceConfig_Stripe",
    "SourceMetronomeConfig",
    "SourcePostgresConfig",
    "SourceState",
    "SourceStripeConfig",
    "SourceStripeConfigApiVersion",
    "StreamProgress",
    "StreamProgressCompletedRangesItem",
    "StreamProgressStatus",
    "StreamProgressTotalRange",
    "SyncState",
    "SyncStateSyncRun",
]
