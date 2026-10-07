

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1alter_offset_request_info import ConnectV1AlterOffsetRequestInfo
from .connect_v1alter_offset_status_previous_offsets_item import ConnectV1AlterOffsetStatusPreviousOffsetsItem
from .connect_v1alter_offset_status_status import ConnectV1AlterOffsetStatusStatus


class ConnectV1AlterOffsetStatus(UniversalBaseModel):
    """
    Status of the alter offset operation. The previous offsets in the response
    is the offsets that the connector last processed, before the offsets were altered,
    via a patch or delete operation.
    """

    request: ConnectV1AlterOffsetRequestInfo
    status: ConnectV1AlterOffsetStatusStatus
    previous_offsets: typing.Optional[typing.List[ConnectV1AlterOffsetStatusPreviousOffsetsItem]] = pydantic.Field(
        default=None
    )
    """
    Array of offsets which are categorised into partitions.
    """

    applied_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the offsets were applied. The time is in UTC, ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
