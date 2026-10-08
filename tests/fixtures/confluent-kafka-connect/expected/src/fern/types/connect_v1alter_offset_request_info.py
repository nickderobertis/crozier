

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connect_v1alter_offset_request_info_offsets_item import ConnectV1AlterOffsetRequestInfoOffsetsItem
from .connect_v1alter_offset_request_type import ConnectV1AlterOffsetRequestType


class ConnectV1AlterOffsetRequestInfo(UniversalBaseModel):
    """
    The request made to alter offsets.
    """

    id: str = pydantic.Field()
    """
    The ID of the connector.
    """

    name: str = pydantic.Field()
    """
    The name of the connector.
    """

    offsets: typing.Optional[typing.List[ConnectV1AlterOffsetRequestInfoOffsetsItem]] = pydantic.Field(default=None)
    """
    Array of offsets which are categorised into partitions.
    """

    requested_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the request was made. The time is in UTC, ISO 8601 format.
    """

    type: ConnectV1AlterOffsetRequestType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
