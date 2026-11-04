

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipeline_config_streams_item_sync_mode import PipelineConfigStreamsItemSyncMode


class PipelineConfigStreamsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Stream (table) name to sync.
    """

    sync_mode: typing.Optional[PipelineConfigStreamsItemSyncMode] = pydantic.Field(default=None)
    """
    How the source reads this stream. Defaults to full_refresh.
    """

    fields: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    If set, only these fields are synced.
    """

    backfill_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Cap backfill to this many records, then mark the stream complete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
