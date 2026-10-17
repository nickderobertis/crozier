

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .postgres_config_response_output_session_replication_role import PostgresConfigResponseOutputSessionReplicationRole


class PostgresConfigResponseOutput(UniversalBaseModel):
    effective_cache_size: typing.Optional[str] = None
    logical_decoding_work_mem: typing.Optional[str] = None
    cron_log_statement: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="cron.log_statement"), pydantic.Field(alias="cron.log_statement")
    ] = None
    log_autovacuum_min_duration: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default unit: ms
    """

    log_checkpoints: typing.Optional[bool] = None
    log_connections: typing.Optional[bool] = None
    log_disconnections: typing.Optional[bool] = None
    log_duration: typing.Optional[bool] = None
    log_lock_waits: typing.Optional[bool] = None
    log_recovery_conflict_waits: typing.Optional[bool] = None
    log_replication_commands: typing.Optional[bool] = None
    log_startup_progress_interval: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default unit: ms
    """

    log_temp_files: typing.Optional[str] = None
    maintenance_work_mem: typing.Optional[str] = None
    track_activity_query_size: typing.Optional[str] = None
    max_connections: typing.Optional[int] = None
    max_locks_per_transaction: typing.Optional[int] = None
    max_logical_replication_workers: typing.Optional[int] = None
    max_parallel_maintenance_workers: typing.Optional[int] = None
    max_parallel_workers: typing.Optional[int] = None
    max_parallel_workers_per_gather: typing.Optional[int] = None
    max_replication_slots: typing.Optional[int] = None
    max_slot_wal_keep_size: typing.Optional[str] = None
    max_standby_archive_delay: typing.Optional[str] = None
    max_standby_streaming_delay: typing.Optional[str] = None
    max_sync_workers_per_subscription: typing.Optional[int] = None
    max_wal_size: typing.Optional[str] = None
    max_wal_senders: typing.Optional[int] = None
    max_worker_processes: typing.Optional[int] = None
    session_replication_role: typing.Optional[PostgresConfigResponseOutputSessionReplicationRole] = None
    shared_buffers: typing.Optional[str] = None
    statement_timeout: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default unit: ms
    """

    track_commit_timestamp: typing.Optional[bool] = None
    wal_keep_size: typing.Optional[str] = None
    wal_sender_timeout: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default unit: ms
    """

    work_mem: typing.Optional[str] = None
    checkpoint_timeout: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default unit: s
    """

    hot_standby_feedback: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
