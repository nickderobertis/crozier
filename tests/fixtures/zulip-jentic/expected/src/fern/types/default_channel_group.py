

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DefaultChannelGroup(UniversalBaseModel):
    """
    Dictionary containing details of a default channel
    group.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the default channel group.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the default channel group.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the default channel group.
    """

    streams: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    An array of IDs of all the channels in the default stream group.
    
    **Changes**: Before Zulip 10.0 (feature level 330), we sent array
    of dictionaries where each dictionary contained details about a
    single stream in the default stream group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
