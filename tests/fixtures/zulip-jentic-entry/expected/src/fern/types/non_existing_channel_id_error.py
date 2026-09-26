

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NonExistingChannelIdError(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    code: typing.Optional[typing.Any] = None
    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The channel ID that could not be found.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
