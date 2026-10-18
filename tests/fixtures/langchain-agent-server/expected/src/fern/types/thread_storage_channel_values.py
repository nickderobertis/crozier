

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_storage_channel_values_by_channel_value import ThreadStorageChannelValuesByChannelValue


class ThreadStorageChannelValues(UniversalBaseModel):
    """
    Stored channel values, one row per channel version.
    """

    count: int
    bytes: int
    by_channel: typing.Dict[str, ThreadStorageChannelValuesByChannelValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
